# -*- coding: utf-8 -*-
# @Time : 2019/11/25
# @Author : zhang
# @Site :
# @File : attend_view.py
# @Software: PyCharm
import calendar
import datetime

from utils import status_code
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
        self.weekday = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日', ]

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
            select SQL_CALC_FOUND_ROWS t1.*, t2.name,t3.total from (
                select t2.companyid,t2.companyid as id,t1.year,t1.month,t1.day,count(t1.id) as punch from tb_attendance as t1
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
        if self.args.get('time', '') != '':
            timestr = self.args.get('time').replace('T', ' ').replace('Z', '').split('.')[0]
            querytime = datetime.datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=8)
            where_sql_list.append(
                r""" (t1.year='{}' and t1.month='{}') """.format(querytime.year, querytime.month))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            where_sql += ' and '.join(where_sql_list)
        total_query_sql = query_sql + where_sql + self.get_now_limit()
        result = self._db.query(total_query_sql)
        total = self._db.query(self.get_total_row)
        for item in result:
            temp = calendar.weekday(int(item['year']), int(item['month']), int(item['day']))
            item['info'] = self.weekday[temp]
        self.success['date'] = self.formatter_result(result)
        self.success['total'] = total[0]['total_row']
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
            select SQL_CALC_FOUND_ROWS t1.*, t2.name,t3.total from (select projectid,projectid as id,year,month,day,count(id) as punch from tb_attendance where amin != '' or amout!= '' or pmin != '' or pmout != '' GROUP BY projectid,year,month,day order by year desc,month desc, day desc) as t1
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
        if self.args.get('time', '') != '':
            timestr = self.args.get('time').replace('T', ' ').replace('Z', '').split('.')[0]
            querytime = datetime.datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S') + datetime.timedelta(hours=8)
            where_sql_list.append(
                r""" (t1.year='{}' and t1.month='{}') """.format(querytime.year, querytime.month))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            where_sql += ' and '.join(where_sql_list)
        total_query_sql = query_sql + where_sql + self.get_now_limit()
        result = self._db.query(total_query_sql)
        total = self._db.query(self.get_total_row)
        for item in result:
            temp = calendar.weekday(int(item['year']), int(item['month']), int(item['day']))
            item['info'] = self.weekday[temp]
        self.success['date'] = self.formatter_result(result)
        self.success['total'] = total[0]['total_row']
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
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t1.pid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t1.cid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t1.did={} """.format(self.args.get('did')))
        if self.args.get('month', '') != '':
            query_time = datetime.datetime.strptime(self.args.get('month'), "%Y-%m")
            where_sql_list.append(r""" t4.year = {} and t4.month = {}""".format(query_time.year, query_time.month))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            where_sql += ' and '.join(where_sql_list)
        total_query_sql = query_sql + where_sql + " order by id desc,year desc, month desc " + self.get_now_limit()
        result = self._db.query(total_query_sql)
        total = self._db.query(self.get_total_row)
        for item in result:
            item['date'] = '-'.join([
                str(item['year']), str(item['month'])
            ])
            item['unpunch'] = calendar.monthrange(int(item['year']), int(item['month']))[1]
            # temp = calendar.weekday(int(item['year']), int(item['month']), int(item['day']))
            # item['info'] = self.weekday[temp]
        self.success['data'] = result
        self.success['total'] = total[0]['total_row']
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

    def query_labor_info(self, args):
        query_sql = r"""
                    select SQL_CALC_FOUND_ROWS t1.ID,t1.Name,t1.JobType,t1.IDCard,t1.ProjectID,t2.Name as CompanyName,t3.Name as ProjectName,
                    t4.punch,t4.year,t4.month,t1.CompanyID,t1.age, t1.sex, t1.Nationality, t1.phone, t5.classname from tb_laborinfo as t1
                    left join tb_company as t2 on t2.ID = t1.CompanyID
                    left JOIN tb_project as t3 on t3.ID = t1.ProjectID
                    left join tb_class as t5 on t5.id = t1.classid
                    right JOIN (select laborid,year,month,count(id) as punch from tb_attendance where amin != '' or amout!= '' or pmin != '' or pmout != '' GROUP BY laborid,year,month)
                    as t4 on t4.laborid = t1.id 
                    where t1.id = {} and  t4.year = '{}' and t4.month = '{}'
                """.format(int(args.get('id')),
                           args.get('year'),
                           args.get('month'))
        result = self._db.query(query_sql)
        for item in result:
            item['unpunch'] = calendar.monthrange(int(item['year']), int(item['month']))[1]
        return result

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
        self.success['labor'] = self.query_labor_info(args)
        return self.make_response(self.success)


class QueryProComInfo(AttendBase):

    def __init__(self):
        super(QueryProComInfo, self).__init__()

    def get_labors_sql(self):
        query_sql = r"""
            select SQL_CALC_FOUND_ROWS t1.ID,t1.Name,t1.JobType,t1.IDCard,t1.ProjectID,t2.Name as CompanyName,t3.Name as ProjectName,
                    t1.CompanyID,t1.age, t1.sex, t1.Nationality, t1.phone, t5.classname from tb_laborinfo as t1
                    left join tb_company as t2 on t2.ID = t1.CompanyID
                    left JOIN tb_project as t3 on t3.ID = t1.ProjectID
                    left join tb_class as t5 on t5.id = t1.classid
        """
        where_sql_list = []
        if self.args.get('type') == 'project':
            where_sql_list.append(r""" t3.id ='{}' """.format(self.args.get('id')))
        else:
            where_sql_list.append(r""" t2.id ='{}' """.format(self.args.get('id')))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            where_sql += ','.join(where_sql_list)
        result = self._db.query(query_sql + where_sql)
        labors_ids = []
        for item in result:
            labors_ids.append(str(item['ID']))
        return result, labors_ids

    def get_attend_labors_ids(self, query_labors_ids: list):
        year, month, day = self.args.get('date').split('-')
        query_sql = r"""select laborid as id from tb_attendance where laborid in ({})
         and year='{}' and month='{}' and day='{}';""".format(
            ','.join(query_labors_ids),
            year, month, day
        )
        result = self._db.query(query_sql)
        labor_ids = []
        for item in result:
            labor_ids.append(item['id'])
        return labor_ids

    def views(self):
        if self.args_is_null('type', 'id', 'date'):
            return self.make_response(status_code.CONTENT_IS_NULL)
        labors, labor_ids = self.get_labors_sql()
        attend_labors = self.get_attend_labors_ids(labor_ids)
        for labor in labors:
            labor['attend'] = 0
            if labor['ID'] in attend_labors:
                labor['attend'] = 1
        self.success['info'] = labors
        normal = len(attend_labors)
        total = len(labors)
        self.success['normal'] = normal
        self.success['total'] = total
        self.success['abnormal'] = total - normal
        self.success['currentrate'] = int(normal / total * 100)
        return self.make_response(self.success)
