# coding:utf-8
import datetime
import os

NAME = "gt-warning"
DEBUG = True
APP_HOST = "127.0.0.1"
APP_ADDR = 8030

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = ROOT_DIR + "/%s" % NAME
STATIC_DIR = ROOT_DIR + "/%s/static" % NAME
TEMPLATE_DIR = ROOT_DIR + "/%s/static/templates" % NAME

MONGO_HOST = "127.0.0.1"
MONGO_ADDR = 27017
TEST_HOST = "127.0.0.1"
TEST_ADDR = 27017

REDIS_HOST = "127.0.0.1"
REDIS_ADDR = 6379
REDIS_LIST = 'testList'

TODAY = datetime.datetime.today().strftime("%Y-%m-%d")
LOG_LEVEL = "WARNING"
# LOG_PATH = BASE_DIR + "/log/%s-tornado_angular2_qs.log"%TODAY
LOG_PATH = BASE_DIR + "/log/warning.log"

try:
    from local_config import *
except:
    pass
