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
        temp = {}
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

