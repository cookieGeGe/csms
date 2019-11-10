# -*- coding: utf-8 -*-
# @Time : 2019/10/12 16:38
# @Author :
# @Site :
# @File : ExportDocx.py
# @Software: PyCharm
from Export.exportexcel_views import ExportExcelTest, ExportExcelCompany, ExportExcelProject, ExportExcelLabor,ExportExcelGuarantee


class ExportExcelFactory:

    def get_export_obj(self, export_type):
        if export_type == 'test':
            return ExportExcelTest()
        elif export_type == 'company':
            return ExportExcelCompany()
        elif export_type == 'project':
            return ExportExcelProject()
        elif export_type == 'labor':
            return ExportExcelLabor()
        elif export_type == 'guarantee':
            return ExportExcelGuarantee()
        else:
            raise Exception('导出excel错误')
