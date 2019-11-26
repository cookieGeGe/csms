# -*- coding: utf-8 -*-
# @Time : 2019/11/25
# @Author : zhang
# @Site :
# @File : attend_view.py
# @Software: PyCharm
import calendar
import datetime

from utils.BaseView import BaseView


class AttendBase(BaseView):

    def __init__(self):
        super(AttendBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        pass


class QueryAttend(AttendBase):

    def __init__(self):
        super(QueryAttend, self).__init__()

    def admin(self):
        if self.args.get('type', 'company') == 'company':
            self.ids = self.get_company_ids()
        elif self.args.get('type', 'project') == 'project':
            self.ids = self.get_project_ids()
        else:
            self.ids = self.get_labor_ids()
        return self.views()


    def query_company(self):
        query_sql = r"""
            select t1.*, t2.name,t3.total from (
                select t2.companyid,t1.year,t1.month,t1.day,count(t1.id) as punch from tb_attendance as t1
                left join tb_laborinfo as t2 on t1.laborid = t2.id
                where t1.amin != '' or t1.amout!= '' or t1.pmin != '' or t1.pmout != '' GROUP BY companyid,year,month,day order by year desc,month desc, day desc
                ) as t1
            left join tb_company as t2 on t1.companyid = t2.id
            left join (select companyid,count(id) as total from tb_laborinfo group by companyid) as t3 on t1.companyid = t3.companyid
                """
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t2.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t2.name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t2.provinceid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t2.cityid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t2.districtid={} """.format(self.args.get('did')))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            where_sql += ' and '.join(where_sql_list)
        total_query_sql = query_sql + where_sql + self.get_now_limit()
        result = self._db.query(total_query_sql)
        self.success['date'] = self.formatter_result(result)
        return self.success

    def get_now_limit(self):
        page = int(self.args.get('page', '1'))
        limit_sql = r""" limit {},{} """.format((page - 1) * 10, 10)
        return limit_sql

    def formatter_result(self, result):
        for item in result:
            item['date'] = '-'.join([
                str(item['year']), str(item['month']), str(item['day'])
            ])
            item['unpunch'] = item['total'] - item['punch']
        return result

    def query_project(self):
        query_sql = r"""
            select t1.*, t2.name,t3.total from (select projectid,year,month,day,count(id) as punch from tb_attendance where amin != '' or amout!= '' or pmin != '' or pmout != '' GROUP BY projectid,year,month,day order by year desc,month desc, day desc) as t1
            left join tb_project as t2 on t1.projectid = t2.id
            left join (select projectid,count(id) as total from tb_laborinfo group by projectid) as t3 on t1.projectid = t3.projectid
        """
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t2.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t2.name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t2.pid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t2.cid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t2.did={} """.format(self.args.get('did')))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            where_sql += ' and '.join(where_sql_list)
        total_query_sql = query_sql + where_sql + self.get_now_limit()
        result = self._db.query(total_query_sql)
        self.success['date'] = self.formatter_result(result)
        return self.success

    def query_labor(self):
        query_sql = r"""
            select SQL_CALC_FOUND_ROWS t1.ID,t1.Name,t1.JobType,t1.IDCard,t1.ProjectID,t2.Name as CompanyName,t3.Name as ProjectName,
            t4.punch,t4.year,t4.month,t1.CompanyID,t1.age, t1.sex, t1.Nationality, t1.phone, t5.classname from tb_laborinfo as t1
            left join tb_company as t2 on t2.ID = t1.CompanyID
            left JOIN tb_project as t3 on t3.ID = t1.ProjectID
            left join tb_class as t5 on t5.id = t1.classid
            right JOIN (select laborid,year,month,count(id) as punch from tb_attendance where amin != '' or amout!= '' or pmin != '' or pmout != '' GROUP BY laborid,year,month)
            as t4 on t4.laborid = t1.id 
        """
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t2.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(
                r""" CONCAT(IFNULL(t2.name,''), IFNULL(t3.name,''), IFNULL(t1.name,'')) LIKE '%{}%' """.format(
                    self.args.get('name')))
        if self.args.get('days', '') != '' and int(self.args.get('days', 0)) != 0:
            where_sql_list.append(r""" t4.Count > {} """.format(int(self.args.get('days'))))
        if self.args.get('month', '') != '':
            query_time = datetime.datetime.strptime(self.args.get('month'), "%Y-%m")
            where_sql_list.append(r""" t4.year = {} and t4.month = {}""".format(query_time.year, query_time.month))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            where_sql += ' and '.join(where_sql_list)
        total_query_sql = query_sql + where_sql + " order by id desc,year desc, month desc " + self.get_now_limit()
        result = self._db.query(total_query_sql)
        for item in result:
            item['date'] = '-'.join([
                str(item['year']), str(item['month'])
            ])
            item['unpunch'] = calendar.monthrange(int(item['year']), int(item['month']))[1]
        self.success['data'] = result
        return self.success

    def views(self):
        if self.args.get('type', 'company') == 'company':
            success = self.query_company()
        elif self.args.get('type', 'project') == 'project':
            success = self.query_project()
        else:
            success = self.query_labor()
        return self.make_response(success)


class QueryAttendLaborInfo(AttendBase):

    def __init__(self):
        super(QueryAttendLaborInfo, self).__init__()

    def views(self):
        args = self.args
        query_sql = r"""select t1.*, t2.Name, t2.IDCard from tb_attendance as t1 left join tb_laborinfo as t2 on t1.laborid = t2.id where t1.laborid={}
                                and t1.year={} and t1.month ={} order by t1.day;""".format(int(args.get('id')),
                                                                                           args.get('year'),
                                                                                           args.get('month'))
        result = self._db.query(query_sql)
        temp_data = []
        for item in result:
            item['date'] = '{}-{}-{}'.format(item['year'], item['month'], item['day'])
            is_miss = False
            for i in ('amin', 'amout', 'pmin', 'pmout'):
                if item[i] is None or item[i] == '':
                    item[i] = ''
                    is_miss = True
                else:
                    if isinstance(item[i], str):
                        item[i] = item[i][-8:]
                    else:
                        item[i] = item[i].strftime("%H:%M:%S")
            item['miss'] = '缺考' if is_miss else '无缺考'
            temp_data.append(item)
        self.success['data'] = temp_data
        return self.make_response(self.success)
