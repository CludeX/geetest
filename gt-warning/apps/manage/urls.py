# coding:utf-8
from .handler import *

url = [
    (r"/api/members", ManageHandler),
    (r"/api/members_change", ChangeManageHandler),
]
