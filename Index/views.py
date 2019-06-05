import datetime

from copy import deepcopy

from flask import request, jsonify

from utils import status_code
from utils.BaseView import BaseView


class IndexBase(BaseView):

    def __init__(self):
        super(IndexBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

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

    def admin(self):
        company_sql = r"""select t2.ID from tb_project as t1
                                INNER JOIN tb_company as t2 on t1.Build = t2.id
                                INNER JOIN tb_company as t3 on t1.Cons = t3.id
                                where t1.DID in ({})""".format(self.get_session_ids())
        self.company_ids = self.set_ids(company_sql)
        if self.company_ids == []:
            self.company_ids = [0, ]

        project_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
        self.project_ids = self.set_ids(project_sql)
        if self.project_ids == []:
            self.project_ids = [0, ]
        return self.views()

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
            where_sql_list.append(r""" ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('companyname', '') != '':
            where_sql_list.append(r"""  CONCAT(IFNULL(Name,'')) LIKE '%{}%' """.format(self.args.get('companyname')))
        return where_sql_list

    def get_company(self):
        query_sql = r"""select id, name, hasbadrecord, badrecord from tb_company """
        temp_query_sql = query_sql + self.create_where_sql(self.company_where())
        result = self._db.query(temp_query_sql.format(1))
        if not result:
            result = self._db.query(temp_query_sql.format(0))
        return result

    def project_where(self, temp_id):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('projectname', '') != '':
            where_sql_list.append(
                r"""  CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%'  """.format(self.args.get('projectname')))
        if temp_id:
            where_sql_list.append(r""" (t4.Status is null or t1.Status > 1) """)
            where_sql_list.append(r""" t3.ProjectID is null """)
        return where_sql_list

    def labor_where(self, temp_id):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('laborname', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(self.args.get('laborname')))
        if temp_id:
            where_sql_list.append(r""" t2.laborid is null """)
        return where_sql_list

    def get_project(self):
        now_time = datetime.datetime.now()
        query_sql_base = r"""select t1.id,t1.name, t4.Status as WStatus, t3.id as progressid from tb_project as t1
left join (select id,projectID,Status from tb_wage where year={} and month = {} group by projectID) as t4 on t4.ProjectID = t1.id  
left join (select id,ProjectID from tb_progress where year={} and month ={}  group by projectID) as t3 on t3.ProjectID = t1.id""".format(
            now_time.year, now_time.month, now_time.year, now_time.month)
        temp_query_sql = query_sql_base + self.create_where_sql(self.project_where(1))
        result = self._db.query(temp_query_sql)
        if not result:
            temp_query_sql = query_sql_base + self.create_where_sql(self.project_where(0))
            result = self._db.query(temp_query_sql)
        for item in result:
            # print(item)
            item['WStatus'] = '本月工资未发' if item['WStatus'] is None else '本月工资已发'
            item['progressinfo'] = '本月进度未上传' if item['progressid'] is None else '本月进度已上传'
        return result

    def get_labor(self):
        now_time = datetime.datetime.now()
        query_sql = r"""select t1.id,t1.name,t1.isbadrecord,t1.badrecord,t2.id as attend from tb_laborinfo as t1
    left join (select id, laborid from tb_attendance where year= {} and month = {}  group by laborid) as t2 on t1.id = t2.laborid""".format(
            now_time.year, now_time.month)
        temp_query_sql = query_sql + self.create_where_sql(self.labor_where(1))
        result = self._db.query(temp_query_sql)
        if not result:
            temp_query_sql = query_sql + self.create_where_sql(self.labor_where(0))
            result = self._db.query(temp_query_sql)
        for item in result:
            # item['WStatus'] = '本月工资未发放' if item['WStatus'] is None else '本月工资已发'
            item['attend'] = '本月考勤未上传' if item['attend'] is None else '本月考勤已上传'
        return result

    def views(self):
        success = deepcopy(status_code.SUCCESS)
        success['company'] = self.get_company()
        success['project'] = self.get_project()
        success['labor'] = self.get_labor()
        return jsonify(success)


class MessageTotal(IndexBase):
    """
    消息统计
    """

    def __init__(self):
        super(MessageTotal, self).__init__()
        self.company_ids = []
        self.project_ids = []

    def admin(self):
        company_sql = r"""select t2.ID from tb_project as t1
                                INNER JOIN tb_company as t2 on t1.Build = t2.id
                                INNER JOIN tb_company as t3 on t1.Cons = t3.id
                                where t1.DID in ({})""".format(self.get_session_ids())
        self.company_ids = self.set_ids(company_sql)
        if self.company_ids == []:
            self.company_ids = [0, ]

        project_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
        self.project_ids = self.set_ids(project_sql)
        if self.project_ids == []:
            self.project_ids = [0, ]
        return self.views()

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
        where_sql_list.append(r""" HasBadRecord = {} """)
        return where_sql_list

    def get_company(self):
        query_sql = r"""select SQL_CALC_FOUND_ROWS id, name, hasbadrecord, badrecord from tb_company """
        temp_query_sql = query_sql + self.create_where_sql(self.company_where())
        result = self._db.query(temp_query_sql.format(1))
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        # if not result:
        #     result = self._db.query(temp_query_sql.format(0))
        return result, total[0]['total_row']

    def project_where(self):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))

        return where_sql_list

    def labor_where(self):
        where_sql_list = []
        if self.project_ids:
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        return where_sql_list

    def get_project(self):
        now_time = datetime.datetime.now()
        query_sql_base = r"""select SQL_CALC_FOUND_ROWS t1.id,t1.name, t4.Status as WStatus, t3.id as progressid from tb_project as t1
left join (select id,projectID,Status from tb_wage where year={} and month = {} group by projectID) as t4 on t4.ProjectID = t1.id  
left join (select id,ProjectID from tb_progress where year={} and month ={}  group by projectID) as t3 on t3.ProjectID = t1.id""".format(
            now_time.year, now_time.month, now_time.year, now_time.month)
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
        now_time = datetime.datetime.now()
        query_sql = r"""select SQL_CALC_FOUND_ROWS t1.id,t1.name,t1.isbadrecord,t1.badrecord,t2.id as attend from tb_laborinfo as t1
    left join (select id, laborid from tb_attendance where year= {} and month = {}  group by laborid) as t2 on t1.id = t2.laborid""".format(
            now_time.year, now_time.month)
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
        return jsonify(success)
