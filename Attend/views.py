import datetime

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
                laborinfo = self.get_labor_id(item['idcard'])
                # laborinfo = {'id': 1, 'projectid': 2}
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
        query_sql = r"""select SQL_CALC_FOUND_ROWS t1.ID,t1.Name,t1.JobType,t1.IDCard,t1.Avatar,t1.ProjectID,t2.Name as CompanyName,t3.Name as ProjectName,
                t4.Count,t4.year,t4.month,t5.ClassName,t1.CompanyID,t1.Avatar from tb_laborinfo as t1
                left join tb_company as t2 on t2.ID = t1.CompanyID
                left JOIN tb_project as t3 on t3.ID = t1.ProjectID
				left join tb_class as t5 on t5.id = t1.classid
                left JOIN (select laborid,year,month,count(id) as Count from tb_attendance where amin != '' or amout!= '' or pmin != '' or pmout != '' GROUP BY laborid,year,month)
                 as t4 on t4.laborid = t1.id"""
        where_sql = []
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            where_sql.append(r""" t1.ProjectID in ({}) """.format(self.to_sql_where_id()))
        if args.get('CompanyName', '') != '':
            where_sql.append(r"""  CONCAT(IFNULL(t2.Name,'')) LIKE '%{}%' """.format(args.get('CompanyName')))
        if args.get('ProjectName', '') != '':
            where_sql.append(r"""  CONCAT(IFNULL(t3.Name,'')) LIKE '%{}%' """.format(args.get('ProjectName')))
        if args.get('LaborName', '') != '':
            where_sql.append(r"""  CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('LaborName')))
        if int(args.get('Days', 0)) != 0:
            where_sql.append(r""" t4.Count > {} """.format(int(args.get('Days'))))
        if args.get('Month', '') != '':
            query_time = datetime.datetime.strptime(args.get('Month'), "%Y-%m")
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
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        success = deepcopy(status_code.SUCCESS)
        success['Attend'] = result
        success['total'] = total[0]['total_row']
        # print(success['Attend'])
        return jsonify(success)


class QueryAttendInfo(AttendBase):

    def __init__(self):
        super(QueryAttendInfo, self).__init__()

    def views(self):
        args = self.args
        query_sql = r"""select t1.*, t2.Name, t2.IDCard from tb_attendance as t1 left join tb_laborinfo as t2 on t1.laborid = t2.id where t1.laborid={}
                        and t1.year={} and t1.month ={} order by t1.day;""".format(int(args.get('Id')),
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
        success = deepcopy(status_code.SUCCESS)
        success['data'] = temp_data
        return jsonify(success)


class QuerySalary(AttendBase):

    def __init__(self):
        super(QuerySalary, self).__init__()

    def admin(self):
        query_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
        self.ids = self.set_ids(query_sql)
        return self.views()

    def get_info(self, laborid, year, month):
        query_sql = r"""select t1.IDCard, t1.JobType,t1.Name,t1.Feestand, t1.isFeeStand, t4.swipe from tb_laborinfo as t1
                        left JOIN (select laborid,year,month,count(id) as swipe from tb_attendance where year = {} and month = {} and (amin != '' or amout!= '' or pmin != '' or pmout != '') GROUP BY laborid,year,month )
                          as t4 on t4.laborid = t1.id where t1.id={};""".format(
            year, month, laborid)
        # print(query_sql)
        result = self._db.query(query_sql)
        data = {}
        if result:
            data = result[0]
        newdata = {
            "laborid": laborid,
            "status": 0,
            "manual": 0,
            "type": "天",
            "unit": 0,
            "basicwage": 0,
            "overtime": 0,
            "subtotal": 0,
            "reward": 0,
            "deduction": 0,
            "total": 0,
            "id": 0,
            "month": month,
            "year": year,
            "time": str(year) + "-" + str(month)
        }
        data.update(newdata)
        return [data, ]

    def views(self):
        args = self.args
        query_sql = r"""select SQL_CALC_FOUND_ROWS t1.*,t2.IDCard,t2.JobType,t2.Name,t2.FeeStand,t2.isFeeStand from tb_salary as t1
                        left join tb_laborinfo as t2 on t1.laborid = t2.id"""
        where_sql = []
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            where_sql.append(r""" t2.ProjectID in ({}) """.format(self.to_sql_where_id()))
        if int(args.get('ID', 0)) == 0:
            if args.get('CompanyName', '') != '':
                where_sql.append(
                    r"""  CONCAT(IFNULL(t1.companyname,'')) LIKE '%{}%' """.format(args.get('CompanyName')))
            if args.get('ProjectName', '') != '':
                where_sql.append(
                    r"""  CONCAT(IFNULL(t1.projectname,'')) LIKE '%{}%' """.format(args.get('ProjectName')))
            if args.get('LaborName', '') != '':
                where_sql.append(r"""  CONCAT(IFNULL(t2.Name,'')) LIKE '%{}%' """.format(args.get('LaborName')))
        else:
            where_sql.append(r""" t1.laborid = {} """.format(int(args.get('ID'))))
        if args.get('Month', '') != '':
            query_time = datetime.datetime.strptime(args.get('Month'), "%Y-%m")
            where_sql.append(r""" t1.year = {} and t1.month = {}""".format(query_time.year, query_time.month))
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
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        if int(args.get('ID', 0)) != 0 and not result:
            result = self.get_info(int(args.get('ID')), query_time.year, query_time.month)
        success = deepcopy(status_code.SUCCESS)
        success['data'] = result
        success['total'] = total[0]['total_row']
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
        save_date = datetime.datetime.strptime(args.get('time'), "%Y-%m")
        args['year'] = save_date.year
        args['month'] = save_date.month
        query_is_in = r"""select id from tb_salary where laborid={} and year={} and month={}""".format(
            args.get('laborid'), args.get('year'), args.get('month'))

        temp_result = self._db.query(query_is_in)
        if temp_result:
            args['id'] = temp_result[0]['id']
            # print(1)
            # return jsonify(status_code.BANK_INFO_EXISTS)
        if int(args.get('id', 0)) == 0:
            temp_res = '新建成功'
            insert_sql = r"""insert into tb_salary(laborid,status,swipe,manual,type,unit,basicwage,overtime,subtotal,reward,
                deduction, total,projectname,companyname,year,month) value ({laborid},'在场','{swipe}','{manual}',
                '天','{unit}','{basicwage}','{overtime}','{subtotal}','{reward}','{deduction}','{total}',
                '{projectname}','{companyname}','{year}','{month}')""".format(**args)
            self._db.insert(insert_sql)
        else:
            temp_res = '编辑成功'
            update_sql = r"""update tb_salary set laborid={laborid},status='在场', swipe='{swipe}', manual='{manual}',
                type='天', unit='{unit}',basicwage='{basicwage}', overtime='{overtime}', subtotal='{subtotal}',
                reward='{reward}', deduction='{deduction}', total='{total}', projectname='{projectname}', 
                companyname='{companyname}', year='{year}', month='{month}' where id={id};""".format(**args)
            self._db.update(update_sql)
        success = deepcopy(status_code.SUCCESS)
        success['msg'] = temp_res
        return jsonify(success)


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
