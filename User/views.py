from copy import deepcopy

from flask import request, jsonify, session, make_response
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
        password = self.args.get('Password', '')
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
        if not check_password_hash(pwd, args['Password']):
            return jsonify(status_code.PASSWORD_ERROR)
        session['id'] = self.uid
        session['AdminType'] = result[0]['AdminType']
        session['url'] = self.get_all_url()
        if result[0]['AdminType']:
            session['area_ids'] = self.get_area_ids()
        success = deepcopy(status_code.SUCCESS)
        success['Permission'], success['AllPermission'] = self.get_permissions(self.uid)
        session['Permission'], session['AllPermission'] = success['Permission'], success['AllPermission']
        session['login'] = True
        # a = jsonify(success)
        # a.set_cookie('session', session)
        # response = make_response({"success":success, "session": session})
        return jsonify(success)

    def get_permissions(self, uid):
        query_sql = r"""select t2.* from tb_user_per as t1
                        left join tb_permission as t2 on t1.PID = t2.ID
                        where t1.uid = {};""".format(uid)
        total = self._db.query(query_sql)
        permission_list = [item['Permission'] for item in total]
        return permission_list, total

    def get_area_ids(self):
        """
        获取登录用户所能管控的地区ID
        :param uid:
        :return:
        """
        query_sql = r"""select t2.* from tb_user_area as t1
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


class UpdateUser(BaseView):

    def __init__(self):
        super(UpdateUser, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        args = self.args
        loginname_sql = r"""select t1.*, t2.AreaID  from tb_user as t1
                            left join tb_user_area as t2 on t1.id = t2.UserID
                            where t1.ID =  {ID}""".format(**args)
        result = self._db.query(loginname_sql)[0]
        ava_file = request.files.get('file', '')
        if ava_file != '':
            args['Avatar'] = save_image(ava_file)
        else:
            args['Avatar'] = result['Avatar']
        if result['Password'] == args.get('Password', ''):
            update_sql = r"""update tb_user set LoginName = '{LoginName}',
                                            UserName = '{UserName}',
                                            Email= '{Email}',
                                            Phone='{Phone}',
                                            Description='{Description}',
                                            AdminType={AdminType},
                                            CompanyID={CompanyID},
                                            Avatar='{Avatar}',
                                            Status={Status}""".format(**args)
        else:
            args['Password'] = generate_password_hash(args.get('Password', ''))
            update_sql = r"""update tb_user set LoginName = '{LoginName}',
                                                UserName = '{UserName}',
                                                Email= '{Email}',
                                                Phone='{Phone}',
                                                Password='{Password}'
                                                Description='{Description}',
                                                AdminType={AdminType},
                                                CompanyID={CompanyID},
                                                Avatar='{Avatar}',
                                                Status={Status}""".format(**args)
        self._db.update(update_sql)
        if int(result['AreaID']) != int(args['AreaID']):
            update_area_sql = r"""update tb_user_area set AreaID = {} where UserID = {}""".format(int(args['AreaID']),
                                                                                                  int(result['ID']))
            self._db.update(update_area_sql)
        return jsonify(status_code.SUCCESS)


class QueryUser(BaseView):

    def __init__(self):
        super(QueryUser, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        query_sql = r"""select t1.*, t3.AreaID from tb_user as t1
                        left join tb_user_area as t3 on t3.userid = t1.id
                        where t3.areaid in ({})""".format(self.get_session_ids())
        self.ids = self._db.query(query_sql)
        return self.views()

    def views(self):
        args = self.args
        query_sql = r"""select t1.*, t2.Name, t3.AreaID from tb_user as t1
                        left join tb_company as t2 on t1.companyID = t2.id
                        left join tb_user_area as t3 on t3.userid = t1.id"""
        where_list = []
        if self.ids:
            where_list.append(r""" t1.id in ({}) """.format(self.to_sql_where_id()))
        if args.get('CompanyName', '') != '':
            where_list.append(r""" CONCAT(IFNULL(t2.Name,'')) LIKE '%{}%' """.format(args.get('CompanyName', '')))
        if args.get('UserName', '') != '':
            where_list.append(r""" CONCAT(IFNULL(t1.UserName,'')) LIKE '%{}%' """.format(args.get('UserName', '')))
        if int(args.get('AreaID', 0)) != 0:
            query_area_sql = r"""select * from tb_area where id={}""".format(args['AreaID'])
            result = self._db.query(query_area_sql)
            areaids = get_all_area_id(self._db, result)
            areaids += [int(args['AreaID']), ]
            temp = ''
            for index, aid in enumerate(areaids):
                temp += str(aid)
                if index < len(areaids) - 1:
                    temp += ','
            where_list.append(r""" t3.AreaID in  ({})""".format(temp))
        where_sql = ''
        if where_list:
            where_sql = ' where '
            for index, temp_sql in enumerate(where_list):
                where_sql += temp_sql
                if index < len(where_list) - 1:
                    where_sql += ' and '
        page = int(args.get('Page', 1))
        pagesize = int(args.get('Pagesize', 10))
        limit_sql = ' limit {},{} '.format((page - 1) * pagesize, pagesize)
        result = self._db.query(query_sql + where_sql + limit_sql)
        success = status_code.SUCCESS
        success['user_list'] = result
        return jsonify(success)
