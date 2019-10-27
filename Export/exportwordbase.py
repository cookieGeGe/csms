# -*- coding: utf-8 -*-
# @Time : 2019/10/12
# @Author : zhang
# @Site :
# @File : exportwordbase.py
# @Software: PyCharm
import datetime
from abc import ABCMeta, abstractmethod
from io import BytesIO

from docxtpl import DocxTemplate


class ExportDocxBase(metaclass=ABCMeta):
    template = None
    content_type = 'application/msword'

    def __init__(self):
        self.export_name = ''
        self.data = None
        self.doc = None
        self.export_data = {
            'export_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.company_type_list = [
            '施工企业', '监理单位', '勘察设计', '劳务公司', '房地产开发', '政府及事业单位', '其他业主单位', '其他'
        ]
        self.company_bad_list = ['', '正常', '风险', '黑名单']
        self.project_bad_list = ['正常', '常态监管', '重点', '严重']
        self.project_type_list = ['政府投资', '民营开发', '国企分包', '其他']
        self.bank_status_list = ['全额到', '部分到', '未到']

    @abstractmethod
    def query_data(self, view):
        """数据库中查询数据"""
        pass

    @abstractmethod
    def formatter(self):
        """
        将查出来的数据格式化成一个二维列表
        :return:
        """
        pass

    def render(self):
        """
        格式化数据
        :return:
        """
        if self.template is None:
            raise KeyError('请指定模板')
        self.doc = DocxTemplate(self.template)
        if self.data is None:
            raise TypeError('data is NoneType')
        self.doc.render(context=self.data)

    def get_stream(self):
        """
        导出数据
        :return:
        """
        io_t = BytesIO()
        self.doc.save(io_t)  # 将文件保存到流中
        io_t.seek(0)  # 指定文件流起始位置
        return io_t.getvalue()  # 获取文件流

    def get_name(self):
        if self.export_name == '' or self.export_name is None:
            raise NameError('export_template file name is None')
        return self.export_name

    def get_content_type(self):
        return self.content_type

    def content_is_null(self, *args, data):
        for arg in args:
            if data[arg] is None:
                return True
            if data[arg] == '':
                return True
        return False

    def query_company_data(self, company_id):
        query_sql = r"""select t1.ID, t1.Address, t1.BadRecord,t1.Description, t1.Legal, t1.License, t1.HasBadRecord,
                                t1.Name, t1.Phone, t1.Type, t1.url, t1.OtherInfo, t2.Name as ProvinceID, t3.Name as CityID, t4.Name as DistrictID, 
                                t1.ProvinceID as province, t1.CityID as city, t1.DistrictID as district from tb_company as t1
                                LEFT JOIN tb_area as t2 on t1.ProvinceID = t2.ID
                                LEFT JOIN tb_area as t3 on t1.CityID = t3.ID
                                LEFT JOIN tb_area as t4 on t1.DistrictID = t4.ID
                                where t1.id = {};""".format(company_id)
        resutl = self.db.query(query_sql)
        return resutl

    def get_type_or_bad(self, key_list, index):
        if isinstance(index, str):
            index = int(index)
        if index < len(key_list) - 1:
            return key_list[index]
        else:
            return ''
