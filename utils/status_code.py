# 返回错误码
SUCCESS = {'code': 0, 'res': 0, 'msg': '请求成功!'}

DB_ERROR = {'code': 50001, 'res': 0, 'msg': '数据库错误，请稍后再试'}
OTHER_ERROR = {'code': 50002, 'msg': '网络错误，请稍后再试'}


CONTENT_IS_NULL = {'code': 50003, 'res': 0, 'msg': '存在必填字段为空，请填写必填字段！'}
PERMISSION_ERROR = {'code': 50004, 'res': 0, 'msg': '普通用户不允许注册用户。'}
USER_UPLOAD_IMG_TYPE_ERROR = {'code': 50005, 'msg': '上传头像图片类型错误'}
USER_EXISTS = {'code': 50006, 'msg': '该用户已存在！'}
LOGINNAME_IS_NOT_EXISTS = {'code': 50007, 'msg': '用户名不存在，请输入正确的用户名！'}
PASSWORD_ERROR = {'code': 50008, 'msg': '密码错误！'}
USER_NOT_LOGIN = {'code': 50009, 'msg': '用户未登录，请登录后重试'}

