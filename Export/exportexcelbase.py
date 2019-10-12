# -*- coding: utf-8 -*-
# @Time : 2019/10/12
# @Author : zhang
# @Site :
# @File : exportexcelbase.py
# @Software: PyCharm
from abc import abstractmethod, ABCMeta
from io import BytesIO

import xlsxwriter


class ExportExcelBase(metaclass=ABCMeta):
    header = []  # 待实现
    content_type = 'application/x-xlsx'

    def __init__(self):
        self.export_name = ''
        self.data = []
        self.excel = None
        self.io = BytesIO()

    @abstractmethod
    def query_data(self):
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
        self.excel = xlsxwriter.Workbook(self.io)
        sheet = self.excel.add_worksheet(u'sheet1')
        # 插入数据
        sheet.write_row('A1', self.header)
        for i in len(self.data):
            sheet.write_row('A{}'.format(i + 2), self.data[i])
        self.excel.close()

    def get_stream(self):
        """
        导出数据
        :return:
        """
        self.io.seek(0)
        return self.io.getvalue()  # 获取文件流

    def get_name(self):
        return self.export_name

    def get_content_type(self):
        return self.content_type
