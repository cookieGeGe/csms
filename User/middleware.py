import functools
from flask import session, jsonify, request

from utils import status_code


def is_login(view):
    @functools.wraps(view)
    def decorator(*args, **kwargs):
        try:
            # 验证用户是否登录
            # if session['user_id']:
            if 'login' in session and session['login']:
                return view(*args, **kwargs)
            else:
                return jsonify(status_code.USER_NOT_LOGIN)

        except:
            return jsonify(status_code.OTHER_ERROR)

    return decorator

def check_permission(view):
    @functools.wraps(view)
    def decorator(*args, **kwargs):
        try:
            # 验证用户是否登录
            # if session['user_id']:
            url = request.url
            if url in session['api']:
                return view(*args, **kwargs)
            else:
                return jsonify(status_code.PERMISSION_NOT_EXISTS)

        except:
            return jsonify(status_code.OTHER_ERROR)

    return decorator