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
from . import salary_view
from . import bank_view
from . import guarantee_view
from . import question_view

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

# 工资计算
wechat.add_url_rule('/query/salary', methods=['get'], view_func=salary_view.WechatQuerySalary.as_view('wechat_salary'))

# 银行管理
wechat.add_url_rule('/query/bank', methods=['get'], view_func=bank_view.WechatBankQuery.as_view('wechat_bank'))
wechat.add_url_rule('/query/bank/info', methods=['get'], view_func=bank_view.WechatBankInfo.as_view('wechat_bank_info'))

# 保函查询
wechat.add_url_rule('/query/guarantee', methods=['get'],
                    view_func=guarantee_view.GuaranteeQuery.as_view('wechat_guarant'))

# 问答平台
wechat.add_url_rule('/query/question', methods=['get'],
                    view_func=question_view.WechatQuestion.as_view('wechat_question'))
