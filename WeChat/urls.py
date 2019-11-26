# -*- coding: utf-8 -*-
# @Time : 2019/11/20
# @Author : zhang
# @Site :
# @File : urls.py
# @Software: PyCharm

from . import index_view
from . import company_view
from . import project_view
from . import labor_view
from . import attend_view

from flask import Blueprint

wechat = Blueprint(__name__, 'wechat')

# 首页统计查询
wechat.add_url_rule('/count', methods=['get'], view_func=index_view.WechatIndexCount.as_view('wechat_count'))

# 项目，详情查询
wechat.add_url_rule('/query/company', methods=['get'],
                    view_func=company_view.WechatComQuery.as_view('wechat_query_com'))
wechat.add_url_rule('/query/company/project', methods=['get'],
                    view_func=company_view.WechatComQueryPro.as_view('wechat_query_com_pro'))
wechat.add_url_rule('/query/project', methods=['get'],
                    view_func=project_view.WechatProQuery.as_view('wechat_query_pro'))
wechat.add_url_rule('/query/labor', methods=['get'], view_func=labor_view.WechatLaborQuery.as_view('wechat_query_lab'))

# 考勤
wechat.add_url_rule('/query/attend', methods=['get'], view_func=attend_view.QueryAttend.as_view('wechat_query_attend'))
wechat.add_url_rule('/query/attend/info', methods=['get'],
                    view_func=attend_view.QueryAttendLaborInfo.as_view('wechat_query_attend_info'))
