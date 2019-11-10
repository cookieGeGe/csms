# -*- coding: utf-8 -*-
# @Time : 2019/10/13
# @Author : zhang
# @Site :
# @File : exportexcel_views.py
# @Software: PyCharm
import random
from copy import deepcopy

from Export.exportexcelbase import ExportExcelBase


class ExportExcelTest(ExportExcelBase):
    header = ['第一列', '第二列', '第三列', '第四列', '第五列', '第六列']

    def __init__(self):
        super(ExportExcelTest, self).__init__()
        self.export_name = 'test.xlsx'

    def query_data(self, data):
        print('excel test view:', data)

    def formatter(self):
        self.data = [['测试', random.randint(0, 100), 'abc', '', random.random() * 100]]


class ExportExcelCompany(ExportExcelBase):
    header = ['企业名称', '联系方式', '企业类型', '企业状态', '企业负责人', '省', '市', '区', '办公地址', '备注', '其他信息']
    header_Name = ['Name', 'Phone', 'Type', 'HasBadRecord', 'Legal',
                   'ProName', 'CityName', 'DisName', 'Description', 'OtherInfo']

    def __init__(self):
        super(ExportExcelCompany, self).__init__()
        self.export_name = 'company.xlsx'
        self.temp_data = None
        self.company_type = ['施工企业', '监理单位', '勘察设计', '劳务公司', '房地产开发', '政府及事业单位', '其他业主单位', '其他']
        self.badrecord_list = ['正常', '风险', '黑名单']

    def formatter_type(self, com_type):
        if isinstance(type, str):
            com_type = int(com_type)
        return self.company_type[com_type]

    def formatter_badrecord(self, bad):
        if isinstance(bad, str):
            bad = int(bad)
        return self.badrecord_list[bad]

    def formatter_Phone(self, phone):
        phone_list = []
        for item in phone:
            temp = []
            for key in item.keys():
                temp.append(item.get(key, ''))
            phone_list.append('-'.join(temp))
        return ';'.join(phone_list)

    def query_data(self, data):
        self.temp_data = data

    def formatter_key(self, item, key):
        if key == 'Type':
            return self.formatter_type(item[key])
        elif key == 'HasBadRecord':
            return self.formatter_badrecord(item[key])
        elif key == 'Phone':
            return self.formatter_Phone(item[key])
        else:
            value = item.get(key, '')
            if value is not None and isinstance(value, str):
                return value.replace('&nbsp;', ' ')
            return value

    def formatter(self):
        self.data = []
        for item in self.temp_data:
            temp = []
            for key in self.header_Name:
                temp.append(self.formatter_key(item, key))
            self.data.append(deepcopy(temp))


class ExportExcelProject(ExportExcelBase):
    header = ['项目名称', '项目类型', '项目状态', '建设方', '业主负责人', '施工方', '施工负责人', '担保金额（元）',
              '工资发放比例（%）', '参与人数', '开始时间', '结束时间', '地址']
    header_Name = ['Name', 'Type', 'Status', 'BuildName', 'OwnerManager', 'ConsName', 'ConsManager',
                   'GAmount', 'WagePercent', 'Persons', 'StartTime', 'EndTime', 'Address']

    def __init__(self):
        super(ExportExcelProject, self).__init__()
        self.export_name = 'project.xlsx'
        self.temp_data = None
        self.project_type = ['政府投资', '民营开发', '国企分包', '其他']
        self.project_status = ['正常', '常态监管', '重点', '严重']

    def query_data(self, data):
        self.temp_data = data

    def formatter_type(self, pro_type):
        if isinstance(pro_type, str):
            pro_type = int(pro_type)
        return self.project_type[pro_type]

    def formatter_status(self, status):
        if isinstance(status, str):
            status = int(status)
        return self.project_type[status]

    def formatter_key(self, item, key):
        if key == 'Type':
            return self.formatter_type(item[key])
        elif key == 'Status':
            return self.formatter_status(item[key])
        else:
            value = item.get(key, '')
            if value is not None and isinstance(value, str):
                return value.replace('&nbsp;', ' ')
            return value


class ExportExcelLabor(ExportExcelBase):
    header = ['姓名', '身份证', '劳工状态', '性别', '年龄', '民族', '出生日期', '工种', '电话号码',
              '紧急联系人号码', '省', '市', '区', '所属项目', '所属公司', '所属班组']
    header_Name = ['Name', 'IDCard', 'Isbadrecord', 'Sex', 'Age', 'Nationality', 'Birthday', 'JobType',
                   'Phone', 'EmerCon', 'PName', 'CName', 'DName', 'ProjectName', 'CompanyName', 'ClassName']

    def __init__(self):
        super(ExportExcelLabor, self).__init__()
        self.export_name = 'labor.xlsx'
        self.temp_data = None
        self.labor_type = ['钢筋工', '架子工', '模板工', '通风工', '机械设备安装工']
        self.labor_status = ['正常', '不良', '黑名单']

    def formatter_type(self, l_type):
        if isinstance(l_type, str):
            l_type = int(l_type)
        return self.labor_type[l_type]

    def formatter_status(self, status):
        if isinstance(status, str):
            status = int(status)
        return self.labor_status[status]

    def query_data(self, data):
        self.temp_data = data

    def formatter_key(self, item, key):
        if key == 'JobType':
            return self.formatter_type(item[key])
        elif key == 'Isbadrecord':
            return self.formatter_status(item[key])
        elif key == 'Sex':
            val = item.get(key, '')
            if val == '':
                return ''
            else:
                if isinstance(val, str):
                    val = int(val)
                return '男' if val else '女'
        else:
            value = item.get(key, '')
            if value is not None and isinstance(value, str):
                return value.replace('&nbsp;', ' ')
            return value


class ExportExcelGuarantee(ExportExcelBase):
    header = ['保函编号', '项目名称', '公司名称', '项目区域', '受益人', '担保金额（万元）', '开始执行日期', '保函结束日期',
              '是否过期', '担保类型']
    header_Name = ['Number', 'ProjectID', 'CompanyID', 'Area', 'Bene', 'Amount', 'SignTime', 'Expiretime',
                   'IsExpire', 'Category']

    def __init__(self):
        super(ExportExcelGuarantee, self).__init__()
        self.export_name = 'guarantee.xlsx'
        self.temp_data = None
        self.category_list = ['投标', '履约', '预付款', '农民工工资支付', '业主支付', '质量', '资本金', '房屋质量', '其他']

    def query_data(self, data):
        self.temp_data = data

    def formatter_area(self, item):
        return item.get('Pname', '') + item.get('Cname', '') + item.get('Dname', '')

    def formatter_category(self, category):
        if isinstance(category, str):
            category = int(category)
        return self.category_list[category]

    def formatter_key(self, item, key):
        if key == 'Area':
            return self.formatter_area(item)
        elif key == 'Category':
            return self.formatter_category(item[key])
        else:
            value = item.get(key, '')
            if value is not None and isinstance(value, str):
                return value.replace('&nbsp;', ' ')
            return value
