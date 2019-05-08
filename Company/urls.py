from flask import Blueprint

from Company.views import CreatePicGroup, DeletePicGroup, DeletePic, GetGroupList, GetCompanyList, \
    UploadPic, GetCompanyInfo, UpdateCompany, CreateCompany,EditGroup,GetOnePic,GetGroupPicList,AllCompanyID

company = Blueprint('company', __name__)
# 创建图片分组 - 已测试
company.add_url_rule('/addgroup', methods=['post'], view_func=CreatePicGroup.as_view('create_pic_group'))
# 删除图片分组 - 已测试
company.add_url_rule('/deletepicgroup', methods=['delete'], view_func=DeletePicGroup.as_view('delete_pic_group'))
# 删除图片 - 已测试
company.add_url_rule('/picgroup', methods=['delete'], view_func=DeletePic.as_view('delete_pic'))
# 获取分组列表 - 已测试
company.add_url_rule('/getpicgroup', methods=['get'], view_func=GetGroupList.as_view('get_pic_group'))
# 获取企业列表 - 已测试
company.add_url_rule('/list', methods=['get'], view_func=GetCompanyList.as_view('get_company_list'))
# 获取企业详细信息 - 已测试
company.add_url_rule('/info', methods=['get'], view_func=GetCompanyInfo.as_view('get_company_iNFO'))
# 上传图片 - 已测试
company.add_url_rule('/uploadgrouppic', methods=['post'], view_func=UploadPic.as_view('upload_pic'))
# 企业注册 - 已测试
company.add_url_rule('/regist', methods=['post'], view_func=CreateCompany.as_view('create_company'))
# 更新企业信息-已测试
company.add_url_rule('/update', methods=['post'], view_func=UpdateCompany.as_view('update_company'))
# 修改图片分组名称 - 已测试
company.add_url_rule('/group/edit', methods=['post'], view_func=EditGroup.as_view('editgroup'))
# 查看单个图片 - 已测试
company.add_url_rule('/pic/getone', methods=['GET'], view_func=GetOnePic.as_view('GET_one_pic'))
# 获取分组下图片列表 - 已测试
company.add_url_rule('/pic/list', methods=['get'], view_func=GetGroupPicList.as_view('get_pic_list'))
# 获取所有企业
company.add_url_rule('/allcompany', methods=['get'], view_func=AllCompanyID.as_view('all_company_list'))
