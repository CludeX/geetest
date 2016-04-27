# coding:utf-8
from models.base import Base


class Channel(object):
    fields = ["_id", "event", "create_time", "level"]
    filter_fields = ["event", "create_time", "level"]

    default = {
        "event": {
            "level1": {
                "operation": [],
                "groups": [],
                "person": "",
                "await": 10
            }
        },
        "create_time": Base.set_create_time(),
        "level": 1
    }

    def __init__(self, _id, **kwargs):
        self._id = _id
        self.body = kwargs['body']

    def get(self):
        channel = {}
        channel["_id"] = self._id
        for i in self.filter_fields:
            channel[i] = self._filter(i)
        return channel

    def _filter(self, name):
        return self.body.get(name, self.default.get(name))
