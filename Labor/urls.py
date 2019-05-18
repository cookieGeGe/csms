from flask import Blueprint

from Labor.views import CreateLabor, CreateLaborPicGroup, UpdateLabor, LaborInfo, QueryLabor, UploadLaborImg, AllLabor

labor = Blueprint('labor', __name__)
# 创建劳工
labor.add_url_rule('/regist', methods=['post'], view_func=CreateLabor.as_view('create_labor'))
# 创建劳工图片分组
labor.add_url_rule('/addgroup', methods=['post'], view_func=CreateLaborPicGroup.as_view('create_labor_pic_group'))
# 更新劳工信息
labor.add_url_rule('/update', methods=['post'], view_func=UpdateLabor.as_view('update_labor'))
# 获取劳工信息
labor.add_url_rule('/info', methods=['get'], view_func=LaborInfo.as_view('info_labor'))
# 劳工列表查询
labor.add_url_rule('/query', methods=['get'], view_func=QueryLabor.as_view('query_labor'))
# 上传劳工合同图片
labor.add_url_rule('/uploadpic', methods=['POST'], view_func=UploadLaborImg.as_view('update_pic_labor'))
# 获取项目下的劳工接口
labor.add_url_rule('/all', methods=['get'], view_func=AllLabor.as_view('all_labor'))
