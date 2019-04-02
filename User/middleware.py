import functools
from flask import session, jsonify

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