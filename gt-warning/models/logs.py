# coding:utf-8


class HistoryLog(object):
    fields = ["_id", "name", "level", "time", "active"]
    filter_fields = ["name", "level", "time", "active"]

    default = {
        "name": "",
        "level": "",
        "time": "",
        "active": ""
    }

    def __init__(self, _id, **kwargs):
        self._id = _id
        self.body = kwargs['body']

    def get(self):
        log = {}
        log["_id"] = self._id
        for i in self.filter_fields:
            log[i] = self._filter(i)
        return log

    def _filter(self, name):
        return self.body.get(name, self.default.get(name))
