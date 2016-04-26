# coding:utf-8
from .handler import *

url = [
    (r"/api/logs", LogsHandler),
    (r"/api/logs_length", LogLengthHandler),
]
