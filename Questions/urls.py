# -*- coding: utf-8 -*-
# @Time : 2019/11/19
# @Author : zhang
# @Site :
# @File : urls.py
# @Software: PyCharm

from flask import Blueprint
from . import views

question = Blueprint(__name__, 'question')

question.add_url_rule('/query', methods=['get'], view_func=views.QueryQuestion.as_view('question_query'))
question.add_url_rule('/insert', methods=['post'], view_func=views.InsertQuestion.as_view('question_add'))
question.add_url_rule('/delete', methods=['delete'], view_func=views.DeleteQuestion.as_view('question_delete'))
