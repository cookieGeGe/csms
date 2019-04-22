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
        self.success = deepcopy(status_code.SUCCESS)

    def dispatch_request(self, db):
        self._db = db
        return self.administrator()
        # if int(session['AdminType']) == 0:
        #     return self.administrator()
        # elif int(session['AdminType']) == 1:
        #     return self.admin()
        # else:
        #     return self.guest()

    @abstractmethod
    def administrator(self):
        pass

    @abstractmethod
    def admin(self):
        pass

    @abstractmethod
    def guest(self):
        pass


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
        ID = request.args.get('ID', None)
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        delete_sql = r"""delete from {} where id={}""".format(self.table_name, ID)
        self._db.delete(delete_sql)
        return jsonify(status_code.SUCCESS)