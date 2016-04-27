# coding:utf-8
import logging
import os
import traceback
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

LIB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = LIB_DIR + "/log"
LOG_LEVEL = "INFO"
LOG_PATH = LOG_DIR + "/lib.log"


def configure_logging():
    logging.basicConfig(
        level=LOG_LEVEL,
        format='%(asctime)s | %(levelname)s | %(message)s',
        filename=LOG_PATH,
        filemode='w',
    )
    logger = logging.getLogger("lib.log")
    handler = RotatingFileHandler(LOG_PATH, maxBytes=10 * 1024 * 1024,
                                  backupCount=5)
    logger.addHandler(handler)
    return logger


logger = configure_logging()


def get_traceback():
    logger.error('%s', traceback.format_exc())


def get_logger(msg):
    logger.critical(msg)