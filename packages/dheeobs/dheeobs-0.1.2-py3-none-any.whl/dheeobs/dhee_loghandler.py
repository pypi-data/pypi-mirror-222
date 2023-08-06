import json
from datetime import datetime, timezone
import logging
import requests
import os
import sys


class DheeLogHandler(logging.Handler):

    def __init__(self, **logparams) -> None:
        super().__init__()
        self.log_integration_list = logparams.get('log_integration_list')
        if logparams.get('glueContext') is not None:
            self.glueContext = logparams.get('glueContext')
        self.run_parameters = {}

    def emit(self, record: logging.LogRecord) -> None:
        """
        Inherited Method invoked for all log levels
        :param record: logging record object
        :return:
        """
        try:

            if self.log_integration_list is not None:
                if "influxdb" in self.log_integration_list:
                    self.post_logs_to_influxdb(record)

                if "cloudwatch" in self.log_integration_list:
                    self.post_logs_to_cloudwatch(record)

        except Exception:
            self.handleError(record)

    def post_logs_to_influxdb(self, record: logging.LogRecord):
        """
        Post Logs to InfluxDB Server
        :param record: logging record object
        :return:
        """
        message = self.format(record)
        level = record.levelname
        log_location = record.filename + "::" + record.funcName + "::" + str(
            record.lineno)  # Eg., dhee_loghandler.py::post_logs_to_influxdb::45

        url = f'{self.run_parameters.get("DHEE_URL")}/log'
        headers = {
            'Authorization': 'Bearer '+self.run_parameters.get("DHEE_TOKEN"),
            'Content-Type': 'application/json'
        }


        if 'CONNECTION_FILE' not in self.run_parameters:
            payload = {
                "measurement": self.run_parameters.get("POD_ID"),
                "bucket": self.run_parameters.get("INFLUXDB_BUCKET"),
                "tags": [
                    {"key": "level", "value": level},
                ],
                "fields": [
                    {"key": "message", "value": message},
                    {"key": "location", "value": log_location},
                ]
            }
        else:
            content = message.split("#")
            payload = {
                "measurement": self.run_parameters.get("POD_ID"),
                "bucket": self.run_parameters.get("INFLUXDB_BUCKET"),
                "tags": [
                    {"key": "pipelineId", "value": self.run_parameters.get("PIPELINE_ID")},
                    {"key": "job_run_id", "value": self.run_parameters.get("JOB_RUN_ID")},
                    {"key": "expectation_type", "value": content[0]},
                    {"key": "column_name", "value": content[1]},
                    {"key": "validation_status", "value": content[2]},
                ],
                "fields":[
                    {"key": "values", "value": content[3]}
                ]
            }
        print(payload)
        response = requests.request("POST", url, headers=headers, json=payload)
        response.raise_for_status()

    def post_logs_to_cloudwatch(self, record: logging.LogRecord):
        """
        Post Logs to Cloudwatch from AWS Glue Job
        :param record: logging record object
        :return:
        """
        if hasattr(self, 'glueContext') and self.glueContext is not None and "get_logger" in dir(self.glueContext):
            glue_logger = self.glueContext.get_logger()
            message = self.format(record)
            if record.levelname == "WARNING":
                glue_logger.warn(message)
            elif record.levelname == "ERROR":
                glue_logger.error(message)
            elif record.levelname == "DEBUG":
                glue_logger.debug(message)
            else:
                glue_logger.info(message)

    def get_commandline_args(self):
        """
        To get Command Line arguments to setup integration endpoint configuration
        :return:
        """
        arguments_dict = {}
        for index, argument in enumerate(sys.argv):
            if argument.startswith("--"):
                arguments_dict[argument[2:]] = sys.argv[index + 1]
        return arguments_dict

    def get_run_parameters(self):
        if hasattr(self, 'glueContext') and self.glueContext is not None:
            args = self.get_commandline_args()
        else:
            args = {'DHEE_URL': os.getenv('DHEE_URL'), 'DHEE_TOKEN': os.getenv('DHEE_TOKEN'), 'POD_ID': os.getenv('POD_ID'),
                    'JOB_RUN_ID': os.getenv('JOB_RUN_ID')}

        dhee_url = args['DHEE_URL']
        podId = args['POD_ID']
        dhee_token = args['DHEE_TOKEN']

        url = f'{dhee_url}/pod/{podId}/runparameters'
        headers = {
            'Authorization': 'Bearer ' + dhee_token,
            'Content-Type': 'application/json'
        }
        response = requests.request('GET', url, headers=headers)
        if response is not None:
            paramJSON = json.loads(json.dumps(response.json()))
            for param in paramJSON:
                self.run_parameters.update({param: paramJSON[param]})

        self.run_parameters.update(args)
        return self.run_parameters
