# -*- coding: utf-8 -*-
# @Time : 2019/11/27
# @Author : zhang
# @Site :
# @File : guarantee_view.py
# @Software: PyCharm
import datetime

from utils.BaseView import BaseView


class GuaranteeBase(BaseView):

    def __init__(self):
        super(GuaranteeBase, self).__init__()
        self.is_admin = 0

    def administrator(self):
        return self.views()

    def admin(self):
        self.is_admin = 1
        query_sql = r"""
                    select guarantee_pren from tb_user where id={};
                """.format(self._uid)
        result = self._db.query(query_sql)
        result = result[0]
        self.show_useer_id_list = []
        self.show_useer_id_list.append(str(self._uid))
        if result['guarantee_pren'] is None:
            result['guarantee_pren'] = ''
        if result['guarantee_pren'] != '':
            self.show_useer_id_list.extend(result['guarantee_pren'].split(','))
        return self.views()

    def views(self):
        pass


class GuaranteeQuery(GuaranteeBase):

    def __init__(self):
        super(GuaranteeQuery, self).__init__()

    def main_query(self):
        query_sql = r"""
            select SQL_CALC_FOUND_ROWS t1.id, t1.number, t1.projectid, t1.companyid, t1.signtime, t1.expiretime,
             t1.bene,t1.category,t1.amount, t2.name as pname, t3.name as cname, t4.name as dname from tb_guarantee as t1
            INNER JOIN tb_area as t2 on t1.pid = t2.id
            INNER JOIN tb_area as t3 on t1.cid = t3.id
            INNER JOIN tb_area as t4 on t1.did = t4.id
        """
        where_sql_list = []
        if self.args.get('name', '') != '':
            where_sql_list.append(
                r""" CONCAT(IFNULL(t1.number,''),IFNULL(t1.projectid,''),IFNULL(t1.companyid,'')) LIKE '%{}%' """.format(
                    self.args.get('name')
                )
            )
        if self.is_admin == 1:
            if len(self.show_useer_id_list):
                where_sql_list.append(r""" t1.CreateUser in ({}) """.format(','.join(self.show_useer_id_list)))
        if int(self.args.get('type', '9')) != 9:
            where_sql_list.append(r""" t1.category={} """.format(self.args.get('type')))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t1.pid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t1.cid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t1.did={} """.format(self.args.get('did')))
        if self.args.get('time', '') != '':
            # print(self.args.get('time'))
            where_sql_list.append(
                r""" t1.createtime>='{}' """.format(self.args.get('time').replace('T', ' ').replace('Z', '')))
            print(self.args.get('time'))
        where_sql = self.get_where_sql(where_sql_list)
        page = int(self.args.get('page', '1'))
        limit_sql = r"""order by t1.CreateTime desc limit {},{} """.format((page - 1) * 10, 10)
        total_query_sql = query_sql + where_sql + limit_sql
        result, total = self.get_total_query(total_query_sql)
        for item in result:
            item['signtime'] = '' if item['signtime'] is None or item['signtime'] == '' else item['signtime'].strftime(
                "%Y-%m-%d")
            item['is_expiretime'] = 0
            if item['expiretime'] is None or item['expiretime'] == '':
                item['expiretime'] = ''
            else:
                now_time = datetime.datetime.now()
                if item['expiretime'] < now_time:
                    item['is_expiretime'] = 1
                item['expiretime'] = item['expiretime'].strftime("%Y-%m-%d")
        self.success['guarantee'] = result
        self.success['total'] = total[0]['total_row']
        return self.success

    def get_pic_groups(self):
        query_sql = r"""select id, name as text, Type, id as value from tb_pic_group where CID={} and Ptype = 0""".format(
            self.args.get('id')
        )
        result_list = self._db.query(query_sql)
        # for index, item in enumerate(result_list):
        #     item['value'] = index
        return [{
            "name": "保函照片",
            "list": result_list
        }]

    def get_one_guarantee(self):
        query_sql = r"""
            select t1.*, t2.name as pname, t3.name as cname, t4.name as dname from tb_guarantee as t1
            INNER JOIN tb_area as t2 on t1.pid = t2.id
            INNER JOIN tb_area as t3 on t1.cid = t3.id
            INNER JOIN tb_area as t4 on t1.did = t4.id
            where t1.id={}
        """.format(self.args.get('id'))
        result = self._db.query(query_sql)
        for item in result:
            item['SignTime'] = '' if item['SignTime'] is None or item['SignTime'] == '' else item['SignTime'].strftime(
                "%Y-%m-%d")
            item['is_expiretime'] = 0
            if item['Expiretime'] is None or item['Expiretime'] == '':
                item['Expiretime'] = ''
            else:
                now_time = datetime.datetime.now()
                if item['Expiretime'] < now_time:
                    item['is_expiretime'] = 1
                item['Expiretime'] = item['Expiretime'].strftime("%Y-%m-%d")
        query_cguarantee_sql = r"""
            select * from tb_cguarantee where gid = {}
        """.format(self.args.get('id'))
        c_result = self._db.query(query_cguarantee_sql)
        self.success['guarantee'] = result[0]
        self.success['cguarantee'] = c_result
        self.success['pic_groups'] = self.get_pic_groups()
        return self.success

    def views(self):
        if int(self.args.get('id', '0')) == 0:
            success = self.main_query()
        else:
            success = self.get_one_guarantee()
        return self.make_response(success)
