from flask import Blueprint

from User.permission_view import Permission
from User.views import UserLogin, UserRegist, UserDelete, StopUser, UserLogout, UpdateUser, QueryUser, GetAllPermission, \
    SuperAdminAddPer

user = Blueprint('user', __name__)

user.add_url_rule('/regist', methods=['POST', ], view_func=UserRegist().as_view('regist'))
user.add_url_rule('/login', methods=['POST', ], view_func=UserLogin().as_view('login'))
user.add_url_rule('/logout', methods=['GET', ], view_func=UserLogout().as_view('logout'))
user.add_url_rule('/delete', methods=['DELETE', ], view_func=UserDelete().as_view('DELETE'))
user.add_url_rule('/down', methods=['GET', ], view_func=StopUser().as_view('stop_user'))
user.add_url_rule('/permission', methods=['POST', ], view_func=Permission().as_view('permission'))
user.add_url_rule('/update', methods=['POST', ], view_func=UpdateUser.as_view('update_user'))
user.add_url_rule('/query', methods=['GET', ], view_func=QueryUser.as_view('query_user'))
user.add_url_rule('/permission/get', methods=['GET', ], view_func=GetAllPermission.as_view('user_get_primission'))

# 超级管理员添加权限
user.add_url_rule('/addper', methods=['get'], view_func=SuperAdminAddPer.as_view('add_permission'))
