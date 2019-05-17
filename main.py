# -*- coding: utf-8 -*-
import itchat
import datetime
import time

if __name__ == '__main__':
    itchat.auto_login()
    MSG = '大家好，我是本群的“提醒喝水小助手”，这是今天的第{0}轮，希望此刻看到消息的人可以和我一起来一杯水。一小时后的我继续提醒大家喝水。和我一起成为一天八杯水的人吧。'
    # group name list
    GROUP_NAMES = ['减肥俱乐部']

    member_list = itchat.get_chatrooms()
    chatrooms = [itchat.search_chatrooms(name=i)[0]['UserName'] for i in GROUP_NAMES]
    old_time = None
    while True:
        now = datetime.datetime.now()
        if old_time is not None and now.hour != old_time.hour:
            for i in chatrooms:
                itchat.send_msg(MSG.format(now.hour + 1), toUserName=i)
            print("send success " + str(now.hour + 1))
        old_time = now
        sleep = (60 - now.minute) * 60
        time.sleep(sleep)
