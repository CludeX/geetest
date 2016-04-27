#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis
import config


class PushList:
    def __init__(self, host=config.REDIS_HOST, port=config.REDIS_ADDR):
        self.host = host
        self.port = port

    def connect_redis(self):
        my_redis = redis.StrictRedis(host=self.host, port=self.port, db=0)
        return my_redis

    @classmethod
    def push(cls, event):
        push_list = cls()
        my_redis = push_list.connect_redis()
        my_redis.rpush(config.REDIS_LIST, event)
        return True

if __name__ == '__main__':
    # for i in range(10):
    #     event = r'id=mongo&level=%i'%i
    #     PushList.push(event)
    event = r'id=mongo&level=1&data=fdafdsafasdf'
    PushList.push(event)
    event = r'id=mfdafdongo'
    PushList.push(event)
    print event

