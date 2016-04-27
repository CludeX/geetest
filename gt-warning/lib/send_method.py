# coding:utf-8
import datetime

from gtweixin import Weixin
from gtemail import send_email
from utils import get_logger

def do_some_thing(db, event):
    try:
        get_logger(event)
        event_list = event.split("&")
        event = {}
        for e in event_list:
            e_list = e.split("=")
            event[e_list[0]] = e_list[1]
        channel = db.Channel.find_one({"_id": event["id"]})
        level = "level" + str(event["level"])
        data_text = event.get("data", "rt")

        if not channel:
            nowtime = datetime.datetime.now()
            db.HistoryLog.insert({
                "_id": event["id"] + "-" + event["level"] + "-" + nowtime.strftime("%Y%m%d%H%M%S"),
                "name": event["id"],
                "level": level,
                "active": -1,
                "time": nowtime
            })
            return

        groups = channel["event"][level]["groups"]
        operations = channel["event"][level]["operation"]
        await_time = int(channel["event"][level]["await"])
        members = []

        if await_time < 1 or await_time > 60:
            await_time = 10

        nowtime = datetime.datetime.now()
        starttime = datetime.datetime.now() - datetime.timedelta(minutes=await_time)
        count = db.HistoryLog.find({
            "name": event["id"],
            "level": level,
            "active": 1,
            "time": {"$gte": starttime}
        }).count()

        data_id = event["id"] + "-" + event["level"] + "-" + nowtime.strftime("%Y%m%d%H%M%S")

        data = {
            "_id": data_id,
            "name": event["id"],
            "level": level,
            "active": 0,
            "time": nowtime
        }
        print count
        if count == 0:
            for gid in groups:
                group = db.Group.find_one({"_id": gid})
                members += group.get("members", [])

            members = list(set(members))
            email_list = []
            wx_text = "%s异常,\"%s\"级警报,详细内容:%s" % (event["id"], event["level"], data_text)
            for mid in members:
                member = db.Member.find_one({"_id": mid})
                email_list.append(member['email'])
                if "message" in operations:
                    try:
                        wx = str(member["wechat"])
                        w = Weixin()
                        w.send_msg(wx_text, [wx])
                    except Exception as e:
                        print e
                if 'tel' in operations:
                    # 打电话
                    pass
            send_email(email_list, event["id"], event["level"], data_text)
            data["active"] = 1

        print data
        db.HistoryLog.insert(data)
    except Exception as e:
        get_logger(e)
        print e