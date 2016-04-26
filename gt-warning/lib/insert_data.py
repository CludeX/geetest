# coding: utf-8
import pymongo
import datetime
from config import *

gt_waring_db = pymongo.Connection(host=MONGO_HOST, port=MONGO_ADDR).gt_waring


def insert_data():
    data = []
    for i in range(1, 101):
        temp = {}
        id = i
        temp['_id'] = id
        temp['name'] = id
        temp['level'] = ''
        temp['time'] = datetime.datetime.today()
        temp['active'] = ''
        data.append(temp)
    gt_waring_db.HistoryLog.insert(data)
    print data
insert_data()
