import datetime

from copy import deepcopy

from flask import request, jsonify

from Project.twoMonthPro import getTwoMonth
from utils import status_code
from utils.BaseView import BaseView


class IndexBase(BaseView):

    def __init__(self):
        super(IndexBase, self).__init__()
        self.company_ids = []
        self.project_ids = []

    def administrator(self):
        return self.views()

    # def admin(self):
    #     # company_sql = r"""select t2.ID from tb_project as t1
    #     #                         INNER JOIN tb_company as t2 on t1.Build = t2.id
    #     #                         INNER JOIN tb_company as t3 on t1.Cons = t3.id
    #     #                         where t1.DID in ({})""".format(self.get_session_ids())
    #     # self.company_ids = self.set_ids(company_sql)
    #     # if self.company_ids == []:
    #     #     self.company_ids = [0, ]
    #     if self.get_session_ids() != '':
    #         project_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
    #         self.project_ids = self.set_ids(project_sql)
    #     if self.project_ids == []:
    #         self.project_ids = [0, ]
    #     return self.views()

    def admin(self):
        self.company_ids = self.get_company_ids()
        if self.company_ids == []:
            self.company_ids = [0, ]
        self.project_ids = self.get_project_ids()
        if self.project_ids == []:
            self.project_ids = [0, ]
        return self.views()

    def list_to_str(self, list):
        return [str(x) for x in list]

    def views(self):
        return jsonify(status_code.SUCCESS)


class GetBadRecordInfo(IndexBase):
    """
    首页信息查询
    """

    def __init__(self):
        super(GetBadRecordInfo, self).__init__()
        self.company_ids = []
        self.project_ids = []

    def create_where_sql(self, where_sql_list):
        temp = ''
        if where_sql_list:
            temp += ' where '
            for index, item in enumerate(where_sql_list):
                temp += item
                if index < len(where_sql_list) - 1:
                    temp += ' and '
        temp += ' limit 0,10;'
        return temp

    def company_where(self):
        where_sql_list = []
        where_sql_list.append(r""" HasBadRecord = {} """)
        if self.company_ids:
            where_sql_list.append(r""" ID in ({}) """.format(','.join(self.list_to_str(self.company_ids))))
        if self.args.get('companyname', '') != '':
            where_sql_list.append(r"""  CONCAT(IFNULL(Name,'')) LIKE '%{}%' """.format(self.args.get('companyname')))
        if int(self.args.get('DID', 0)) != 0:
            where_sql_list.append(r""" DistrictID={} """.format(int(self.args.get('DID'))))
        if int(self.args.get('CID', 0)) != 0:
            where_sql_list.append(r""" cityid={} """.format(int(self.args.get('CID'))))
        if int(self.args.get('PID', 0)) != 0:
            where_sql_list.append(r""" ProvinceID={} """.format(int(self.args.get('PID'))))
        return where_sql_list

    def get_company(self):
        query_sql = r"""select id, name, hasbadrecord from tb_company """
        temp_query_sql = query_sql + self.create_where_sql(self.company_where())
        result = self._db.query(temp_query_sql.format(2))
        if not result:
            result = self._db.query(temp_query_sql.format(1))
        return result

    def project_where(self, temp_id):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" t1.ID in ({}) """.format(','.join(self.list_to_str(self.project_ids))))
        if self.args.get('projectname', '') != '':
            where_sql_list.append(
                r"""  CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%'  """.format(self.args.get('projectname')))
        if int(self.args.get('DID', 0)) != 0:
            where_sql_list.append(r""" t1.DID={} """.format(int(self.args.get('DID'))))
        if int(self.args.get('CID', 0)) != 0:
            where_sql_list.append(r""" t1.CID={} """.format(int(self.args.get('CID'))))
        if int(self.args.get('PID', 0)) != 0:
            where_sql_list.append(r""" t1.PID={} """.format(int(self.args.get('PID'))))
        if temp_id:
            where_sql_list.append(r""" t1.Status > 1 """)
            # where_sql_list.append(r""" t3.ProjectID is null """)
        return where_sql_list

    def labor_where(self, temp_id):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" t1.projectID in ({}) """.format(','.join(self.list_to_str(self.project_ids))))
        if self.args.get('laborname', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(self.args.get('laborname')))
        if self.args.get('idcrad', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.IDCard,'')) LIKE '%{}%' """.format(self.args.get('idcrad')))
        if int(self.args.get('DID', 0)) != 0:
            where_sql_list.append(r""" t1.DID={} """.format(int(self.args.get('DID'))))
        if int(self.args.get('CID', 0)) != 0:
            where_sql_list.append(r""" t1.CID={} """.format(int(self.args.get('CID'))))
        if int(self.args.get('PID', 0)) != 0:
            where_sql_list.append(r""" t1.PID={} """.format(int(self.args.get('PID'))))
        if temp_id:
            where_sql_list.append(r""" t1.isbadrecord > 0 """)
        return where_sql_list

    def get_project(self):
        # now_time = datetime.datetime.now()
        query_sql_base = r"""select t1.id,t1.name, t1.status from tb_project as t1"""
        """left join (select id,projectID,Status from tb_wage where year={} and month = {} group by projectID) as t4 on t4.ProjectID = t1.id  
