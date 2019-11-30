# -*- coding: utf-8 -*-
# @Time : 2019/11/20
# @Author : zhang
# @Site :
# @File : labor_view.py
# @Software: PyCharm
import datetime

from flask import jsonify

from utils import status_code
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
        if self.args.get('status') != '' and self.args.get('status') == 'false':
            where_sql_list.append(r""" t1.isbadrecord>0 """)
        else:
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
        self.success['labor'] = result
        self.success['total'] = total[0]['total_row']
        self.success['alarm'] = alarm
        return self.success

    def get_all_class_labor(self):
        query_sql = r"""select id, name from tb_laborinfo 
                        where classID = (
                            select classid from tb_laborinfo where id= {0}
                        ) and id != {0};""".format(self.args.get('id'))
        return self._db.query(query_sql)

    def one_labor_query(self):
        labor_id = self.args.get('id')
        if self.args_is_null('id'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select t1.*, t2.ClassName as ClassName, t3.Name as ProjectName, t4.Name as CompanyName, t5.Name as PName, t6.Name as CName, t7.Name as DName, t8.name as SuperiorsName, t9.Name as SubCompanyName from tb_laborinfo as t1
                        left join tb_class as t2 on t1.ClassID = t2.id
                        left join tb_project as t3 on t1.projectid = t3.id
                        left join tb_company as t4 on t1.CompanyID = t4.id
                        left JOIN tb_area as t5 on t5.ID = t1.PID
                        left JOIN tb_area as t6 on t6.ID = t1.CID
                        left JOIN tb_area as t7 on t7.ID = t1.DID
                        left join tb_laborinfo as t8 on t8.id = t1.Superiors
                        left join tb_company as t9 on t9.id = t1.SubCompany
                        where t1.id = {};""".format(labor_id)
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.LABOR_IS_NOT_EXISTS)
        labor_info = result[0]
        query_pic_group = r"""select * from tb_pic_group where cid={} and ptype=2;""".format(labor_id)
        pic_group = self._db.query(query_pic_group)
        pic_group_dict = {
            'bad_list': [],
            'info': []
        }
        for item in pic_group:
            if int(item['Type']) == 0:
                pic_group_dict['bad_list'].append(item)
            else:
                pic_group_dict['info'].append(item)
        labor_info['isDeparture'] = False
        for i in ('Birthday', 'DepartureDate', 'EntryDate', 'CreateTime'):
            if labor_info[i] != None and labor_info[i] != '':
                if i == 'DepartureDate' and labor_info[i] < datetime.datetime.now():
                    labor_info['isDeparture'] = True
                labor_info[i] = labor_info[i].strftime("%Y-%m-%d")
        self.success['labor'] = labor_info
        self.success['labor']['pic_group'] = pic_group_dict
        self.success['class_labors'] = self.get_all_class_labor()
        return self.success

    def views(self):
        if int(self.args.get('id', '0')) == 0:
            success = self.main_list_query()
        else:
            success = self.one_labor_query()
        return self.make_response(success)
