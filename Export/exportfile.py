# -*- coding: utf-8 -*-
# @Time : 2019/10/12
# @Author : zhang
# @Site :
# @File : exportfile.py
# @Software: PyCharm
from Export.ExportDocx import ExportWordFactory
from Export.ExportExcel import ExportExcelFactory


class ExportFile:

    def get_export_factory(self, type):
        if type == 'word':
            return ExportWordFactory()
        if type == 'excel':
            return ExportExcelFactory()
