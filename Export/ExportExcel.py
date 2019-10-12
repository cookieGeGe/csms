# -*- coding: utf-8 -*-
# @Time : 2019/10/12 16:38
# @Author :
# @Site :
# @File : ExportDocx.py
# @Software: PyCharm
from abc import ABCMeta, abstractmethod
from io import BytesIO

import xlsxwriter


class ExportExcelFactory:

    def get_export_obj(self, export_type):
        if export_type:
            pass


