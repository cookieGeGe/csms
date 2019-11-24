# -*- coding: utf-8 -*-
# @Time : 2019/11/20
# @Author : zhang
# @Site :
# @File : labor_view.py
# @Software: PyCharm
from flask import jsonify

from utils.BaseView import BaseView


class WechatLaborBase(BaseView):

    def __init__(self):
        super(WechatLaborBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        pass


class WechatLaborQuery(WechatLaborBase):

    def __init__(self):
        super(WechatLaborQuery, self).__init__()

    def admin(self):
        """以项目ID为基准"""
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
            select t1.id, t1.name, t1.avatar, t1.age, t1.sex, t1.jobtype, t1.nationality, t1.createtime, t4.name as pid,
             t5.name as cid, t6.name as did, t2.name as project, t3.name as company,
              t1.isbadrecord from tb_laborinfo as t1
            left join tb_project as t2 on t1.ProjectID = t2.id
            left join tb_company as t3 on t1.CompanyID = t3.id
            INNER JOIN tb_area as t4 on t1.PID = t4.id
            INNER JOIN tb_area as t5 on t1.CID = t5.id
            INNER JOIN tb_area as t6 on t1.CID = t6.id
        """
        where_sql_list = []
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            where_sql_list.append(r""" t1.projectid in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if int(self.args.get('status', '3')) != 3:
            where_sql_list.append(r""" t1.isbadrecord={} """.format(self.args.get('status')))
        if int(self.args.get('sex', 2)) != 2:
            where_sql_list.append(r""" t1.sex={} """.format(self.args.get('sex')))
        if int(self.args.get('jobtype', 5)) != 5:
            where_sql_list.append(r""" t1.jobtype='{}' """.format(int(self.args.get('jobtype'))))
        if int(self.args.get('education', 7)) != 7:
            where_sql_list.append(r""" t1.education='{}' """.format(int(self.args.get('education'))))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t1.pid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t1.cid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t1.did={} """.format(self.args.get('did')))
        if int(self.args.get('age', 6)) != 6:
            if int(self.args.get('age', 0)) == 0:
                where_sql_list.append(r""" t1.Age<18 """)
            if int(self.args.get('age', 0)) == 1:
                where_sql_list.append(r""" t1.Age>=18 and t1.Age<30  """)
            if int(self.args.get('age', 0)) == 2:
                where_sql_list.append(r""" t1.Age>=30 and t1.Age<39  """)
            if int(self.args.get('age', 0)) == 3:
                where_sql_list.append(r"""  t1.Age>=39 and t1.Age<49 """)
            if int(self.args.get('age', 0)) == 4:
                where_sql_list.append(r"""  t1.Age>=49 and t1.Age<55  """)
            if int(self.args.get('age', 0)) == 5:
                where_sql_list.append(r""" t1.Age>=55 """)
        if self.args.get('time', '') != '':
            where_sql_list.append(r""" t1.createtime > '{}' """.format(self.args.get('time')))
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
            if item['createtime'] is not None and item['createtime'] != '':
                item['createtime'] = self.time_to_str(item['createtime'])
            if item['isbadrecord'] > 0:
                alarm += 1
        self.success['project'] = result
        self.success['total'] = total[0]['total_row']
        self.success['alarm'] = alarm
        return self.success

    def one_labor_query(self):
        pass

    def views(self):
        if int(self.args.get('id', '0')) == 0:
            success = self.main_list_query()
        else:
            success = self.one_labor_query()

        return jsonify(success)
