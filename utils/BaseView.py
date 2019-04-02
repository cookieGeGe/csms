from copy import deepcopy
from flask.views import View

from utils import status_code
from utils.sqlutils import coon_mysql
from abc import ABCMeta, abstractmethod


class BaseView(View, metaclass=ABCMeta):
    decorators = (coon_mysql,)

    def __init__(self):
        super(BaseView, self).__init__()
        self._token = None
        self._permissions = None
        self._uid = None
        self._db = None
        self._roles = None
        self.success = deepcopy(status_code.SUCCESS)

    def dispatch_request(self, db, token=None):
        self._db = db
        self._token = token
        self._uid = token['uid']
        self._permissions = token['permission']
        self._roles = token['roles']
        if 'superadmin' in self._roles:
            return self.administrator()
        elif 'admin' in self._roles:
            return self.admin()
        else:
            return self.guest()

    @abstractmethod
    def administrator(self):
        pass

    @abstractmethod
    def admin(self):
        pass

    @abstractmethod
    def guest(self):
        pass
