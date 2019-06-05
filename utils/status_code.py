# 返回错误码
SUCCESS = {'code': 0, 'res': 0, 'msg': '请求成功!'}

DB_ERROR = {'code': 50001, 'res': 0, 'msg': '数据库错误，请稍后再试'}
OTHER_ERROR = {'code': 50002, 'msg': '网络错误，请稍后再试'}
PERMISSION_NOT_EXISTS = {'code': 50012, 'msg': '权限不足，请联系管理员'}

CONTENT_IS_NULL = {'code': 50003, 'res': 0, 'msg': '存在必填字段为空，请填写必填字段！'}
PERMISSION_ERROR = {'code': 50004, 'res': 0, 'msg': '普通用户不允许注册用户。'}
USER_UPLOAD_IMG_TYPE_ERROR = {'code': 50005, 'msg': '上传头像图片类型错误'}
USER_EXISTS = {'code': 50006, 'msg': '该用户已存在！'}
LOGINNAME_IS_NOT_EXISTS = {'code': 50007, 'msg': '用户名不存在，请输入正确的用户名！'}
PASSWORD_ERROR = {'code': 50008, 'msg': '密码错误！'}
USER_NOT_LOGIN = {'code': 50009, 'msg': '用户未登录，请登录后重试'}
USER_IS_DISABLED = {'code': 50010, 'msg': '用户已停用，请联系管理员！'}
DELETE_USER_FAILD = {'code': 50011, 'msg': '删除用户失败1'}
ID_ERROR = {'code': 50012, 'msg': 'ID错误！'}
FILE_NOT_EXISTS = {'code': 50013, 'msg': '上传图片不存在！'}
DIR_NOT_EXISTS = {'code': 50014, 'msg': '上传目录错误！'}
GET_COMPANY_INFO_FAILD = {'code': 50015, 'msg': '没有找到当前用户！'}

LABOR_IS_EXISTS = {'code': 50016, 'msg': '身份证号码重复，请勿重复添加！'}
LABOR_IS_NOT_EXISTS = {'code': 50017, 'msg': '劳工不存在'}
TEMPLATE_ERROR = {'code': 50018, 'msg': '模板错误'}
BANK_INFO_EXISTS = {'code': 50019, 'msg': '该月信息已存在'}
CREATE_FEATURE_BANK_INFO = {'code': 50020, 'msg': '不能创建将来的月份信息'}
PROGRESS_TIME_ERROR = {'code': 50021, 'msg': '请上传项目期间的进度'}
