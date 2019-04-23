from copy import deepcopy

from flask import request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

from User.util import save_image, get_all_area_id
from utils import status_code
from utils.BaseView import BaseView


class UserRegist(BaseView):

    def __init__(self):
        super(UserRegist, self).__init__()
        self._form = None
        self._insert_sql = None

    def dispatch_request(self, db):
        self.get_args()
        self._db = db
        return self.administrator()

    def filter(self):
        form = request.form
        self._form = form
        name = form.get('LoginName', '')
        username = form.get('UserName', '')
        password = form.get('PassWord', '')
        if name == '' or username == '' or password == '':
            return False
        return True

    def administrator(self):
        if not self.filter():
            return jsonify(status_code.CONTENT_IS_NULL)
        return self.views()

    def admin(self):
        return self.administrator()

    def guest(self):
        return jsonify(status_code.PERMISSION_ERROR)

    def views(self):
        ava_file = request.files.get('file', '')
        img_url = '/static/media/ava/home.png'
        if ava_file != '':
            img_url = save_image(ava_file)
        loginname_sql = r"""select id from tb_user where LoginName = {LoginName}""".format(**self._form)
        if len(self._db.query(loginname_sql)):
            return jsonify(status_code.USER_EXISTS)
        self._insert_sql = r"""insert into tb_user(LoginName,UserName,Password,Email,Phone,Description,AdminType,CompanyID,Avatar,Status) 
                                value('{}', '{}','{}','{}','{}', '{}',{},{},'{}',1)"""
        self._insert_sql = self._insert_sql.format(
            self._form.get('LoginName', ''),
            self._form.get('UserName', ''),
            str(generate_password_hash(self._form.get('Password', ''))),
            self._form.get('Email', ''),
            self._form.get('Phone', ''),
            self._form.get('Description', ''),
            int(self._form.get('AdminType', 0)),
            int(self._form.get('CompanyID', 0)),
            img_url,
        )
        try:
            id = self._db.insert(self._insert_sql)
            area_sql = r"""insert into tb_user_area(userid, areaid) value ({}, {})""".format(id,
                                                                                             self._form.get('AreaID'))
            self._db.insert(area_sql)
        except:
            return jsonify(status_code.DB_ERROR)
        return jsonify(deepcopy(status_code.SUCCESS))


class UserLogin(BaseView):

    def __init__(self):
        super(UserLogin, self).__init__()
        self._form = None
        self._insert_sql = None
        self.uid = None

    def dispatch_request(self, db):
        self.get_args()
        self._db = db
        return self.administrator()

    def filter(self):
        self._form = self.args
        name = self.args.get('LoginName', '')
        password = self.args.get('PassWord', '')
        if name == '' or password == '':
            return False
        return True

    def administrator(self):
        if not self.filter():
            return jsonify(status_code.CONTENT_IS_NULL)
        return self.views()

    def admin(self):
        return self.administrator()

    def guest(self):
        return self.administrator()

    def views(self):
        args = self.args
        sql = r"""select id,UserName,LoginName,Password,AdminType,Status from tb_user where loginname='{}';""".format(
            args['LoginName'])
        result = self._db.query(sql)
        self.uid = result[0]['id']
        if not result:
            return jsonify(status_code.LOGINNAME_IS_NOT_EXISTS)
        if result[0]['Status'] != 1:
            return jsonify(status_code.USER_IS_DISABLED)
        pwd = result[0]['Password']
        if not check_password_hash(pwd, args['PassWord']):
            return jsonify(status_code.PASSWORD_ERROR)
        session['id'] = self.uid
        session['AdminType'] = result[0]['AdminType']
        session['url'] = self.get_all_url()
        if result[0]['AdminType']:
            session['area_ids'] = self.get_area_ids(self.uid)
        success = deepcopy(status_code.SUCCESS)
        success['PerName'], session['api'] = self.get_permissions(self.uid)
        session['login'] = True
        return jsonify(status_code.SUCCESS)

    def get_permissions(self, uid):
        query_sql = r"""select t2.ID,t2.PerName, t2.Permission, t3.Name from tb_user_per as t1
                        LEFT JOIN tb_permission as t2 on t1.PID = t2.ID
                        LEFT JOIN tb_api as t3 on t3.PID = t2.ID
                        WHERE t1.UID = {};""".format(uid)
        per_name_list = []
        per_id_list = []
        permission_list = []
        api_list = []
        total = self._db.query(query_sql)
        for item in total:
            per_id_list.append(item['ID'])
            per_name_list.append(item['PerName'])
            permission_list.append(item['Permission'])
            api_list.append(item['Name'])
        return per_name_list, api_list

    def get_area_ids(self):
        """
        获取登录用户所能管控的地区ID
        :param uid:
        :return:
        """
        query_sql = r"""select t1.* from tb_user_area as t1
                        left join tb_area as t2 on t1.areaid=t2.id
                        where t1.userid={}""".format(self.uid)
        area_list = self._db.query(query_sql)
        all_area_id = get_all_area_id(self._db, area_list)
        return all_area_id

    def get_all_url(self):
        query_sql = r"""select url,name from tb_user_per as t1
                        right join tb_per_url as t2 on t1.pid = t2.pid
                        where t1.UID = {};""".format(self.uid)
        result = self._db.query(query_sql)
        url_list = [item['url'] for item in result]
        return url_list


class UserLogout(BaseView):

    def __init__(self):
        super(UserLogout, self).__init__()
        self._form = None
        self._insert_sql = None
        self.uid = None

    def administrator(self):
        session['login'] = False
        return jsonify(status_code.SUCCESS)

    def admin(self):
        return self.administrator()

    def guest(self):
        return self.administrator()


class UserDelete(BaseView):

    def __init__(self):
        super(UserDelete, self).__init__()
        self._form = None
        self._insert_sql = None
        self.uid = None

    def administrator(self):
        args = self.args
        sql = r"""delete from tb_user where id = {};""".format(args.get('ID'))
        try:
            self._db.delete(sql)
            return jsonify(status_code.SUCCESS)
        except Exception as e:
            return jsonify(status_code.DELETE_USER_FAILD)

    def admin(self):
        return self.administrator()

    def guest(self):
        return self.administrator()


class StopUser(BaseView):

    def __init__(self):
        super(StopUser, self).__init__()
        self._form = None
        self._insert_sql = None
        self.uid = None

    def administrator(self):
        args = self.args
        sql = r"""update tb_user set status=0 where id = {};""".format(args.get('ID'))
        try:
            self._db.update(sql)
            return jsonify(status_code.SUCCESS)
        except Exception as e:
            return jsonify(status_code.DELETE_USER_FAILD)

    def admin(self):
        return self.administrator()

    def guest(self):
        return self.administrator()
