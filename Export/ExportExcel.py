# -*- coding: utf-8 -*-
# @Time : 2019/10/12 16:38
# @Author :
# @Site :
# @File : ExportDocx.py
# @Software: PyCharm
from Export.exportexcel_views import ExportExcelTest


class ExportExcelFactory:

    def get_export_obj(self, export_type):
        if export_type == 'test':
            return ExportExcelTest()
