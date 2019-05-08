from flask import Blueprint

from Project.views import CreateProject, UpdateProject, DeleteProject, QueryProject, ProgressProject, \
    ADDProgressProject, CreateProPicGroup, GetComAndPer, GetProgressGicList, UploadProjectIMG, ProjectMainQuery, \
    ALLProjectID

project = Blueprint('project', __name__)

# 创建项目 -
project.add_url_rule('/create', methods=['POST'], view_func=CreateProject.as_view('create_pro'))
# 修改项目 -
project.add_url_rule('/update', methods=['POST'], view_func=UpdateProject.as_view('update_pro'))
# 删除项目 -
project.add_url_rule('/delete', methods=['DELETE'], view_func=DeleteProject.as_view('delete_pro'))
# 项目查询 -
project.add_url_rule('/query', methods=['GET'], view_func=QueryProject.as_view('query_pro'))
# 进度查询
project.add_url_rule('/progress/query', methods=['GET'], view_func=ProgressProject.as_view('progress_pro'))
# 添加项目进度 -
project.add_url_rule('/progress/create', methods=['GET'], view_func=ADDProgressProject.as_view('add_progress_pro'))
# 新建项目图片目录 - 已测试
project.add_url_rule('/group/create', methods=['Post'], view_func=CreateProPicGroup.as_view('create_pro_pic_group'))
# 获取企业和其负责人 - 已测试
project.add_url_rule('/companyinfo', methods=['get'], view_func=GetComAndPer.as_view('get_com_and_person'))
# 获取项目分组目录列表 - 已测试
project.add_url_rule('/group/list', methods=['get'], view_func=GetProgressGicList.as_view('get_progress_list'))
# 上传图片列表 - 已测试
project.add_url_rule('/img/upload', methods=['post'], view_func=UploadProjectIMG.as_view('upload_img'))
# 主项目进度查询 - 还差发放情况没有统计
project.add_url_rule('/search', methods=['get'], view_func=ProjectMainQuery.as_view('main_query'))
# 获取所有项目列表
project.add_url_rule('/allproject', methods=['get'], view_func=ALLProjectID.as_view('all_project'))
