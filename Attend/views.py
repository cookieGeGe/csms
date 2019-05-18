from copy import deepcopy

from flask import jsonify, request

from utils import status_code
from utils.BaseView import BaseView

from utils.ImportTemp import Data_Excel, TempColnames
from utils.pulic_utils import str_to_datetime, str_to_date
from utils.status_code import TEMPLATE_ERROR


class AttendBase(BaseView):

    def __init__(self):
        super(AttendBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        pass


class ImportAttend(AttendBase):

    def __init__(self):
        super(ImportAttend, self).__init__()

    def get_labor_id(self, idcard):
        query_sql = r"""select id,projectid from tb_laborinfo where idcard={}""".format(idcard)
        result = self._db.query(query_sql)
        temp = None
        if result:
            temp = result[0]
        return temp

    def views(self):
        attend_file = request.files.get('file', '')
        error_info = []
        if attend_file != '':
            f = attend_file.read()  # 文件内容
            f_name = attend_file.filename.split('.')[-1]
            if f_name not in ('xlsx', 'csv', 'xls'):
                return jsonify(TEMPLATE_ERROR)
            excel = Data_Excel(f, TempColnames.ATTEND)
            excel_data = excel.excel_data()
            for item in excel_data:
                # laborinfo = self.get_labor_id(item['idcard'])
                laborinfo = {'id': 1, 'projectid': 2}
                if laborinfo is not None:
                    insert_sql = r"""insert into tb_attendance(laborid, projectid, amin,amout,pmin,pmout, year,month,day) value 
                                    ({},{},'{}','{}','{}','{}','{}','{}','{}');""".format(laborinfo['id'],
                                                                                          laborinfo['projectid'],
                                                                                          item['amin'],
                                                                                          item['amout'],
                                                                                          item['pmin'],
                                                                                          item['pmout'],
                                                                                          item['atime'].year,
                                                                                          item['atime'].month,
                                                                                          item['atime'].day, )
                    self._db.insert(insert_sql)
                else:
                    error_info.append('{}-{}'.format(item['name'], item['idcard']))
        success = deepcopy(status_code.SUCCESS)
        success['error'] = error_info
        return jsonify(success)


class QueryAttend(AttendBase):

    def __init__(self):
        super(QueryAttend, self).__init__()

    def admin(self):
        query_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
        self.ids = self.set_ids(query_sql)
        return self.views()

    def views(self):
        args = self.args
        query_sql = r"""select t1.ID,t1.Name,t1.JobType,t1.IDCard,t1.ProjectID,t2.Name as CompanyName,t3.Name as ProjectName,
                t4.Count,t4.year,t4.month from tb_laborinfo as t1
                left join tb_company as t2 on t2.ID = t1.CompanyID
                left JOIN tb_project as t3 on t3.ID = t1.ProjectID
                left JOIN (select laborid,year,month,count(id) as Count from tb_attendance GROUP BY laborid,year,month )
                 as t4 on t4.laborid = t1.id"""
        where_sql = []
        if self.ids:
            where_sql.append(r""" t1.ProjectID in ({}) """.format(self.to_sql_where_id()))
        if args.get('CompanyName', '') != '':
            where_sql.append(r"""  CONCAT(IFNULL(t2.Name,'')) LIKE '%{}%' """.format(args.get('CompanyName')))
        if args.get('ProjectName', '') != '':
            where_sql.append(r"""  CONCAT(IFNULL(t3.Name,'')) LIKE '%{}%' """.format(args.get('ProjectName')))
        if args.get('LaborName', '') != '':
            where_sql.append(r"""  CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('LaborName')))
        if args.get('Month', '') != '':
            query_time = str_to_datetime(args.get('Month'))
            where_sql.append(r""" t4.year = {} and t4.month = {}""".format(query_time.year, query_time.month))
        temp = ''
        if where_sql:
            temp = ' where '
            for index, i in enumerate(where_sql):
                temp += i
                if index < len(where_sql) - 1:
                    temp += 'and'
        page = int(args.get('Page', 1))
        psize = int(args.get('PageSize', 10))
        limit_sql = r""" limit {},{};""".format((page - 1) * psize, psize)
        query_sql_main = query_sql + " " + temp + limit_sql
        result = self._db.query(query_sql_main)
        success = deepcopy(status_code.SUCCESS)
        success['Attend'] = result
        return jsonify(success)


class QueryAttendInfo(AttendBase):

    def __init__(self):
        super(QueryAttendInfo, self).__init__()

    def views(self):
        args = self.args
        query_sql = r"""select * from tb_attendance where laborid={laborid} and projectid ={projectid}
                        and year={year} and month ={month} order by day;""".format(**args)
        result = self._db.query(query_sql)
        temp_data = []
        for item in result:
            item['date'] = '{}-{}-{}'.format(item['year'], item['month'], item['day'])
            is_miss = False
            for i in ('amin', 'amout', 'pmin', 'pmout'):
                if isinstance(item[i], str):
                    item[i] = ''
                    is_miss = True
                else:
                    item[i] = item[i].strftime("%H:%M:%S")
            item['miss'] = '缺考' if is_miss else '无缺考'
            temp_data.append(item)
        success = deepcopy(status_code.SUCCESS)
        success['Attend_info'] = temp_data
        return jsonify(success)


class QuerySalary(AttendBase):

    def __init__(self):
        super(QuerySalary, self).__init__()

    def admin(self):
        query_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
        self.ids = self.set_ids(query_sql)
        return self.views()

    def views(self):
        args = self.args
        query_sql = r"""select t1.*,t2.IDCard,t2.JobType,t2.Name from tb_salary as t1
                        left join tb_laborinfo as t2 on t1.laborid = t2.id"""
        where_sql = []
        if self.ids:
            where_sql.append(r""" t2.ProjectID in ({}) """.format(self.to_sql_where_id()))
        if args.get('CompanyName', '') != '':
            where_sql.append(r"""  CONCAT(IFNULL(t1.companyname,'')) LIKE '%{}%' """.format(args.get('CompanyName')))
        if args.get('ProjectName', '') != '':
            where_sql.append(r"""  CONCAT(IFNULL(t1.projectname,'')) LIKE '%{}%' """.format(args.get('ProjectName')))
        if args.get('LaborName', '') != '':
            where_sql.append(r"""  CONCAT(IFNULL(t2.Name,'')) LIKE '%{}%' """.format(args.get('LaborName')))
        if args.get('Month', '') != '':
            query_time = str_to_date(args.get('Month'))
            where_sql.append(r""" t1.year = {} and t2.month = {}""".format(query_time.year, query_time.month))
        temp = ''
        if where_sql:
            temp = ' where '
            for index, i in enumerate(where_sql):
                temp += i
                if index < len(where_sql) - 1:
                    temp += 'and'
        page = int(args.get('Page', 1))
        psize = int(args.get('PageSize', 10))
        limit_sql = r""" limit {},{};""".format((page - 1) * psize, psize)
        query_sql_main = query_sql + " " + temp + limit_sql
        result = self._db.query(query_sql_main)
        success = deepcopy(status_code.SUCCESS)
        success['Salary'] = result
        return jsonify(success)


class ADDSalary(AttendBase):

    def __init__(self):
        super(ADDSalary, self).__init__()

    def views(self):
        args = self.args
        query_sql = r"""select t2.Name as projectname, t3.Name as companyname from tb_laborinfo as t1
                        left join tb_project as t2 on t1.ProjectID=t2.ID
                        LEFT JOIN tb_company as t3 on t1.CompanyID=t3.ID
                        where t1.ID ={}""".format(args.get('laborid'))
        result = self._db.query(query_sql)[0]
        args['companyname'] = result['companyname']
        args['projectname'] = result['projectname']
        save_date = str_to_date(args.get('time'))
        args['year'] = save_date.year
        args['month'] = save_date.month
        if int(args.get('is_create', 1)):
            insert_sql = r"""insert into tb_salary(laborid,status,swipe,manual,type,unit,basicwage,overtime,subtotal,reward,
                deduction, total,projectname,companyname,year,month) value ({laborid},'{status}','{swipe}','{manual}',
                '{type}','{unit}','{basicwage}','{overtime}','{subtotal}','{reward}','{deduction}','{total}',
                '{projectname}','{companyname}','{year}','{month}')""".format(**args)
            self._db.insert(insert_sql)
        else:
            update_sql = r"""update tb_salary set laborid={laborid},status='{status}', swipe='{swipe}', manual='{manual}',
                type='{type}', unit='{unit}',basicwage='{basicwage}', overtime='{overtime}', subtotal='{subtotal}',
                reward='{reward}', deduction='{deduction}', total='{total}', projectname='{projectname}', 
                companyname='{companyname}', year='{year}', month='{month}' where id={id};""".format(**args)
            self._db.update(update_sql)
        return jsonify(status_code.SUCCESS)


class GetOneSalary(AttendBase):

    def __init__(self):
        super(GetOneSalary, self).__init__()

    def views(self):
        args = self.args
        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select t1.*, t2.ProjectID, t2.CompanyID from tb_salary as t1
                        left join tb_laborinfo as t2 on t1.laborid = t2.id where t1.id ={};""".format(args.get('ID'))
        result = self._db.query(query_sql)
        temp = {}
        if result:
            temp = result[0]
        success = deepcopy(status_code.SUCCESS)
        success['salary'] = temp
        return jsonify(success)
