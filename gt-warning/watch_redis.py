#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import re
import time

import config
from lib.send_method import do_some_thing


def check_if_fmt_valid(list_str):
    pattern = re.compile(r'id=.*&level=\d{1}')
    if pattern.match(list_str):
        return True
    else:
        return False


def check_if_level_valid(list_str):
    level = list_str.split('&')[1].split('=')[1]
    if int(level) in range(1, 4):
        return True
    else:
        return False


def get_redis_event(r, mongo):
    while True:
        try:
            list_name, event = r.brpop(config.REDIS_LIST, timeout=30)
            if check_if_fmt_valid(event):
                if check_if_level_valid(event):
                    now_time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
                    event = event + '&time=' + now_time
                    do_some_thing(mongo, event)
                    continue
            # 错误事件直接写入日志
            mongo.HistoryLog.insert({
                "_id": event,
                "active": -2,
                "name": "other",
                "time": datetime.datetime.now()
            })
        except Exception as e:
            print e
            continue
