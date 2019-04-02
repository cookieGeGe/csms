from flask import Blueprint
from User.views import UserLogin, UserRegist

user = Blueprint('user', __name__)

user.add_url_rule('/regist', methods=['POST', ], view_func=UserRegist().as_view('regist'))
user.add_url_rule('/login', methods=['POST', ], view_func=UserLogin().as_view('login'))
