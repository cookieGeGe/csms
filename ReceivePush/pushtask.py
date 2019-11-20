# -*- coding: utf-8 -*-
# @Time : 2019/11/11
# @Author : zhang
# @Site :
# @File : pushtask.py
# @Software: PyCharm
import time

from celery import Celery

from APP.settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from ReceivePush.push_attend import PushAttend


def make_celery():
    celery = Celery(__name__,
                    broker=CELERY_BROKER_URL,
                    backend=CELERY_RESULT_BACKEND
                    )
    return celery


celery = make_celery()


@celery.task
def deal_push_attend(args):
    # print(args)
    pushattend = PushAttend(args)
    data = pushattend.check_has_data()
    t_id, field = pushattend.check_in_or_out()
    if not data:
        pushattend.insert_or_update(1, field, field + 'pos')
        return
    if pushattend.need_deal_data(t_id, field, data):
        pushattend.insert_or_update(0, field, field + 'pos')
