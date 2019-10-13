# -*- coding: utf-8 -*-
# @Time : 2019/10/13
# @Author : zhang
# @Site :
# @File : exportexcel_views.py
# @Software: PyCharm
from Export.exportexcelbase import ExportExcelBase


class ExportExcelTest(ExportExcelBase):
    header = ['第一列', '第二列', '第三列', '第四列', '第五列', '第六列']

    def __init__(self):
        super(ExportExcelTest, self).__init__()
        self.export_name = 'test.xlsx'

    def query_data(self, view):
        print('excel test view:', view)

    def formatter(self):
        self.data = [['测试', 1, 'abc', 12.345]]
