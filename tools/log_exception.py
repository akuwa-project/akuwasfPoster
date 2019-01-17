# -*- coding: utf-8 -*-

import logging
from enum import Enum

logging.basicConfig(filename='duniya.log', level=logging.DEBUG, format='[%(levelname)s] %(asctime)s  "%(message)s"',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

LOG_ERROR = "%a, %d %b %Y %H:%M:%S GMT"


class LOG_TYPE(Enum):
    ERROR = 1
    INFO = 2
    DEBUG = 3
    WARNING = 4
    CRITICAL = 5


class DUNIYA_EXCEPTION_TYPE(Enum):
    FILE_VALIDATION_EXCEPTION = 1
    MONGO_CONNECTION_EXCEPTION = 2
    FILE_SERVER_CONNECTION_EXCEPTION = 3
    RUNTIME_CALL_EXCEPTION = 4
    MONGO_INSERTION_EXCEPTION = 5
    PARSING_EXCEPTION = 6
    TEMPLATE_WRITING_EXCEPTION = 7
    NON_CONFORMING_DATA = 8


def printLog(log_type, duniya_exception, msg):
    if log_type == LOG_TYPE.ERROR:
        logging.error(duniya_exception.name + " : " + msg)
    elif log_type == LOG_TYPE.INFO:
        logging.info(duniya_exception.name + " : " + msg)
    elif log_type == LOG_TYPE.DEBUG:
        logging.debug(duniya_exception.name + " : " + msg)
    elif log_type == LOG_TYPE.WARNING:
        logging.warning(duniya_exception.name + " : " + msg)
    elif log_type == LOG_TYPE.CRITICAL:
        logging.critical(duniya_exception.name + " : " + msg)
    else:
        logging.info(duniya_exception + " : " + msg)


def info(msg):
    logging.INFO(str(msg))

