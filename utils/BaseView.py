from copy import deepcopy
from flask import session, request, jsonify
from flask.views import View

from utils import status_code
from utils.pulic_utils import str_to_datetime
from utils.sqlutils import coon_mysql
from abc import ABCMeta, abstractmethod


class BaseView(View, metaclass=ABCMeta):
    decorators = (coon_mysql,)

    def __init__(self):
        super(BaseView, self).__init__()
        self._permissions = None
        self.api_permission = None  # api 接口权限名称和数据库中的名称对应
        self._uid = None  # 用户uid
        self._db = None  # 数据库连接对象
        self.args = None  # 前端传过来的参数字典
        self.ids = None  # 用户可以查看的权限范围ID列表
        self.success = deepcopy(status_code.SUCCESS)
        # self.get_args()

    def get_args(self):
        """
        多种方式获取前端传过来的参数
        :return:
        """
        args = dict(request.form.items())
        if dict(args) == {}:
            args = request.args
        if dict(args) == {}:
            args = request.json
            if args is None:
                args = {}
        self.args = args

    def time_format(self, time_str):
        return str_to_datetime(time_str)

    def time_to_str(self, datetime_obj):
        return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

    def set_ids(self, sql):
        """
        当用户不是superadmin时，获取管辖范围内的id（公司，项目，劳工）
        :param sql:
        :return:
        """
        result = self._db.query(sql)
        return [item['ID'] for item in result]

    def to_sql_where_id(self):
        """
        将查询到得管辖范围id列表转换为where子句中in部分的内容
        :return:
        """
        temp = ''
        for index, i in enumerate(self.ids):
            temp += str(i)
            if index < len(self.ids) - 1:
                temp += ','
        return temp

    def query_filter(self, result, field='ID'):
        """
        搜索查询过滤，将正常查询的结果和管辖范围内的ID进行对比，过滤掉不是管辖范围内的数据
        :param result:
        :return:
        """
        if self.ids:
            temp_result = []
            for item in result:
                if item[field] in self.ids:
                    temp_result.append(item)
            return temp_result
        else:
            return result

    def check_permission(self):
        """
        权限验证，有权限返回True，没有权限返回False
        :return:
        """
        if self.api_permission is not None:
            if self.api_permission not in session['Permission']:
                return False
        return True

    def dispatch_request(self, db):
        """
        请求进入后台处理的初始函数
        :param db:
        :return:
        """
        self.get_args()
        self._db = db
        return self.administrator()
        try:
            tempint = session['AdminType']
        except:
            return jsonify(status_code.USER_NOT_LOGIN)
        if int(session['AdminType']) == 0:
            return self.administrator()
        elif int(session['AdminType']) == 1:
            if not self.check_permission():
                return jsonify(status_code.PERMISSION_NOT_EXISTS)
            return self.admin()
        else:
            if not self.check_permission():
                return jsonify(status_code.PERMISSION_NOT_EXISTS)
            return self.guest()

    def args_is_null(self, *args):
        """
        判断参数是否是空，传入一个不定常参数
        :param args:
        :return:
        """
        for i in args:
            if self.args.get(i, None) is None:
                return True
            if self.args.get(i, '') == '':
                return True
            if self.args.get(i, '') == 'null':
                return True
            if self.args.get(i, '') == 'NaN':
                return True
            if i in ('ProvinceID', 'CityID', 'DistrictID', 'PID', 'CID', 'DID', 'province', 'city', 'district'):
                if self.args.get(i, '') == '0':
                    return True
            if self.args.get(i) == 'undefined' or self.args.get(i) == '请选择':
                return True
        return False

    @abstractmethod
    def administrator(self):
        pass

    @abstractmethod
    def admin(self):
        pass

    # @abstractmethod
    def guest(self):
        return self.admin()

    def has_data(self, table_name, field, data, db_id):
        if db_id is None:
            query_sql = r"""select id from {} where {}='{}';""".format(table_name, field, data)
        else:
            query_sql = r"""select id from {} where {}='{}' and id!={};""".format(table_name, field, data, db_id)
        result = self._db.query(query_sql)
        if result:
            return True
        return False

    def get_session_ids(self):
        """
        将session中的区域ID转换为sql语句中where中的条件格式
        :return:
        """
        temp = ''
        for index, area_id in enumerate(session['area_ids']):
            temp += str(area_id)
            if index < len(session['area_ids']) - 1:
                temp += ','
        return temp

    def get_where_sql(self, where_sql_list):
        temp = ''
        if where_sql_list:
            temp = ' where '
            for index, i in enumerate(where_sql_list):
                temp += i
                if index < len(where_sql_list) - 1:
                    temp += ' and '
        return temp


class DelteBase(BaseView):

    def __init__(self):
        super(DelteBase, self).__init__()
        self.table_name = ''

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.views()

    def views(self):
        ID = self.args.get('ID', None)
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        delete_sql = r"""delete from {} where id={}""".format(self.table_name, ID)
        self._db.delete(delete_sql)
        return jsonify(status_code.SUCCESS)
