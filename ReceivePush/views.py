# -*- coding: utf-8 -*-
# @Time : 2019/11/11
# @Author : zhang
# @Site :
# @File : views.py
# @Software: PyCharm
import random

from flask import jsonify

from ReceivePush.pushtask import deal_push_attend
from utils import status_code
from utils.BaseView import BaseView


class ReceiveAttend(BaseView):

    def __init__(self):
        super(ReceiveAttend, self).__init__()
        self.push_success = {'code': 10001, 'messages': 'SUCCESS'}
        self.push_error = {'code': 10002, 'messages': 'FAIL'}

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        # 数据预处理
        args = self.args
        if self.args_is_null('user_id', 'identityNo', 'departMentName', 'date_time', 'pass_type'):
            return jsonify(self.push_error)
        query_sql = r"""
            select t1.id as laborid, t2.id as projectid from tb_laborinfo as t1
            left join tb_project as t2 on t1.ProjectID = t2.ID
            where t1.IDCard = '{}' and t2.Name='{}';
        """.format(args.get('identityNo'), args.get('departMentName'))
        result = self._db.query(query_sql)
        if not result:
            return jsonify(self.push_error)
        args.update(result[0])
        deal_push_attend.delay(args)
        return jsonify({'code': 10001, 'messages': 'SUCCESS'})
