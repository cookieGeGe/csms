# -*- coding: utf-8 -*-
# @Time : 2019/11/11
# @Author : zhang
# @Site :
# @File : urls.py
# @Software: PyCharm

from flask import Blueprint

from ReceivePush import views

push = Blueprint(__name__, 'push')

push.add_url_rule('/attend', methods=['post'], view_func=views.ReceiveAttend.as_view('recevie_attend'))
