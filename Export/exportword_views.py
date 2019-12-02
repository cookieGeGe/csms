# -*- coding: utf-8 -*-
# @Time : 2019/10/13
# @Author : zhang
# @Site :
# @File : exportword_views.py
# @Software: PyCharm
import datetime
import os
import random
from copy import deepcopy
from json import loads

from APP.settings import static_dir
from Export.exportwordbase import ExportDocxBase

template_base = os.path.join(static_dir, 'export_template')


class ExportWordTest(ExportDocxBase):
    template = os.path.join(template_base, 'test.docx')

    def __init__(self):
        super(ExportWordTest, self).__init__()
        self.export_name = 'test.docx'

    def query_data(self, view):
        """

        :param view:当前视图类
        :return:
        """
        print(view)

    def formatter(self):
        self.data = {
            'title': '测试文档',
            'content': '建工管理软件导出测试文档——随机数{}'.format(random.randint(0, 100)),
            'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


class ExportCompanyWord(ExportDocxBase):
    """
    导出企业模板
    """
    template = os.path.join(template_base, 'export_company.docx')

    def __init__(self):
        super(ExportCompanyWord, self).__init__()
        self.export_name = None

    def formatter_company(self, company):
        if company['Phone'] is not None and company['Phone'] != '':
            company['Phone'] = loads(company['Phone'])
        return company

    def formatter_projects(self, projects):
        projects_list = []
        for project in projects:
            projects_list.append({
                "Name": project['Name'],
                'Status': self.project_bad_list[int(project['Status'])],
                'Address': project['PID'] + project['CID'] + project['DID'] + project['Address']
            })
        return projects_list

    def query_data(self, view):
        company_id = view.args.get('id')
        query_sql = r"""select t1.ID, t1.Address, t1.BadRecord,t1.Description, t1.Legal, t1.License, t1.HasBadRecord,
                        t1.Name, t1.Phone, t1.Type, t1.url, t1.OtherInfo, t2.Name as ProvinceID, t3.Name as CityID, t4.Name as DistrictID, 
                        t1.ProvinceID as province, t1.CityID as city, t1.DistrictID as district from tb_company as t1
                        LEFT JOIN tb_area as t2 on t1.ProvinceID = t2.ID
                        LEFT JOIN tb_area as t3 on t1.CityID = t3.ID
                        LEFT JOIN tb_area as t4 on t1.DistrictID = t4.ID
                        where t1.id = {};""".format(company_id)
        resutl = view._db.query(query_sql)
        all_projects = r"""select t1.ID,t1.Name,t1.Status,t1.Address,t3.Name as PID, t4.Name as CID, t5.Name as DID 
                        from tb_project as t1
                        LEFT JOIN tb_company as t2 on t1.Build = t2.ID or t1.Cons =t2.ID
						LEFT JOIN tb_area as t3 on t1.PID = t3.ID
                        LEFT JOIN tb_area as t4 on t1.CID = t4.ID
                        LEFT JOIN tb_area as t5 on t1.DID = t5.ID
                        where t2.ID = {} or CONCAT(IFNULL(t1.SubCompany,'')) LIKE '%"ID":"{}"%';""".format(company_id,
                                                                                                           company_id)
        resutl_projects = view._db.query(all_projects)
        self.data = {}
        if resutl:
            self.data = self.formatter_company(resutl[0])
        self.data['projects'] = []
        if resutl_projects:
            self.data.update({
                'projects': self.formatter_projects(resutl_projects)
            })

    def formatter(self):
        self.export_name = '{}.docx'.format(self.data.get('Name', 'company'))
        self.data.update(self.export_data)
        if not self.content_is_null('Type', data=self.data):
            self.data['Type'] = self.company_type_list[int(self.data['Type'])]
        if not self.content_is_null('HasBadRecord', data=self.data):
            self.data['HasBadRecord'] = self.company_bad_list[int(self.data['HasBadRecord'])]
        if self.content_is_null('OtherInfo', data=self.data):
            self.data['OtherInfo'] = ''


class ExportProjectWord(ExportDocxBase):
    """
    导出项目信息目录
    """
    template = os.path.join(template_base, 'export_project.docx')

    def __init__(self):
        super(ExportProjectWord, self).__init__()
        self.export_name = None
        self.db = None
        self.args = None

    def get_default_project_info(self):
        query_sql = r"""
        select t1.*,t7.Name as BankName,t2.Name as PIDN,t3.Name as CIDN,t4.Name as DIDN, t5.totallabor
        from tb_project as t1
        LEFT JOIN tb_area as t2 on t1.PID = t2.ID
        LEFT JOIN tb_area as t3 on t1.CID = t3.ID
        LEFT JOIN tb_area as t4 on t1.DID = t4.ID
        left join tb_bank as t7 on t7.id = t1.bank
        left join (select count(id) as totallabor, projectid from tb_laborinfo GROUP BY ProjectID) as t5 on t1.id=t5.ProjectID
        where t1.id={};
        """.format(self.args.get('id'))
        result = self.db.query(query_sql)
        return result[0] if result else {}

    def query_data(self, view):
        self.db = view._db
        self.args = view.args
        self.data = self.get_default_project_info()  # 获取项目基本数据

    def formatter_company_default(self, companyid):
        """
        获取默认企业信息方法
        :param companyid:
        :return:
        """
        result = self.query_company_data(companyid)
        temp = {
            'Name': '',
            'ProvinceID': '',
            'CityID': '',
            'DistrictID': '',
            'Address': '',
            'HasBadRecord': '',
            'Description': ''
        }
        if result:
            company = result[0]
            temp = {
                'Name': company['Name'],
                'ProvinceID': company['ProvinceID'],
                'CityID': company['CityID'],
                'DistrictID': company['DistrictID'],
                'Address': company['Address'],
                'HasBadRecord': self.company_bad_list[int(company['HasBadRecord'])] if not self.content_is_null(
                    'HasBadRecord', data=company
                ) else '',
                'Description': company['Description']
            }
        return temp

    def formatter_manager(self, key, companyid):
        """
        格式化负责人
        :param key:
        :param companyid:
        :return:
        """
        temp_manager = self.formatter_company_default(companyid)
        temp_manager.update({
            key + 'Manager': self.data[key + 'Manager'].replace('&nbsp;', ''),
        })
        return temp_manager

    def formatter_subcompany(self, subcompany):
        subcompany = loads(subcompany)
        temp = []
        for company in subcompany:
            temp_company = self.formatter_company_default(company['ID'])
            temp_company.update({
                'Person': company['Person'].replace('&nbsp;', '')
            })
            temp.append(deepcopy(temp_company))
        return temp

    def formatter_hadstartmonth(self):
        end = datetime.datetime.now()
        year1 = end.year
        year2 = self.data['StartTime'].year
        month1 = end.month
        month2 = self.data['StartTime'].month
        num = (year1 - year2) * 12 + (month1 - month2)
        return num

    def formatter_progress(self):
        query_progress_sql = r"""
        select t1.*, t2.Status as BankStatus from tb_progress as t1
        left join tb_wage as t2 on (t1.year =t2.year and t1.month = t2.month and t1.ProjectID = t2.ProjectID)
        where t1.ProjectID = {};
        """.format(self.data['ID'])
        result = self.db.query(query_progress_sql)
        progress_list = []
        if result:
            for item in result:
                temp = {
                    'year': item['year'],
                    'month': item['month'],
                    'BankStatus': self.bank_status_list[item['BankStatus']] if item['BankStatus'] is not None else '未到',
                    'Content': item['Content'] if item['Content'] is not None else '',
                    'Status': '是' if item['Status'] else '否',
                    'Percent': item['Percent']
                }
                progress_list.append(deepcopy(temp))
        return progress_list

    def formatter(self):
        self.export_name = '{}.docx'.format(self.data.get('Name', 'project'))
        self.data.update(self.export_data)
        self.data['Type'] = self.get_type_or_bad(self.project_type_list, self.data['Type'])
        self.data['HasStartMonth'] = self.formatter_hadstartmonth()
        self.data['PrinPical'] = loads(self.data['PrinPical']) if self.data['PrinPical'] is not None else []
        self.data['Build'] = self.formatter_manager('Owner', self.data['Build'])
        self.data['Cons'] = self.formatter_manager('Cons', self.data['Cons'])
        self.data['Subcompany'] = self.formatter_subcompany(self.data['SubCompany'])
        self.data['ProgressList'] = self.formatter_progress()
        for key in ('StartTime', 'EndTime', 'Duration'):
            # if self.data[key] is not None and self.data[key] != '':
            if isinstance(self.data[key], datetime.datetime):
                self.data[key] = self.data[key].strftime("%Y-%m-%d %H:%M:%S")


class ExportProgressWord(ExportDocxBase):
    template = os.path.join(template_base, 'export_progress.docx')

    def __init__(self):
        super(ExportProgressWord, self).__init__()
        self.export_name = None
        self.db = None
        self.args = None

    def query_data(self, view):
        self.db = view._db
        self.args = view.args
        self.data = self.get_default_progress_data()

    def get_default_progress_data(self):
        query_sql = r"""
                    select t1.*,t2.Name as project_name from tb_progress as t1
                    left join tb_project as t2 on t1.ProjectID = t2.ID
                    where t1.id = {};
                    """.format(self.args.get('id'))
        result = self.db.query(query_sql)
        return result[0] if result else {}

    def query_bank_info(self):
        query_sql = r"""
            select * from tb_wage where projectid={} and month={} and year={};
            """.format(self.args.get('id'), self.data['month'], self.data['year'])
        result = self.db.query(query_sql)
        temp = {
            'RPay': '',
            'ActualPay': '',
            'Diff': '',
            'BankStatus': ''
        }
        if result:
            item = result[0]
            temp = {
                'RPay': item['RPay'],
                'ActualPay': item['ActualPay'],
                'Diff': eval(item['RPay']) - eval(item['ActualPay']),
                'BankStatus': self.bank_status_list[item['Status']]
            }
        return temp

    def formatter_person(self, persons):
        persons = loads(persons)
        person_list = []
        for person in persons:
            query_sql = r"""
            select t1.name, t1.phone, t1.EntryDate as time, t2.ClassName as class from tb_laborinfo as t1
            left join tb_class as t2 on t1.ClassID = t2.id
            where t1.id = {};""".format(person.get('id'))
            result = self.db.query(query_sql)
            if result:
                if result[0]['name'] is None or result[0]['name'] == '':
                    continue
                temp = result[0]
                temp['wage'] = person['wage']
                person_list.append(deepcopy(temp))
        return person_list

    def formatter(self):
        name = self.data.get('project_name', 'project') + '_' + str(
            self.data.get('year', datetime.datetime.now().year)) + '_' + str(
            self.data.get('month', datetime.datetime.now().month))
        self.export_name = '{}.docx'.format(name)
        if not len(self.data.keys()):
            raise Exception('未找到数据')
        self.data.update(self.export_data)
        # self.data['Status'] = '是' if self.data['Status'] else '否'
        self.data['Connect'] = '' if self.data['Connect'] is None else self.data['Connect'].replace('&nbsp;', '')
        self.data['RType'] = self.progress_type_list[self.data['RType']]
        self.data['Bank'] = self.query_bank_info()
        self.data['Difference'] = eval(self.data['TotalSalary']) - eval(self.data['RealIssues'])
        self.data['Person'] = self.formatter_person(self.data['Person'])
        for key in ('Status', 'Contract', 'RealName', 'Attend', 'Lwage', 'LAB', 'PAB', 'LPayCert'):
            if key == 'Status':
                self.data[key] = '是' if self.data[key] else '否'
            else:
                self.data[key] = '有' if self.data[key] else '无'

        for key in ('UploadTime',):
            # if self.data[key] is not None and self.data[key] != '':
            if isinstance(self.data[key], datetime.datetime):
                self.data[key] = self.data[key].strftime("%Y-%m-%d %H:%M:%S")


class ExportLaborWord(ExportDocxBase):
    template = os.path.join(template_base, 'export_labor.docx')

    def __init__(self):
        super(ExportLaborWord, self).__init__()
        self.export_name = None
        self.db = None
        self.args = None

    def query_data(self, view):
        self.db = view._db
        self.args = view.args
        self.data = self.get_labor_default()

    def get_labor_default(self):
        query_sql = r"""select t1.*, t2.ClassName as ClassName, t3.Name as ProjectName, t4.Name as CompanyName, t5.Name as PName, t6.Name as CName, t7.Name as DName, t8.name as SuperiorsName from tb_laborinfo as t1
                        left join tb_class as t2 on t1.ClassID = t2.id
                        left join tb_project as t3 on t1.projectid = t3.id
                        left join tb_company as t4 on t1.CompanyID = t4.id
                        left JOIN tb_area as t5 on t5.ID = t1.PID
                        left JOIN tb_area as t6 on t6.ID = t1.CID
                        left JOIN tb_area as t7 on t7.ID = t1.DID
                        left join tb_laborinfo as t8 on t8.id = t1.Superiors
                        where t1.id = 53;"""
        result = self.db.query(query_sql)
        return result[0] if result else {}

    def formatter(self):
        self.export_name = '{}.docx'.format(self.data.get('Name', 'labor'))
        if not len(self.data.keys()):
            raise Exception('未找到数据')
        self.data.update(self.export_data)
        for key in ('IsPM', 'IsLeader'):
            self.data[key] = '是' if self.data[key] else '否'
        self.data['Isbadrecord'] = self.labor_bad_list[self.data['Isbadrecord']]
        self.data['isFeeStand'] = '合同工' if self.data['isFeeStand'] else '临时工'


class ExportGuaranteeWord(ExportDocxBase):
    template = os.path.join(template_base, 'export_guarantee.docx')

    def __init__(self):
        super(ExportGuaranteeWord, self).__init__()
        self.export_name = None
        self.db = None
        self.args = None

    def query_data(self, view):
        self.db = view._db
        self.args = view.args
        self.data = self.get_default_guarantee()

    def get_default_guarantee(self):
        query_sql = r"""
            select SQL_CALC_FOUND_ROWS t1.*, t4.name as PName,t5.name as CName, t6.name as DName from tb_guarantee as t1
            INNER JOIN tb_area as t4 on t1.PID = t4.id
            INNER JOIN tb_area as t5 on t1.CID = t5.id
            INNER JOIN tb_area as t6 on t1.DID = t6.id
            where t1.id = {};
        """.format(self.args.get('id'))
        result = self.db.query(query_sql)
        return result[0] if result else {}

    def get_all_cguarantee(self):
        result = []
        if not self.content_is_null('Number', data=self.data):
            query_sql = r"""select * from tb_cguarantee where gid={};""".format(self.args.get('id'))
            result = self.db.query(query_sql)
            for item in result:
                for key in item.keys():
                    if key == 'Description':
                        print(key)
                    if item[key] is None:
                        item[key] = ''
        return result

    def formatter(self):
        self.export_name = '{}.docx'.format(self.data.get('Name', 'guarantee'))
        if not len(self.data.keys()):
            raise Exception('未找到数据')
        self.data.update(self.export_data)
        self.data['Cguarantee'] = self.get_all_cguarantee()
        if self.data['Expiretime'] < datetime.datetime.now():
            self.data['isExpire'] = '是'
        else:
            self.data['isExpire'] = '否'

        for key in self.data.keys():
            if self.data[key] is None:
                self.data[key] = ''
        self.data['SignTime'] = self.data['SignTime'].strftime("%Y-%m-%d")
        self.data['Expiretime'] = self.data['Expiretime'].strftime("%Y-%m-%d")
        self.data['Category'] = self.guarantee_type_list[self.data['Category']]
