# coding:utf-8
import logging
import traceback
from logging.handlers import RotatingFileHandler

import motor
import pymongo
import redis

from config import NAME, DEBUG, MONGO_ADDR, MONGO_HOST, \
    TEST_ADDR, TEST_HOST, LOG_LEVEL, LOG_PATH, \
    REDIS_ADDR, REDIS_HOST


def gee_database():
    if DEBUG:
        client = motor.MotorClient(TEST_HOST, TEST_ADDR, connectTimeoutMS=2000)
        db = client["gt_waring"]
    else:
        client = motor.MotorClient(MONGO_HOST, MONGO_ADDR, connectTimeoutMS=2000)
        db = client["gt_waring"]
    return db


def gee_redis():
    r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_ADDR, db=0)
    return r


def listen_mongo():
    if DEBUG:
        client = pymongo.Connection(TEST_HOST, TEST_ADDR, connectTimeoutMS=2000)
        db = client["gt_waring"]
    else:
        client = pymongo.Connection(MONGO_HOST, MONGO_ADDR, connectTimeoutMS=2000)
        db = client["gt_waring"]
    return db


def configure_logging():
    logging.basicConfig(
        level=LOG_LEVEL,
        format='%(asctime)s | %(levelname)s | %(message)s',
        filename=LOG_PATH,
        filemode='w',
    )
    logger = logging.getLogger(NAME)
    handler = RotatingFileHandler(LOG_PATH, maxBytes=10 * 1024 * 1024,
                                  backupCount=5)
    logger.addHandler(handler)
    return logger


logger = configure_logging()


def get_traceback():
    logger.error('%s', traceback.format_exc())


def get_logger(msg):
    logger.critical(msg)


def return_500(Handler):
    get_traceback()
    Handler.clear()
    Handler.set_status(500)
    Handler.finish("<html><body>Internal Server Error</body></html>")
