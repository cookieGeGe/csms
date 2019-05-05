from copy import deepcopy
from flask import session, request, jsonify
from flask.views import View

from utils import status_code
from utils.sqlutils import coon_mysql
from abc import ABCMeta, abstractmethod


class BaseView(View, metaclass=ABCMeta):
    decorators = (coon_mysql,)

    def __init__(self):
        super(BaseView, self).__init__()
        self._permissions = None
        self._uid = None
        self._db = None
        self.args = None
        self.success = deepcopy(status_code.SUCCESS)
        # self.get_args()

    def get_args(self):
        args = dict(request.form.items())
        if dict(args) == {}:
            args = request.args
        if dict(args) == {}:
            args = request.json
            if args is None:
                args = {}
        self.args = args

    def dispatch_request(self, db):
        self.get_args()
        self._db = db
        # return self.administrator()
        if int(session['AdminType']) == 0:
            return self.administrator()
        elif int(session['AdminType']) == 1:
            return self.admin()
        else:
            return self.guest()

    def args_is_null(self, *args):
        for i in args:
            if self.args.get(i, None) is None:
                return jsonify(status_code.CONTENT_IS_NULL)

    @abstractmethod
    def administrator(self):
        pass

    @abstractmethod
    def admin(self):
        pass

    # @abstractmethod
    def guest(self):
        return self.admin()


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
