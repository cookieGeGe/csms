from json import dumps

from copy import deepcopy

from flask import request, jsonify, session, make_response, Response
from werkzeug.security import generate_password_hash, check_password_hash

from User.util import save_image, get_all_area_id
from utils import status_code
from utils.BaseView import BaseView


class UserRegist(BaseView):

    def __init__(self):
        super(UserRegist, self).__init__()
        self.api_permission = 'permission_user_edit'
        self._form = None
        self._insert_sql = None

    # def dispatch_request(self, db):
    #     self.get_args()
    #     self._db = db
    #     if session['AdminType']:
    #         return self.admin()
    #     return self.administrator()

    def filter(self):
        form = request.form
        self._form = form
        username = form.get('UserName', '')
        password = form.get('Password', '')
        if username == '' or password == '':
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

    def insert_permission(self, tb, filed, value):
        try:
            uid = self._db.insert(self._insert_sql)
            area_sql = r"""insert into {}({}, {}) value ({}, {})""".format(tb, filed[0], filed[1], uid, value)
            self._db.insert(area_sql)
            return True
        except:
            if uid:
                delete_sql = r"""delete from tb_user where id = {};""".format(uid)
                self._db.delete(delete_sql)
            return False

    def views(self):
        """
        permission为1表示按照地区，为2表示按照项目
        :return:
        """
        ava_file = request.files.get('file', '')
        img_url = '/static/media/ava/home.png'
        if ava_file != '':
            img_url = save_image(ava_file)
        loginname_sql = r"""select id from tb_user where LoginName = '{}';""".format(self._form.get('UserName'))
        if len(self._db.query(loginname_sql)):
            return jsonify(status_code.USER_EXISTS)
        self._insert_sql = r"""insert into tb_user(LoginName,UserName,Password,Email,Phone,Description,AdminType,CompanyID,Avatar,Status, permission) 
                                value('{}', '{}','{}','{}','{}', '{}',{},{},'{}',1)"""
        self._insert_sql = self._insert_sql.format(
            self._form.get('UserName', ''),
            self._form.get('UserName', ''),
            self._form.get('Password', ''),
            self._form.get('Email', ''),
            self._form.get('Phone', ''),
            self._form.get('Description', ''),
            int(self._form.get('AdminType', 1)),
            int(self._form.get('CompanyID', 0)),
            img_url, self._form.get('permission', 1)
        )
        if self._form.get('permission', 1) == 1:
            if not self.insert_permission('tb_user_area', ['userid', 'areaid'], self._form.get('AreaID')):
                return jsonify(status_code.DB_ERROR)
            # try:
            #     uid = self._db.insert(self._insert_sql)
            #     area_sql = r"""insert into tb_user_area(userid, areaid) value ({}, {})""".format(uid,
            #                                                                                      self._form.get('AreaID'))
            #     self._db.insert(area_sql)
            # except:
            #     if uid:
            #         delete_sql = r"""delete from tb_user where id = {};""".format(uid)
            #         self._db.delete(delete_sql)
            #     return jsonify(status_code.DB_ERROR)
        else:
            if not self.insert_permission('tb_user_pro', ['uid', 'pid'], self._form.get('projectid')):
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
        sql = r"""select id,UserName,LoginName,Password,AdminType,Status,permission from tb_user where loginname='{}';""".format(
            args['LoginName'])
        result = self._db.query(sql)
        self.uid = result[0]['id']
        if not result:
            return jsonify(status_code.LOGINNAME_IS_NOT_EXISTS)
        if result[0]['Status'] != 1:
            return jsonify(status_code.USER_IS_DISABLED)
        pwd = result[0]['Password']
        if pwd != args['Password']:
            return jsonify(status_code.PASSWORD_ERROR)
        session['id'] = self.uid
        session['AdminType'] = result[0]['AdminType']
        session['url'] = self.get_all_url()
        # print(result[0]['AdminType'])
        if result[0]['AdminType']:
            session['area_ids'] = self.get_area_ids()
            # print(session['area_ids'])
        success = deepcopy(status_code.SUCCESS)
        success['Permission'], success['AllPermission'] = self.get_permissions(self.uid)
        session['Permission'], session['C'] = success['Permission'], success['AllPermission']
        session['login'] = True
        session['pertype'] = result[0]['permission']
        # a = jsonify(success)
        # a.set_cookie('session', session)
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
        delete_area = r"""delete from tb_user_area where userid ={};""".format(args.get('ID'))
        sql = r"""delete from tb_user where id = {};""".format(args.get('ID'))
        try:
            self._db.delete(delete_area)
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
        self.api_permission = 'permission_user_edit'

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
        if args.get('Password', '') == '':
            return jsonify(status_code.PASSWORD_IS_NULL)
            update_sql = r"""update tb_user set LoginName = '{UserName}',
                                            UserName = '{UserName}',
                                            Description='{Description}',
                                            Avatar='{Avatar}' where id={ID};""".format(**args)
        else:
            # args['Password'] = generate_password_hash(args.get('Password', ''))
            update_sql = r"""update tb_user set LoginName = '{UserName}',
                                                UserName = '{UserName}',
                                                Password='{Password}',
                                                Description='{Description}',
                                                Avatar='{Avatar}' where id ={ID} ;""".format(**args)
        self._db.update(update_sql)
        if result['AreaID'] is None:
            insert_sql = r"""insert tb_user_area(areaid,userid) value ({}, {});""".format(args['AreaID'], result['ID'])
            self._db.insert(insert_sql)
        elif int(result['AreaID']) != int(args['AreaID']):
            update_area_sql = r"""update tb_user_area set AreaID = {} where UserID = {}""".format(int(args['AreaID']),
                                                                                                  int(result['ID']))
            self._db.update(update_area_sql)
        else:
            pass
        return jsonify(status_code.SUCCESS)


