from flask import Blueprint

from Guarantee.views import CreateCGuarantee, UpdateCGuarantee, CreateGuaranteePic, GetPicGroupList, CreateGuarantee, \
    UpdateGuarantee, QueryGuarantee

guarantee = Blueprint('Guarantee', __name__)

# 创建反担保人
guarantee.add_url_rule('/cguarantee/create', methods=['POST'], view_func=CreateCGuarantee.as_view('create_cguarantee'))
# 更新反担保人
guarantee.add_url_rule('/cguarantee/update', methods=['POST'], view_func=UpdateCGuarantee.as_view('update_cguarantee'))
# 创建图片分组
guarantee.add_url_rule('/addgroup', methods=['POST'], view_func=CreateGuaranteePic.as_view('Pic_cguarantee'))
# 获取图片分组列表 劳工和保函共用ptype 2为劳工，3为保函
guarantee.add_url_rule('/getgroup', methods=['GET'], view_func=GetPicGroupList.as_view('get_pic_list'))
# 创建保函
guarantee.add_url_rule('/create', methods=['POST'], view_func=CreateGuarantee.as_view('add_cguarantee'))
# 更新保函
guarantee.add_url_rule('/update', methods=['POST'], view_func=UpdateGuarantee.as_view('update_guarantee'))
# 查询保函
guarantee.add_url_rule('/query', methods=['get'], view_func=QueryGuarantee.as_view('query_guarantee'))
