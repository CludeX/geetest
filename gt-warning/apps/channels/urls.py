# coding:utf-8
from .handler import *

url = [
    (r"/api/channels", ChannelHandler),
    (r"/api/channels/setting", SettingChannelHandler),
]
