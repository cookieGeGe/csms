# -*- coding: utf-8 -*-
# @Time : 2020/1/5
# @Author : zhang
# @Site :
# @File : test.py
# @Software: PyCharm
import os

from flask import send_from_directory

from APP.settings import static_dir
from utils.BaseView import BaseView


class BackHelpPdf(BaseView):

    def __init__(self):
        super(BackHelpPdf, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        template_dir = os.path.join(static_dir, 'template')
        return send_from_directory(template_dir, 'use_new.pdf')
