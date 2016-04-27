# coding:utf-8
from models.base import Base


class Group(object):
    fields = ["_id", "members", "create_time", "level"]
    filter_fields = ["members", "create_time", "level"]

    default = {
        "level": "",
        "create_time": Base.set_create_time(),
        "members": []
    }

    def __init__(self, _id, **kwargs):
        self._id = _id
        self.body = kwargs['body']

    def get(self):
        group = {}
        group["_id"] = self._id
        for i in self.filter_fields:
            group[i] = self._filter(i)
        return group

    def _filter(self, name):
        return self.body.get(name, self.default.get(name))





