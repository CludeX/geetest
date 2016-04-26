# coding:utf-8
import time
import datetime
import random
import hashlib

class Base(object):
    fields = []
    filter_fields = []
    default = {}

    @staticmethod
    def set_create_time():
        return datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def create_id(sstr=None):
        ti = int(time.time())
        if not sstr:
            string = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
            random.shuffle(string)
            sstr = ''.join(string)
        rand = str(random.randint(0, 99999))
        res = str(ti) + sstr + rand
        res = hashlib.md5(res).hexdigest()
        return res