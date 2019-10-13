# -*- coding: utf-8 -*-
# @Time : 2019/10/12
# @Author : zhang
# @Site :
# @File : exportwordbase.py
# @Software: PyCharm
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
