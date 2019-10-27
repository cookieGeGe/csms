# -*- coding: utf-8 -*- 
# @Time : 2019/10/12 16:38 
# @Author :  
# @Site :  
# @File : ExportDocx.py 
# @Software: PyCharm
from abc import ABCMeta, abstractmethod

from docxtpl import DocxTemplate
from io import BytesIO

from Export import exportword_views


class ExportWordFactory:
    """
    工厂类（导出word工厂类）
    """

    def get_export_obj(self, export_type):
        if export_type == 'test':
            return exportword_views.ExportWordTest()
        elif export_type == 'company':
            return exportword_views.ExportCompanyWord()
        elif export_type == 'project':
            return exportword_views.ExportProjectWord()
        elif export_type == 'progress':
            return exportword_views.ExportProgressWord()
        elif export_type == 'labor':
            return exportword_views.ExportLaborWord()
