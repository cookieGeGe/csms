# -*- coding: utf-8 -*-
# @Time : 2019/11/20
# @Author : zhang
# @Site :
# @File : project_view.py
# @Software: PyCharm
from flask import jsonify

from utils.BaseView import BaseView


class WechatProBase(BaseView):

    def __init__(self):
        super(WechatProBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        pass


class WechatProQuery(WechatProBase):

    def __init__(self):
        super(WechatProQuery, self).__init__()

    def admin(self):
        self.ids = self.get_project_ids()
        return self.views()

    def get_total_query(self, query_sql):
        result = self._db.query(query_sql)
        total = self._db.query(self.get_total_row)
        return result, total

    def main_list_query(self):
        """
        首页和列表页面搜索
        :return:
        """
        query_sql = r"""
            select SQL_CALC_FOUND_ROWS t1.name, t1.address, t1.`status`, t1.type, t1.gamount, t1.starttime, t1.endtime, t1.guarantype,t1.wagepercent, t2.name as bank, t1.createtime  from tb_project as t1
            left join tb_bank as t2 on t1.bank = t2.id
        """
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if int(self.args.get('type', '0')) != 0:
            where_sql_list.append(r""" t1.type={} """.format(self.args.get('type')))
        if int(self.args.get('status', '0')) != 0:
            where_sql_list.append(r""" t1.status={} """.format(self.args.get('status')))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t1.pid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t1.cid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t1.did={} """.format(self.args.get('did')))
        if self.args.get('time', '') != '':
            where_sql_list.append(r""" t1.starttime > '{}' """.format(self.args.get('time')))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            where_sql += ' and '.join(where_sql_list)
        page = int(self.args.get('page', '1'))
        limit_sql = r""" limit {},{} """.format((page - 1) * 10, 10)
        total_query_sql = query_sql + where_sql + limit_sql
        result, total = self.get_total_query(total_query_sql)
        alarm = 0
        for item in result:
            if item['starttime'] is not None and item['starttime'] != '':
                item['starttime'] = self.time_to_str(item['starttime'])
            if item['endtime'] is not None and item['endtime'] != '':
                item['endtime'] = self.time_to_str(item['endtime'])
            if item['status'] > 1:
                alarm += 1
        self.success['project'] = result
        self.success['total'] = total[0]['total_row']
        self.success['alarm'] = alarm
        return self.success

    def one_project_query(self):
        pass

    def views(self):
        if int(self.args.get('id', '0')) == 0:
            success = self.main_list_query()
        else:
            success = self.one_project_query()

        return jsonify(success)