left join (select id,ProjectID from tb_progress where year={} and month ={}  group by projectID) as t3 on t3.ProjectID = t1.id"""
        temp_query_sql = query_sql_base + self.create_where_sql(self.project_where(1))
        result = self._db.query(temp_query_sql)
        if not result:
            temp_query_sql = query_sql_base + self.create_where_sql(self.project_where(0))
            result = self._db.query(temp_query_sql)
        # for item in result:
        #     # print(item)
        #     item['WStatus'] = '工资未发' if item['WStatus'] is None else '工资已发'
        #     item['progressinfo'] = '进度未上传' if item['progressid'] is None else '进度已上传'
        return result

    def get_labor(self):
        # now_time = datetime.datetime.now()
        query_sql = r"""select t1.id,t1.name,t1.isbadrecord,t1.badrecord from tb_laborinfo as t1 """
        """left join (select id, laborid from tb_attendance where year= {} and month = {}  group by laborid) as t2 on t1.id = t2.laborid"""
        temp_query_sql = query_sql + self.create_where_sql(self.labor_where(1))
        result = self._db.query(temp_query_sql)
        if not result:
            temp_query_sql = query_sql + self.create_where_sql(self.labor_where(0))
            result = self._db.query(temp_query_sql)
        # for item in result:
        # item['WStatus'] = '本月工资未发放' if item['WStatus'] is None else '本月工资已发'
        # item['attend'] = '考勤未上传' if item['attend'] is None else '考勤已上传'
        return result

    def get_bank_info(self):
        query_sql = r"""
        select t1.id,t1.name,sum(t2.labors+0) as totalcards, sum(t2.pay+0) as totalpay, count(t2.id) as totalproject from tb_bank as t1
        left join 
            (
                select t1.*,t2.pay  from (
                    select t1.id, t1.bank, t2.labors from tb_project as t1
                    left join (select count(id) as labors, projectid from tb_laborinfo GROUP BY ProjectID) as t2 on t1.id = t2.projectid
                    ) as t1
            
                left join (
                    select t1.id,t1.bank,t2.pay from tb_project as t1
                    left join (select sum(ActualPay+0) as pay, projectid from tb_wage group by ProjectID) as t2 on t1.id = t2.projectid
                ) as t2 on t1.id=t2.id
            ) as t2 on t1.id=t2.bank GROUP BY t1.id ORDER BY totalproject desc limit 0,10;
        """
        result = self._db.query(query_sql)
        for item in result:
            for key in item.keys():
                if item[key] is None or item[key] == '':
                    item[key] = 0
                if key == 'totalcards' and item[key] != None:
                    item[key] = int(item[key])

        return result

    def views(self):
        success = deepcopy(status_code.SUCCESS)
        success['company'] = self.get_company()
        success['project'] = self.get_project()
        success['labor'] = self.get_labor()
        success['bankinfo'] = self.get_bank_info()
        # print(success['labor'])
        return jsonify(success)


class MessageTotal(IndexBase, getTwoMonth):
    """
    消息统计
    """

    def __init__(self):
        super(MessageTotal, self).__init__()
        super(getTwoMonth, self).__init__()
        self.company_ids = []
        self.project_ids = []

    # def admin(self):
    #     company_sql = r"""select t2.ID from tb_project as t1
    #                             INNER JOIN tb_company as t2 on t1.Build = t2.id
    #                             INNER JOIN tb_company as t3 on t1.Cons = t3.id
    #                             where t1.DID in ({})""".format(self.get_session_ids())
    #     self.company_ids = self.set_ids(company_sql)
    #     if self.company_ids == []:
    #         self.company_ids = [0, ]
    #
    #     project_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
    #     self.project_ids = self.set_ids(project_sql)
    #     if self.project_ids == []:
    #         self.project_ids = [0, ]
    #     return self.views()

    def create_where_sql(self, where_sql_list):
        temp = ''
        if where_sql_list:
            temp += ' where '
            for index, item in enumerate(where_sql_list):
                temp += item
                if index < len(where_sql_list) - 1:
                    temp += ' and '
        temp += ' limit 0,3;'
        return temp

    def company_where(self):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" ID in ({}) """.format(','.join(self.list_to_str(self.company_ids))))
        where_sql_list.append(r""" HasBadRecord = 2 """)
        return where_sql_list

    def get_company(self):
        query_sql = r"""select SQL_CALC_FOUND_ROWS id, name, hasbadrecord from tb_company """
        temp_query_sql = query_sql + self.create_where_sql(self.company_where())
        result = self._db.query(temp_query_sql.format(2))
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        # if not result:
        #     result = self._db.query(temp_query_sql.format(0))
        return result, total[0]['total_row']

    def project_where(self):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" t1.ID in ({}) """.format(','.join(self.list_to_str(self.project_ids))))
        where_sql_list.append(r""" t1.Status > 1 """)
        return where_sql_list

    def labor_where(self):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" t1.projectID in ({}) """.format(','.join(self.list_to_str(self.project_ids))))
        where_sql_list.append(r""" t1.isbadrecord > 0 """)
        return where_sql_list

    def get_project(self):
        # now_time = datetime.datetime.now()
        query_sql_base = r"""select SQL_CALC_FOUND_ROWS t1.id,t1.name, t1.status from tb_project as t1"""
        """left join (select id,projectID,Status from tb_wage where year={} and month = {} group by projectID) as t4 on t4.ProjectID = t1.id  
left join (select id,ProjectID from tb_progress where year={} and month ={}  group by projectID) as t3 on t3.ProjectID = t1.id.format(
            now_time.year, now_time.month, now_time.year, now_time.month)"""

        temp_query_sql = query_sql_base + self.create_where_sql(self.project_where())
        result = self._db.query(temp_query_sql)
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        # if result:
        #     for item in result:
        #         # print(item)
        #         item['WStatus'] = '本月工资未发' if item['WStatus'] is None else '本月工资已发'
        #         item['progressinfo'] = '本月进度未上传' if item['progressid'] is None else '本月进度已上传'
        return result, total[0]['total_row']

    def get_labor(self):
        # now_time = datetime.datetime.now()
        query_sql = r"""select SQL_CALC_FOUND_ROWS t1.id,t1.name,t1.isbadrecord,t1.badrecord from tb_laborinfo as t1"""
        temp_query_sql = query_sql + self.create_where_sql(self.labor_where())
        result = self._db.query(temp_query_sql)
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        # if result:
        #     for item in result:
        #         # item['WStatus'] = '本月工资未发放' if item['WStatus'] is None else '本月工资已发'
        #         item['attend'] = '本月考勤未上传' if item['attend'] is None else '本月考勤已上传'
        return result, total[0]['total_row']

    def views(self):
        success = deepcopy(status_code.SUCCESS)
        success['company_list'], com_total = self.get_company()
        success['project_list'], pro_total = self.get_project()
        success['labor_list'], labor_total = self.get_labor()
        success['number_list'] = [com_total, pro_total, labor_total]
        success['not_write_progress'] = len(self.get_uninput_project_ids(self.project_ids))
        return jsonify(success)


