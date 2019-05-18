from flask import Blueprint

from Attend.views import ImportAttend, QueryAttendInfo, QueryAttend, ADDSalary, GetOneSalary, QuerySalary

attend = Blueprint('attend', __name__)

# 考勤导入
attend.add_url_rule('/import', methods=['post'], view_func=ImportAttend.as_view('import_attend'))
# 获取每个月考勤
attend.add_url_rule('/monthinfo', methods=['get'], view_func=QueryAttendInfo.as_view('attend_info'))
# 考勤查询页面
attend.add_url_rule('/query', methods=['get'], view_func=QueryAttend.as_view('query_attend'))

# 查询薪资计算
attend.add_url_rule('/salary/query', methods=['get'], view_func=QuerySalary.as_view('query_salary'))
# 获取薪资计算详情
attend.add_url_rule('/salary/info', methods=['get'], view_func=GetOneSalary.as_view('info_salary'))
# 创建和编辑薪资管理
attend.add_url_rule('/salary/create', methods=['post'], view_func=ADDSalary.as_view('info_salary'))
