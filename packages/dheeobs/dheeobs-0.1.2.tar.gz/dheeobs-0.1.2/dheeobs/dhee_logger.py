import logging
from .dhee_loghandler import DheeLogHandler


class DheeLogger:
    POD_PARAMETERS = {}

    @staticmethod
    def get_logger(**log_params):
        """
        Invokes DheeLogger Handler
        :param log_params: Log Integrations like InfluxDB,Cloudwatch,etc, Log Level , Glue Context
        :return logger object
        """
        logger = logging.getLogger(__name__)
        dhee_logger_handler = DheeLogHandler(**log_params)
        logger.addHandler(dhee_logger_handler)
        DheeLogger.POD_PARAMETERS = dhee_logger_handler.get_run_parameters()
        logger.setLevel(log_params.get('loglevel'))
        return logger


    @staticmethod
    def get_pod_parameter(paramName):
        if paramName in DheeLogger.POD_PARAMETERS:
            return DheeLogger.POD_PARAMETERS.get(paramName)
        return None
