# -*- coding: utf-8 -*-
# @Time : 2019/10/13
# @Author : zhang
# @Site :
# @File : exportword_views.py
# @Software: PyCharm
import datetime
import os
import random
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
    template = os.path.join(template_base, 'export_company.docx')

    def __init__(self):
        super(ExportCompanyWord, self).__init__()
        self.export_name = None
        self.company_type_list = [
            '施工企业', '监理单位', '勘察设计', '劳务公司', '房地产开发', '政府及事业单位', '其他业主单位', '其他'
        ]
        self.bad_list = ['', '正常', '风险', '黑名单']
        self.project_list = ['正常', '常态监管', '重点', '严重']

    def formatter_company(self, company):
        if company['Phone'] is not None and company['Phone'] != '':
            company['Phone'] = loads(company['Phone'])
        return company

    def formatter_projects(self, projects):
        projects_list = []
        for project in projects:
            projects_list.append({
                "Name": project['Name'],
                'Status': self.project_list[int(project['Status'])],
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
        if not self.content_is_null('Type'):
            self.data['Type'] = self.company_type_list[int(self.data['Type'])]
        if not self.content_is_null('HasBadRecord'):
            self.data['HasBadRecord'] = self.bad_list[int(self.data['HasBadRecord'])]

