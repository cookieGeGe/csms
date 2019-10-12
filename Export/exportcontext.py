# -*- coding: utf-8 -*-
# @Time : 2019/10/12
# @Author : zhang
# @Site :
# @File : exportcontext.py
# @Software: PyCharm


class ExportContext:

    def __init__(self, export_obj):
        self.export_obj = export_obj

    def query_data(self):
        self.export_obj.query_data()

    def formatter(self):
        self.export_obj.formatter()

    def render(self):
        self.export_obj.render()

    def get_stream(self):
        return self.export_obj.get_stream()

    @property
    def export_name(self):
        return self.export_obj.get_name()

    @property
    def content_type(self):
        return self.export_obj.get_content_type()
