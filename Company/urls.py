from flask import Blueprint

from Company.views import CreatePicGroup, DeletePicGroup, DeletePic, GetGroupList, GetCompanyList, CompanyInfo

company = Blueprint('company', __name__)
# 创建图片分组
company.add_url_rule('/addgroup', methods=['post'], view_func=CreatePicGroup.as_view('create_pic_group'))
# 删除图片分组
company.add_url_rule('/deletepicgroup', methods=['delete'], view_func=DeletePicGroup.as_view('delete_pic_group'))
# 删除图片
company.add_url_rule('/picgroup', methods=['delete'], view_func=DeletePic.as_view('delete_pic'))
# 获取分组列表
company.add_url_rule('/getpicgroup', methods=['get'], view_func=GetGroupList.as_view('get_pic_group'))
# 获取企业列表
company.add_url_rule('/list', methods=['get'], view_func=GetCompanyList.as_view('get_company_list'))
# 获取企业详细信息
company.add_url_rule('/list', methods=['get'], view_func=CompanyInfo.as_view('get_company_iNFO'))


