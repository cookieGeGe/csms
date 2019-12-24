# -*- coding: utf-8 -*-
# @Time : 2019/11/26
# @Author : zhang
# @Site :
# @File : salary_view.py
# @Software: PyCharm
import datetime

from utils import status_code
from utils.BaseView import BaseView


class SalaryBase(BaseView):

    def __init__(self):
        super(SalaryBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        pass


class WechatQuerySalary(SalaryBase):

    def __init__(self):
        super(WechatQuerySalary, self).__init__()

    def admin(self):
        if self.args.get('type', 'company') == 'company':
            self.ids = self.get_company_ids()
        elif self.args.get('type', 'project') == 'project':
            self.ids = self.get_project_ids()
        else:
            self.ids = self.get_labor_ids()
        return self.views()

    def get_company_where(self):
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t4.provinceid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t4.cityid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t4.districtid={} """.format(self.args.get('did')))
        return where_sql_list

    def get_project_where(self):
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t3.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t3.name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t3.pid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t3.cid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t3.did={} """.format(self.args.get('did')))
        return where_sql_list

    def get_labor_where(self):
        where_sql_list = []
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            where_sql_list.append(r""" t2.projectid in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t2.name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t2.pid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t2.cid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t2.did={} """.format(self.args.get('did')))
        return where_sql_list

    def views(self):
        query_sql = r"""
                            select SQL_CALC_FOUND_ROWS t1.*, t2.isfeestand,t2.sex, t2.age, t2.IDCard, t2.phone, t2.jobtype, t2.nationality, t2.name, t3.name as pro_name, t4.name as com_name, t5.ClassName from tb_salary as t1
                            left join tb_laborinfo as t2 on t1.laborid = t2.id
                            left join tb_project as t3 on t2.ProjectID = t3.id
                            left join tb_company as t4 on t2.CompanyID = t4.id
                            left join tb_class as t5 on t2.ClassID = t5.id
                        """
        if int(self.args.get('id', '0')) == 0:
            if self.args.get('type') == 'company':
                where_sql_list = self.get_company_where()
            elif self.args.get('type') == 'project':
                where_sql_list = self.get_project_where()
            else:
                where_sql_list = self.get_labor_where()
            if self.args.get('time', '') != '':
                timestr = self.args.get('time').replace('T', ' ').replace('Z', '').split('.')[0]
                querytime = datetime.datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=8)
                where_sql_list.append(
                    r""" (t1.year='{}' and t1.month='{}') """.format(querytime.year, querytime.month))
            page = int(self.args.get('page', '1'))
            limit_sql = r""" limit {},{} """.format((page - 1) * 10, 10)
        else:
            where_sql_list = [r""" t1.id ={} """.format(self.args.get('id'))]
            limit_sql = ''
        if self.args.get('month', '') != '':
            query_time = datetime.datetime.strptime(self.args.get('month'), "%Y-%m")
            where_sql_list.append(r""" t1.year = {} and t1.month = {}""".format(query_time.year, query_time.month))
        where_sql = self.get_where_sql(where_sql_list)
        total_query_sql = query_sql + where_sql + limit_sql
        result, total = self._db.query(total_query_sql), self._db.query(self.get_total_row)
        self.success['data'] = result
        self.success['total'] = total[0]['total_row']
        return self.make_response(self.success)


class QueryNextSalary(SalaryBase):

    def __init__(self):
        super(QueryNextSalary, self).__init__()

    def views(self):
        if self.args_is_null('id', 'month'):
            return self.make_response(status_code.CONTENT_IS_NULL)
        query_sql = r"""
                        select SQL_CALC_FOUND_ROWS t1.*, t2.isfeestand,t2.sex, t2.age, t2.IDCard, t2.phone, t2.jobtype, t2.nationality, t2.name, t3.name as pro_name, t4.name as com_name, t5.ClassName from tb_salary as t1
                        left join tb_laborinfo as t2 on t1.laborid = t2.id
                        left join tb_project as t3 on t2.ProjectID = t3.id
                        left join tb_company as t4 on t2.CompanyID = t4.id
                        left join tb_class as t5 on t2.ClassID = t5.id
                                """
        where_sql_list = [r""" t2.id ={} """.format(self.args.get('id'))]
        limit_sql = ''
        if self.args.get('month', '') != '':
            year_month = self.args.get('month').split('-')
            where_sql_list.append(
                r""" (t1.year='{}' and t1.month='{}') """.format(year_month[0], year_month[1]))
        where_sql = self.get_where_sql(where_sql_list)
        total_query_sql = query_sql + where_sql + limit_sql
        result, total = self._db.query(total_query_sql), self._db.query(self.get_total_row)
        self.success['data'] = result
        self.success['total'] = total[0]['total_row']
        return self.make_response(self.success)
