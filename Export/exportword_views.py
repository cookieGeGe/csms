# -*- coding: utf-8 -*-
# @Time : 2019/10/13
# @Author : zhang
# @Site :
# @File : exportword_views.py
# @Software: PyCharm
import datetime
import os
import random

from APP.settings import static_dir
from Export.exportwordbase import ExportDocxBase


class ExportWordTest(ExportDocxBase):
    template = os.path.join(static_dir, 'export_template', 'test.docx')

    def __init__(self):
        super(ExportWordTest, self).__init__()
        self.export_name = 'test.docx'

    def query_data(self, view):
        print(view)

    def formatter(self):
        self.data = {
            'title': '测试文档',
            'content': '建工管理软件导出测试文档——随机数{}'.format(random.randint(0, 100)),
            'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
