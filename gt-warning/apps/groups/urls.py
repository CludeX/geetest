# coding:utf-8
from .handler import *

url = [
    (r"/api/groups", GroupHandler),
    (r"/api/group_member", AddNewMemberHandler)
]
