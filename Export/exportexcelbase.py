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
        将格式化后的数据写入IO流
        :return:
        """
        self.excel = xlsxwriter.Workbook(self.io)
        sheet = self.excel.add_worksheet(u'sheet1')
        style = self.excel.add_format(self.xlsx_style())
        # 插入数据
        sheet.write_row('A1', self.header, style)
        for i in range(len(self.data)):
            sheet.write_row('A{}'.format(i + 2), self.data[i], style)
        self.excel.close()

    def get_stream(self):
        """
        导出数据
        :return:
        """
        self.io.seek(0)
        return self.io.getvalue()  # 获取文件流

    def get_name(self):
        if self.export_name == '' or self.export_name is None:
            raise NameError('export_template file name is None')
        return self.export_name

    def get_content_type(self):
        return self.content_type

    def xlsx_style(*args, **kwargs):
        """
        excel表格格式化
        :param kwargs:
        :return:
        """
        style = {
            'bold': kwargs.get('bold', False),  # 加粗
            'font_name': kwargs.get('font_name', 'SimSun'),  # 字体类型，默认宋体
            'font_size': kwargs.get('font_size', 12),  # 字体大小，默认12
            'font_color': kwargs.get('font_color', '#000000'),  # 字体颜色，黑色
            'align': kwargs.get('align', 'center'),  # 默认水平居中
            'valign': kwargs.get('valign', 'vcenter'),  # 默认垂直居中
            'text_wrap': kwargs.get('text_wrap', True),  # 默认自动换行
            'top': kwargs.get('top', 1),  # 上边界，线条宽度
            'bottom': kwargs.get('bottom', 1),  # 边界
            'left': kwargs.get('left', 1),  # 边界
            'right': kwargs.get('right', 1),  # 边界
            'bg_color': kwargs.get('bg_color', '#FFFFFF'),  # 背景颜色，白色
            # 其他类型设置格式可以接着写
        }

        return style