class QueryUser(BaseView):

    def __init__(self):
        super(QueryUser, self).__init__()
        self.api_permission = 'permission_show'

    def administrator(self):
        return self.views()

    def admin(self):
        # query_sql = r"""select t1.*, t3.AreaID from tb_user as t1
        #                 left join tb_user_area as t3 on t3.userid = t1.id
        #                 where t3.areaid in ({})""".format(self.get_session_ids())
        # self.ids = self._db.query(query_sql)
        return self.views()

    def find_father(self, child_id):
        temp_father_name = []
        select = r"""select id, name, fatherid from tb_area where id = {};""".format(child_id)
        result = self._db.query(select)
        temp_father_name.extend([result[0]['name'], result[0]['id']])
        if result[0]['fatherid'] != 0:
            temp_father_name.extend(self.find_father(result[0]['fatherid']))
        # print(temp_father_name)
        return temp_father_name

    def main_query(self, args):
        where_list = []
        where_list.append(r""" t1.admintype !=0 """)
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            where_list.append(r""" t1.id in ({}) """.format(self.to_sql_where_id()))
        # if args.get('CompanyName', '') != '':
        #     where_list.append(r""" CONCAT(IFNULL(t2.Name,'')) LIKE '%{}%' """.format(args.get('CompanyName', '')))
        if args.get('UserName', '') != '':
            where_list.append(r""" CONCAT(IFNULL(t1.UserName,'')) LIKE '%{}%' """.format(args.get('UserName', '')))
        if int(args.get('AreaId', 0)) != 0:
            query_area_sql = r"""select * from tb_area where id={}""".format(args['AreaId'])
            result = self._db.query(query_area_sql)
            areaids = get_all_area_id(self._db, result)
            areaids += [int(args['AreaId']), ]
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
        return where_sql + limit_sql

    def views(self):
        args = self.args
        query_sql = r"""select SQL_CALC_FOUND_ROWS t1.* from tb_user as t1"""
        if int(args.get('ID', 0)) == 0:
            query_sql += self.main_query(args)
        else:
            query_sql += r""" where t1.id ={} """.format(args.get('ID'))
        result = self._db.query(query_sql)
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        for item in result:
            query_area_id = r"""select * from tb_user_area where userid = {};""".format(item['ID'])
            area_id_list = self._db.query(query_area_id)
            if not area_id_list:
                item['AreaName'] = ''
                item['PID'], item['CID'], item['DID'] = 0, 0, 0
                item['PName'], item['CName'], item['DName'] = '', '', ''
            else:
                area_list = self.find_father(area_id_list[0]['AreaID'])
                item['AreaName'] = '-'.join(area_list[::2][::-1])
                item['PID'], item['CID'], item['DID'] = 0, 0, 0
                item['PName'], item['CName'], item['DName'] = '', '', ''
                if len(area_list[::-1][::2]) == 1:
                    item['PName'] = area_list[::2][::-1][0]
                    item['PID'] = area_list[::-1][::2][0]
                elif len(area_list[::-1][::2]) == 2:
                    item['PName'], item['CName'] = area_list[::2][::-1]
                    item['PID'], item['CID'] = area_list[::-1][::2]
                elif len(area_list[::-1][::2]) == 3:
                    item['PID'], item['CID'], item['DID'] = area_list[::-1][::2]
                    item['PName'], item['CName'], item['DName'] = area_list[::2][::-1]
        success = deepcopy(status_code.SUCCESS)
        success['user_list'] = result
        success['total'] = total[0]['total_row']
        return jsonify(success)


class GetAllPermission(BaseView):
    """
    获取权限接口：
    :param ID 0表示获取当前用户的权限， 用户id 表示获取指定用户的权限
    """

    def __init__(self):
        super(GetAllPermission, self).__init__()
        self.except_show = ['permission_show', 'labor_badrecord_show']

    def admin(self):
        return self.views()

    def administrator(self):
        return self.views()

    def get_permissions(self, uid):
        query_sql = r"""select t2.* from tb_user_per as t1
                        left join tb_permission as t2 on t1.PID = t2.ID
                        where t1.uid = {};""".format(uid)
        total = self._db.query(query_sql)
        permission_list = [item['Permission'] for item in total]
        return permission_list, total

    def views(self):
        success = deepcopy(status_code.SUCCESS)
        args = self.args
        query_sql = r"""select * from tb_permission;"""
        total = self._db.query(query_sql)
        if int(args.get('ID', 0)) == 0:
            # success['AllPermission'] = session.get('AllPermission')
            user_permission = session.get('Permission')
        else:
            user_permission, user_all_permission = self.get_permissions(args.get('ID'))
        menu_show = {}
        button_show = {}
        for item in total:
            if 'show' in item['Permission']:
                if item['Permission'] in user_permission:
                    menu_show[item['Permission']] = 1
                else:
                    menu_show[item['Permission']] = 0
            else:
                if item['Permission'] in user_permission:
                    button_show[item['Permission']] = 1
                else:
                    button_show[item['Permission']] = 0
        success['menu_show'] = menu_show
        success['button_show'] = button_show

        return jsonify(success)


class SuperAdminAddPer(BaseView):

    def __init__(self):
        super(SuperAdminAddPer, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        query_sql = r"""select id from tb_user where admintype=0;"""
        result = self._db.query(query_sql)
        values = []
        if result:
            for item in result:
                values.append(r""" ({},{}) """.format(item['id'], self.args.get('id')))
        if values:
            insert_sql = r"""insert into tb_user_per(uid, pid) values {};""".format(','.join(values))
            self._db.insert(insert_sql)
        return jsonify(self.success)