class IndexNumberPic(IndexBase):

    def __init__(self):
        super(IndexNumberPic, self).__init__()
        self.company_ids = []
        self.project_ids = []

    # def admin(self):
    #     company_sql = r"""select t2.ID from tb_project as t1
    #                             INNER JOIN tb_company as t2 on t1.Build = t2.id
    #                             INNER JOIN tb_company as t3 on t1.Cons = t3.id
    #                             where t1.DID in ({})""".format(self.get_session_ids())
    #     self.company_ids = self.set_ids(company_sql)
    #     if self.company_ids == []:
    #         self.company_ids = [0, ]
    #
    #     project_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
    #     self.project_ids = self.set_ids(project_sql)
    #     if self.project_ids == []:
    #         self.project_ids = [0, ]
    #     return self.views()

    def ids_to_sql(self, ids):
        return ','.join(ids)

    def create_where_sql(self, where_sql_list):
        temp = ''
        if where_sql_list:
            temp += ' where '
            for index, item in enumerate(where_sql_list):
                temp += item
                if index < len(where_sql_list) - 1:
                    temp += ' and '
        # temp += ' limit 0,3;'
        return temp

    def company_where(self, isbad):
        where_sql_list = []
        if self.company_ids:
            where_sql_list.append(r""" ID in ({}) """.format(','.join(self.list_to_str(self.company_ids))))
        if isbad == 1:
            where_sql_list.append(r""" HasBadRecord = 2 """)
        if isbad == 0:
            where_sql_list.append(r""" HasBadRecord = 1 """)
        return where_sql_list

    def project_where(self, isbad):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" ID in ({}) """.format(','.join(self.list_to_str(self.project_ids))))
        if isbad == 1:
            where_sql_list.append(r""" Status > 1 """)
        if isbad == 0:
            where_sql_list.append(r""" Status<=1 """)

        return where_sql_list

    def labor_where(self, isbad):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" projectid in ({}) """.format(','.join(self.list_to_str(self.project_ids))))
        if isbad == 1:
            where_sql_list.append(r""" Isbadrecord>0 """)
        # if isbad == 0:
        #     where_sql_list.append(r""" Isbadrecord=0 """)
        return where_sql_list

    def get_pie_labor(self):
        total = r"""select count(id) as total from tb_laborinfo """
        query_bad_sql = r"""select count(id) as total from tb_laborinfo """
        query_no_bad_sql = r"""select count(id) as total from tb_laborinfo """
        bad_data = {
            'name': '不良劳工',
            'value': self._db.query(query_bad_sql + self.create_where_sql(self.labor_where(1)))[0]['total']
        }
        data = {
            'name': '正常劳工',
            'value': self._db.query(query_no_bad_sql + self.create_where_sql(self.labor_where(0)))[0]['total']
        }
        return [bad_data, data], self._db.query(total + self.create_where_sql(self.labor_where(2)))[0]['total'], \
               bad_data['value']

    def get_pie_company(self):
        total = r"""select count(id) as total from tb_company"""
        query_bad_sql = r"""select count(id) as total from tb_company"""
        query_no_bad_sql = r"""select count(id) as total from tb_company """
        bad_data = {
            'name': '不良企业',
            'value': self._db.query(query_bad_sql + self.create_where_sql(self.company_where(1)))[0]['total']
        }
        data = {
            'name': '正常企业',
            'value': self._db.query(query_no_bad_sql + self.create_where_sql(self.company_where(0)))[0]['total']
        }
        return [bad_data, data], self._db.query(total + self.create_where_sql(self.company_where(2)))[0]['total'], \
               bad_data['value']

    def get_pie_project(self):
        total = r"""select count(id) as total from tb_project """
        query_bad_sql = r"""select count(id) as total from tb_project """
        query_no_bad_sql = r"""select count(id) as total from tb_project """
        bad_data = {
            'name': '不良项目',
            'value': self._db.query(query_bad_sql + self.create_where_sql(self.project_where(1)))[0]['total']
        }
        data = {
            'name': '正常项目',
            'value': self._db.query(query_no_bad_sql + self.create_where_sql(self.project_where(0)))[0]['total']
        }
        return [bad_data, data], self._db.query(total + self.create_where_sql(self.project_where(2)))[0]['total'], \
               bad_data['value']

    def views(self):
        pie_labor, total_labor, bad_labor = self.get_pie_labor()
        pie_company, total_company, bad_company = self.get_pie_company()
        pie_project, total_project, bad_project = self.get_pie_project()
        success = deepcopy(status_code.SUCCESS)
        success['pie_labor'] = pie_labor
        success['pie_company'] = pie_company
        success['pie_project'] = pie_project
        success['total_labor'] = total_labor
        success['total_company'] = total_company
        success['total_project'] = total_project
        success['bad_company'] = bad_company
        success['bad_project'] = bad_project
        success['bad_labor'] = bad_labor
        return jsonify(success)
