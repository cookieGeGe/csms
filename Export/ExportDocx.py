# -*- coding: utf-8 -*- 
# @Time : 2019/10/12 16:38 
# @Author :  
# @Site :  
# @File : ExportDocx.py 
# @Software: PyCharm
from abc import ABCMeta, abstractmethod

from docxtpl import DocxTemplate
from io import BytesIO

from Export.exportword_views import ExportWordTest


class ExportWordFactory:
    """
    工厂类（导出word工厂类）
    """

    def get_export_obj(self, export_type):
        if export_type == 'test':
            return ExportWordTest()
