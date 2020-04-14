import datetime
from copy import deepcopy
from json import dumps, loads

from flask import jsonify, request, session

from Company.utils import update_pic_and_group
from Company.views import CreatePicGroup, AllCompanyID
from User.util import save_image
from utils import status_code
from utils.BaseView import BaseView
from utils.pulic_utils import str_to_date


class LaborBase(BaseView):

    def __init__(self):
        super(LaborBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        return jsonify(status_code.SUCCESS)


class CreateLabor(LaborBase):
    """
    创建劳工
    """

    def __init__(self):
        super(CreateLabor, self).__init__()
        self.api_permission = 'labor_edit'
        self._insert_list = ['Name', 'Age', 'Sex', 'Birthday', 'Address', 'Nationality', 'IDCard', 'Phone',
                             'CompanyId', 'JobType', 'ClassID', 'Identity', 'EntryDate', 'Hardhatnum',
                             'Education', 'CreateTime', 'ProjectID', 'IsPM', 'IssueAuth', 'Political',
                             'Train', 'EmerCon', 'IDP', 'IDB', 'PID', 'CID', 'DID', 'Superiors', 'IsLeader',
                             'CloseupPhoto', 'Remark', 'FeeStand', 'Avatar',
                             'isFeeStand', 'SubCompany', 'TrainPic']
        self._bad_field_list = ['BadRecord', 'Isbadrecord']
        self.edit_badrecord = 'labor_badrecord_edit'
        self.bad_list = ['正常', '不良', '黑名单']

    def get_insert_sql(self, args):
        field_str = []
        value_str = []
        if self.edit_badrecord in session['Permission']:
            field_str.append(' userid ')
            value_str.append(r""" '{}' """.format(self._uid))
            self._insert_list += self._bad_field_list
        if args.get('DepartureDate', '') != '':
            field_str.append(' DepartureDate ')
            value_str.append(r""" '{}' """.format(args.get('DepartureDate', '')))
        for key in self._insert_list:
            field_str.append(' {} '.format(key))
            if isinstance(args.get(key), int):
                value_str.append(r""" {} """.format(args.get(key, '')))
            else:
                value_str.append(r""" '{}' """.format(args.get(key, '')))
        return ','.join(field_str), ','.join(value_str)

    def chech_badrecord_info(self, args):
        query_sql = r"""select t1.Name, t1.Isbadrecord, t1.BadRecord, t1.IDCard, t2.LoginName from tb_laborinfo as t1
                        left join tb_user as t2 on t1.userid = t2.id
                        where t1.IDCard = '{}' and t1.isbadrecord > 0;""".format(args.get('IDCard'))
        result = self._db.query(query_sql)
        msg = ''
        if result:
            for item in result:
                temp_msg = r"""{}曾有不良劳务信息，被{}账号列为{}人员。\n""".format(
                    item['Name'], item['LoginName'], self.bad_list[int(item['Isbadrecord'])]
                )
                msg += temp_msg
            self.success = {'code': 50029, 'msg': msg}

    def views(self):
        args = self.args
        for key in args.keys():
            if args.get(key) == 'undefined':
                args[key] = ''
        isnull = self.args_is_null('ProjectID', 'Name', 'PID', 'CID', 'DID', 'IDCard', 'Nationality', 'Sex', 'ClassID',
                                   'IssueAuth', 'CompanyId', 'Birthday', 'Address', 'EntryDate', 'isFeeStand',
                                   'SubCompany')
        if args.get('isPM') == 'false':
            args['isPM'] = 0
        else:
            args['isPM'] = 1
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        if self.args.get('IsLeader') == 'false' and self.args.get('ClassID') == '0':
            return jsonify(status_code.CLASS_ID_NULL)
        if len(args.get('IDCard')) != 18:
            return jsonify(status_code.LABOR_IDCARD_ERROR)
        self.chech_badrecord_info(args)
        args['Birthday'] = str_to_date(args['Birthday'])
        args['EntryDate'] = str_to_date(args['EntryDate'])
        if args['DepartureDate'] != '':
            args['DepartureDate'] = str_to_date(args['DepartureDate'])
            if args['DepartureDate'] < args['EntryDate']:
                return jsonify(status_code.LABOR_TIME_ERROR)
        # args['CreateTime'] = self.time_format(args[''])
        # args['SVP'] = str_to_date(args['SVP'])
        # args['EVP'] = str_to_date(args['EVP'])
        args['Age'] = datetime.datetime.now().year - args['Birthday'].year
        query_sql = "select id from tb_laborinfo where IDCard = '{}';".format(args.get('IDCard'))
        result = self._db.query(query_sql)
        if result:
            return jsonify(status_code.LABOR_IS_EXISTS)
        args['CreateTime'] = datetime.datetime.now()
        for i in ('IDP', 'IDB', 'CloseupPhoto', 'Avatar', 'TrainPic'):
            temp_img = request.files.get(i, '')
            args[i] = ''
            if temp_img != '':
                args[i] = save_image(temp_img, 'static/media/labor')
        # bad_list = []
        # if bad_list:
        #     args['BadRecord'] = dumps(bad_list)
        # else:
        #     args['BadRecord'] = '0'
        if args.get('IsLeader', '') == 'true':
            if self.args_is_null('classname'):
                return jsonify(status_code.CONTENT_IS_NULL)
            create_class = r"""insert into tb_class(companyid, classname, projectid) 
                value ({},'{}', {})""".format(args.get('CompanyId'), args.get('classname'), args.get('ProjectID'))
            class_id = self._db.insert(create_class)
            args['ClassID'] = class_id
        else:
            # query_class = r"""select ClassID from tb_laborinfo where id={};""".format(args.get('SuperiorsID'))
            # class_result = self._db.query(query_class)
            # args['ClassID'] = class_result[0]['ClassID']
            args['ClassID'] = args.get('ClassID')
        args['Identity'] = 0
        # print(args)
        # if args.get('DepartureDate', '') == '':
        #     insert_sql = r"""insert into tb_laborinfo(Name, Age,Sex,Birthday,Address, Nationality,IDCard,Phone,CompanyID,
        #                               JobType, ClassID, Identity,EntryDate,Hardhatnum,Education,CreateTime,
        #                             ProjectID,IsPM,IssueAuth,Political,Train,EmerCon,IDP,IDB,PID,CID,DID,Superiors,IsLeader,
        #                              CloseupPhoto,Remark, BadRecord, FeeStand, Avatar, isFeeStand,isbadrecord,SubCompany)
        #                              value ('{Name}',{Age},{Sex},'{Birthday}','{Address}','{Nationality}','{IDCard}','{Phone}',
        #                              {CompanyID},{JobType},{ClassID},{Identity},'{EntryDate}','{Hardhatnum}',
        #                              '{Education}','{CreateTime}',{ProjectID},{IsPM},'{IssueAuth}','{Political}',
        #                              '{Train}','{EmerCon}','{IDP}','{IDB}',{PID},{CID},{DID},{SuperiorsID},{IsLeader},
        #                              '{CloseupPhoto}','{Remark}','{BadRecord}','{FeeStand}', '{Avatar}',
        #                              {isFeeStand},'{BadRecord}','{SubCompany}')""".format(
        #         **args)
        # else:
        #     insert_sql = r"""insert into tb_laborinfo(Name, Age,Sex,Birthday,Address, Nationality,IDCard,Phone,CompanyID,
        #                   JobType, ClassID, Identity, DepartureDate,EntryDate,Hardhatnum,Education,CreateTime,
        #                 ProjectID,IsPM,IssueAuth,Political,Train,EmerCon,IDP,IDB,PID,CID,DID,Superiors,IsLeader,
        #                  CloseupPhoto,Remark, BadRecord, FeeStand, Avatar, isFeeStand,isbadrecord,SubCompany)
        #                  value ('{Name}',{Age},{Sex},'{Birthday}','{Address}','{Nationality}','{IDCard}','{Phone}',
        #                  {CompanyID},{JobType},{ClassID},{Identity},'{DepartureDate}','{EntryDate}','{Hardhatnum}',
        #                  '{Education}','{CreateTime}',{ProjectID},{IsPM},'{IssueAuth}','{Political}',
        #                  '{Train}','{EmerCon}','{IDP}','{IDB}',{PID},{CID},{DID},{SuperiorsID},{IsLeader},
        #                  '{CloseupPhoto}','{Remark}','{BadRecord}','{FeeStand}', '{Avatar}',
        #                  {isFeeStand},'{BadRecord}','{SubCompany}')""".format(
        #         **args)
        args['Superiors'] = args['SuperiorsID']
        args['IsPM'] = 1 if args['IsPM'] == 'true' else 0
        args['IsLeader'] = 1 if args['IsLeader'] == 'true' else 0
        args['Train'] = 0 if args['Train'] == '' else args['Train']
        args['Isbadrecord'] = 0 if args['Isbadrecord'] == '' else args['Isbadrecord']
        insert_sql = r"""insert into tb_laborinfo({}) value ({})""".format(*self.get_insert_sql(args))
        lid = self._db.insert(insert_sql)
        update_pic_and_group('tb_pic_group', lid, args.get('group_list'), self._db)
        # update_pic_and_group('tb_pics', lid, args.get('Img_list'), self._db)
        self.success['ID'] = lid
        self.success['Name'] = args.get('Name')
        return jsonify(self.success)


class CreateLaborPicGroup(CreatePicGroup):
    """
    创建劳工图片分组
    """

    def __init__(self):
        super(CreateLaborPicGroup, self).__init__()
        self.dir = 'labor/'
        self.ptype = 2
        self.db_dir = '/static/media/' + self.dir


class CreateClass(LaborBase):

    def __init__(self):
        super(CreateClass, self).__init__()

    def views(self):
        return jsonify(status_code.SUCCESS)


class UpdateLabor(LaborBase):
    """更新劳工信息"""

    def __init__(self):
        super(UpdateLabor, self).__init__()
        self.api_permission = 'labor_edit'
        self._insert_list = ['Name', 'Age', 'Sex', 'Birthday', 'Address', 'Nationality', 'IDCard', 'Phone',
                             'CompanyID', 'JobType', 'ClassID', 'Identity', 'EntryDate', 'Hardhatnum',
                             'Education', 'CreateTime', 'ProjectID', 'IsPM', 'IssueAuth', 'Political',
                             'Train', 'EmerCon', 'IDP', 'IDB', 'PID', 'CID', 'DID', 'CompanyId', 'IsLeader',
                             'CloseupPhoto', 'Remark', 'FeeStand', 'Avatar',
                             'isFeeStand', 'SubCompany', 'TrainPic']
        self._bad_field_list = ['BadRecord', 'Isbadrecord']
        self.edit_badrecord = 'labor_badrecord_edit'
        self.bad_list = ['正常', '不良', '黑名单']

    def get_update_sql(self, args):
        value_str = []
        if self.edit_badrecord in session['Permission']:
            value_str.append(r""" userid={} """.format(self._uid))
            self._insert_list += self._bad_field_list
        if args.get('DepartureDate', '') != '':
            value_str.append(r""" DepartureDate='{}' """.format(args.get('DepartureDate', '')))
        for key in self._insert_list:
            if key in ('IDP', 'IDB', 'CloseupPhoto', 'Avatar', 'TrainPic'):
                if key not in args.keys():
                    continue
                if args.get(key) == '':
                    continue
            if isinstance(args.get(key), int):
                value_str.append(r""" {}={} """.format(key, args.get(key)))
            else:
                value_str.append(r""" {} = '{}' """.format(key, args.get(key)))
        return ','.join(value_str)

    def chech_badrecord_info(self, args):
        query_sql = r"""select t1.Name, t1.Isbadrecord, t1.BadRecord, t1.IDCard, t2.LoginName from tb_laborinfo as t1
                                left join tb_user as t2 on t1.userid = t2.id
                                where t1.IDCard = '{}' and t1.isbadrecord > 0;""".format(args.get('IDCard'))
        result = self._db.query(query_sql)
        msg = ''
        if result:
            for item in result:
                temp_msg = r"""{}曾有不良劳务信息，被{}账号列为{}人员。""".format(
                    item['Name'], item['LoginName'], self.bad_list[int(item['Isbadrecord'])]
                )
                msg += temp_msg
            self.success = {'code': 0, 'msg': msg}

    def check_class_change(self):
        query_sql = r"""select t2.id,t1.isleader,t2.classname, t1.superiors from tb_laborinfo as t1
                        left join tb_class as t2 on t1.classid = t2.id
                        where t1.id = {};
                        """.format(self.args['ID'])
        result = self._db.query(query_sql)
        if result:
            return result
        return None

    def views(self):
        args = self.args
        for key in args.keys():
            if args.get(key) == 'undefined':
                args[key] = ''
        isnull = self.args_is_null('ProjectID', 'Name', 'PID', 'CID', 'DID', 'IDCard', 'Nationality', 'Sex', 'IsPM',
                                   'IssueAuth', 'CompanyId', 'Birthday', 'Address', 'EntryDate', 'isFeeStand',
                                   'SubCompany')
        # if args.get('IsPM') == 'false':
        #     args['IsPM'] = 0
        # else:
        #     args['IsPM'] = 1
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        if args.get('SubCompany') == '0' or args.get('CompanyId') == '0':
            return jsonify(status_code.SubcompanyID_ID_NULL)
        if len(args.get('IDCard')) != 18:
            return jsonify(status_code.LABOR_IDCARD_ERROR)
        self.chech_badrecord_info(args)
        args['Birthday'] = str_to_date(args['Birthday'])
        args['Age'] = datetime.datetime.now().year - args['Birthday'].year
        args['EntryDate'] = str_to_date(args['EntryDate'])
        if args['DepartureDate'] != '':
            args['DepartureDate'] = str_to_date(args['DepartureDate'])
            if args['DepartureDate'] < args['EntryDate']:
                return jsonify(status_code.LABOR_TIME_ERROR)
        # args['CreateTime'] = str_to_date(args[''])
        # args['SVP'] = str_to_date(args['SVP'])
        # args['EVP'] = str_to_date(args['EVP'])
        for i in ('IDP', 'IDB', 'CloseupPhoto', 'Avatar', 'TrainPic'):
            temp_img = request.files.get(i, '')
            if temp_img != '':
                args[i] = save_image(temp_img, 'static/media/labor')
        # idp_img = request.files.get('IDP', '')
        # if idp_img != '':
        #     args['IDP'] = save_image(idp_img, 'static/media/labor')
        # idp_img = request.files.get('IDB', '')
        # if idp_img != '':
        #     args['IDB'] = save_image(idp_img, 'static/media/labor')
        # idp_img = request.files.get('CloseupPhoto', '')
        # if idp_img != '':
        #     args['CloseupPhoto'] = save_image(idp_img, 'static/media/labor')
        # idp_img = request.files.get('TrainPic', '')
        # if idp_img != '':
        #     args['TrainPic'] = save_image(idp_img, 'static/media/labor')
        # bad_list = []
        # for item in request.files.get('BadRecord'):
        #     img_file = item['file']
        #     img_url = save_image(img_file, 'static/medis/labor')
        #     item['file'] = img_url
        #     bad_list.append(item)
        # if bad_list:
        #     args['BadRecord'] = dumps(bad_list)
        # else:
        #     args['BadRecord'] = '0'
        check_class = self.check_class_change()
        if args.get('IsLeader') == 'true':
            if self.args_is_null('classname'):
                return jsonify(status_code.CONTENT_IS_NULL)

            if check_class[0]['isleader'] == 0:
                if check_class[0]['superiors'] == int(args.get('SuperiorsID')):
                    return jsonify(status_code.SUPERIORS_ERROR)
                if check_class[0]['classname'] != self.args.get('classname'):
                    create_class = r"""insert into tb_class(companyid, classname, projectid) 
                                value ({},'{}', {})""".format(args.get('CompanyId'), args.get('classname'),
                                                              args.get('ProjectID'))
                    class_id = self._db.insert(create_class)
                    args['ClassID'] = class_id
                else:
                    update_sql = 'update tb_laborinfo set isleader = 0, superiors = {} where classid={} and isleader=1;'.format(
                        self.args.get('ID'), check_class[0]['id']
                    )
                    self._db.update(update_sql)
                    update_others = r"""update tb_laborinfo set superiors={} where superiors={}""".format(
                        self.args.get('ID'), check_class[0]['superiors']
                    )
                    self._db.update(update_others)
            else:
                update_class = r"""update tb_class set classname='{}' where id={};""".format(
                    args.get('classname'), check_class[0]['id']
                )
                self._db.update(update_class)
                args['ClassID'] = check_class[0]['id']
            args['Superiors'] = args['SuperiorsID']
            del args['SuperiorsID']
        else:
            query_class = ''
            if self.args_is_null('ClassID'):
                return jsonify(status_code.CONTENT_IS_NULL)
            if check_class[0]['isleader'] != 0:
                if self.args_is_null('class_labors'):
                    return jsonify(status_code.CONTENT_IS_NULL)
                update_sql = r"""update tb_laborinfo set isleader = 1,superiors={} where id={};""".format(
                    check_class[0]['superiors'], self.args.get('class_labors'))
                self._db.update(update_sql)
                update_others = r"""update tb_laborinfo set superiors={} where superiors={};""".format(
                    self.args.get('class_labors'), self.args.get('ID')
                )
                self._db.update(update_others)
                query_class = r"""select Superiors from tb_laborinfo 
                                where classID={} and isleader=1 and id!={};""".format(
                    args.get('ClassID'), self.args.get('ID')
                )
                if int(self.args.get('ClassID')) == check_class[0]['id']:
                    args['Superiors'] = self.args.get('class_labors')
                else:
                    query_class = ''
                # if check_class[0]['classname'] != self.args.get('classname'):
                #     create_class = r"""insert into tb_class(companyid, classname, projectid)
                #                                     value ({},'{}', {})""".format(args.get('CompanyId'),
                #                                                                   args.get('classname'),
                #                                                                   args.get('ProjectID'))
                #     class_id = self._db.insert(create_class)
                #     args['ClassID'] = class_id
                # else:
                #     update_sql = r"""update tb_laborinfo set isleader = 0, superiors={}
                #                     where classid={} and isleader = 1;""".format(
                #         self.args.get('class_labors'), self.args.get('ClassID')
                #     )
                #     self._db.update(update_sql)

            if query_class == '':
                query_class = r"""select id from tb_laborinfo where classID={} and isleader=1;""".format(
                    args.get('ClassID'))
                class_result = self._db.query(query_class)
                args['Superiors'] = class_result[0]['id']

            del args['SuperiorsID']
        laborid = args['ID']
        del args['class_labors']
        del args['classname']
        del args['group_list']
        # del args['Img_list']
        del args['ID']
        if args.get('DepartureDate', '') == '':
            del args['DepartureDate']
        update_sql = r"""update tb_laborinfo set """
        for key in ('Avatar', 'IDP', 'IDB', 'CloseupPhoto'):
            if args[key] == '' or args[key] == 'undefined':
                del args[key]
        for key in ('IsPM', 'IsLeader'):
            if args[key] == 'true':
                args[key] = 1
            else:
                args[key] = 0
        for key in ('SVP', 'EVP'):
            if key in args.keys():
                del args[key]
        args['Train'] = 0 if args['Train'] == '' else args['Train']
        args['Isbadrecord'] = 0 if args['Isbadrecord'] == '' else args['Isbadrecord']
        args['userid'] = session['id']
        set_str = ''
        for index, item in enumerate(args.keys()):
            temp = ''
            if item == 'TrainPic' and args[item] == '':
                continue
            if isinstance(args[item], int):
                temp = str(item) + '=' + str(args[item])
            else:
                temp = str(item) + "='" + str(args[item]) + "'"
            if index < len(args.keys()) - 1:
                temp += ','
            set_str += temp

        # set_str = self.get_update_sql(args)
        update_sql = update_sql + set_str + ' where id={}'.format(laborid)
        self._db.update(update_sql)
        self.success['ID'] = laborid
        self.success['Name'] = args.get('Name')
        return jsonify(self.success)


class DeleteLabor(LaborBase):

    def __init__(self):
        super(DeleteLabor, self).__init__()

    def views(self):
        return jsonify(status_code.SUCCESS)


class QueryLabor(LaborBase):

    def __init__(self):
        super(QueryLabor, self).__init__()
        self.api_permission = 'labor_show'

    def admin(self):
        """以项目ID为基准"""
        # query_sql = r"""select ID from tb_project where DID in ({})""".format(self.get_session_ids())
        # self.ids = self.set_ids(query_sql)
        self.ids = self.get_project_ids()
        return self.views()

    def views(self):
        args = self.args
        query_sql_base = r"""select SQL_CALC_FOUND_ROWS t1.*, t2.ClassName as ClassName, t3.Name as ProjectName, t4.Name as CompanyName, t5.Name as PName, t6.Name as CName, t7.Name as DName from tb_laborinfo as t1
                            left join tb_class as t2 on t1.ClassID = t2.id
                            left join tb_project as t3 on t1.projectid = t3.id
                            left join tb_company as t4 on t1.CompanyID = t4.id
                            left JOIN tb_area as t5 on t5.ID = t1.PID
                            left JOIN tb_area as t6 on t6.ID = t1.CID
                            left JOIN tb_area as t7 on t7.ID = t1.DID"""
        where_sql_list = []
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            where_sql_list.append(r""" t1.projectid in ({}) """.format(self.to_sql_where_id()))
        if args.get('ProjectName', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t3.Name,'')) LIKE '%{}%' """.format(args.get('ProjectName')))
        if args.get('CompanyName', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t4.Name,'')) LIKE '%{}%' """.format(args.get('CompanyName')))
        if int(args.get('DID', 0)) != 0:
            where_sql_list.append(r""" t1.DID={} """.format(args.get('DID')))
        if int(args.get('CID', 0)) != 0:
            where_sql_list.append(r""" t1.CID={} """.format(args.get('CID')))
        if int(args.get('PID', 0)) != 0:
            where_sql_list.append(r""" t1.PID={} """.format(args.get('PID')))
        if int(args.get('Age', 6)) != 6:
            if int(args.get('Age', 0)) == 0:
                where_sql_list.append(r""" t1.Age<18 """)
            if int(args.get('Age', 0)) == 1:
                where_sql_list.append(r""" t1.Age>=18 and t1.Age<30  """)
            if int(args.get('Age', 0)) == 2:
                where_sql_list.append(r""" t1.Age>=30 and t1.Age<39  """)
            if int(args.get('Age', 0)) == 3:
                where_sql_list.append(r"""  t1.Age>=39 and t1.Age<49 """)
            if int(args.get('Age', 0)) == 4:
                where_sql_list.append(r"""  t1.Age>=49 and t1.Age<55  """)
            if int(args.get('Age', 0)) == 5:
                where_sql_list.append(r""" t1.Age>=55 """)
        if int(args.get('Isbad', 2)) == 1:
            where_sql_list.append(r""" t1.isBadRecord >= 1 """)
        elif int(args.get('Isbad', 2)) == 0:
            where_sql_list.append(r""" t1.isBadRecord = 0 """)
        else:
            pass
        if args.get('Name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('Name')))
        if args.get('IDCard', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.IDCard,''))='{}' """.format(args.get('IDCard')))
        if int(args.get('Sex', 2)) != 2:
            where_sql_list.append(r""" t1.Sex={} """.format(args.get('Sex')))
        if int(args.get('JobType', 5)) != 5:
            where_sql_list.append(r""" t1.JobType='{}' """.format(int(args.get('JobType'))))
        if int(args.get('Education', 7)) != 7:
            where_sql_list.append(r""" t1.Education='{}' """.format(int(args.get('Education'))))
        # 按照管理员，班组长，普通人员查询
        if args.get('queryType', 0) != 0:
            queryType = str(args.get('queryType'))
            if queryType == '1':
                where_sql_list.append(r""" t1.isPM = 1""")
            elif queryType == '2':
                where_sql_list.append(r""" t1.IsLeader = 1""")
            elif queryType == '3':
                where_sql_list.append(r""" t1.isPM != 1 """)
                where_sql_list.append(r""" t1.IsLeader != 1""")
        temp = ''
        if where_sql_list:
            temp = ' where '
            for index, i in enumerate(where_sql_list):
                temp += i
                if index < len(where_sql_list) - 1:
                    temp += 'and'
        if int(args.get('export', '0')) == 0:
            page = int(args.get('Page', 1))
            psize = int(args.get('PageSize', 10))
            limit_sql = r""" limit {},{};""".format((page - 1) * psize, psize)
            query_sql = query_sql_base + " " + temp + limit_sql
        else:
            query_sql = query_sql_base + ' ' + temp
        # print(query_sql)
        result = self._db.query(query_sql)
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        labors = []
        for item in result:
            item['isDeparture'] = False
            for i in ('Birthday', 'DepartureDate', 'EntryDate', 'CreateTime', 'SVP', 'EVP'):
                if item[i] != None:
                    if (i == 'DepartureDate') and (item[i] < datetime.datetime.now()):
                        item['isDeparture'] = True
                    item[i] = item[i].strftime("%Y-%m-%d")
            if item['Avatar'] is None:
                item['Avatar'] = ''
            # item['BadRecord'] = loads(item['BadRecord'])
            # print(item['BadRecord'])
            labors.append(deepcopy(item))
        if int(args.get('export', '0')) == 0:
            success = deepcopy(status_code.SUCCESS)
            success['labor_list'] = labors
            success['total'] = total[0]['total_row']
            return jsonify(success)
        else:
            return self.export_file('labor', labors)


class LaborInfo(LaborBase):

    def __init__(self):
        super(LaborInfo, self).__init__()
        self.api_permission = 'labor_show'

    def get_all_class_labor(self):
        query_sql = r"""select id, name from tb_laborinfo 
                        where classID = (
                            select classid from tb_laborinfo where id= {0}
                        ) and id != {0};""".format(self.args.get('ID'))
        return self._db.query(query_sql)

    def views(self):
        args = self.args
        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select t1.*, t2.ClassName as ClassName, t3.Name as ProjectName, t4.Name as CompanyName, t5.Name as PName, t6.Name as CName, t7.Name as DName, t8.name as SuperiorsName, t9.Name as SubCompanyName from tb_laborinfo as t1
                        left join tb_class as t2 on t1.ClassID = t2.id
                        left join tb_project as t3 on t1.projectid = t3.id
                        left join tb_company as t4 on t1.CompanyID = t4.id
                        left JOIN tb_area as t5 on t5.ID = t1.PID
                        left JOIN tb_area as t6 on t6.ID = t1.CID
                        left JOIN tb_area as t7 on t7.ID = t1.DID
                        left join tb_laborinfo as t8 on t8.id = t1.Superiors
						left join tb_company as t9 on t9.id = t1.SubCompany
                        where t1.id = {};""".format(args.get('ID'))
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.LABOR_IS_NOT_EXISTS)
        labor_info = result[0]
        query_pic_group = r"""select * from tb_pic_group where cid={} and ptype=2;""".format(args.get('ID'))
        pic_group = self._db.query(query_pic_group)
        pic_group_dict = {
            'bad_list': [],
            'info': []
        }
        for item in pic_group:
            if int(item['Type']) == 0:
                pic_group_dict['bad_list'].append(item)
            else:
                pic_group_dict['info'].append(item)
        # labor_info['BadRecord'] = loads(labor_info['BadRecord'])
        # labor_info['Birthday'] = self.time_to_str(labor_info['Birthday'])
        labor_info['isDeparture'] = False
        for i in ('Birthday', 'DepartureDate', 'EntryDate', 'CreateTime'):
            if labor_info[i] != None and labor_info[i] != '':
                if i == 'DepartureDate' and labor_info[i] < datetime.datetime.now():
                    labor_info['isDeparture'] = True
                labor_info[i] = labor_info[i].strftime("%Y-%m-%d")
        success = deepcopy(status_code.SUCCESS)
        success['labor'] = labor_info
        success['labor']['pic_group'] = pic_group_dict
        success['class_labors'] = self.get_all_class_labor()
        return jsonify(success)


class UploadLaborImg(LaborBase):

    def __init__(self):
        super(UploadLaborImg, self).__init__()

    def save_more_img(self, ptype, r_type, img_dir, file_list):
        result_file_list = []
        for one_file in file_list:
            try:
                iamge_url = save_image(one_file, img_dir)
                insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type) 
                                        value ({},'{}', '{}', {},{})""".format(self.args['GID'], iamge_url,
                                                                               one_file.filename[:-4],
                                                                               ptype, r_type)
                pid = self._db.insert(insert_sql)
                temp = {'id': pid, 'name': one_file.filename[:-4], 'url': iamge_url, 'Purl': iamge_url}
                result_file_list.append(deepcopy(temp))
            except:
                continue
        return result_file_list

    def views(self):
        args = self.args
        query_sql = r"""select gurl,type,ptype from tb_pic_group 
                                where id={}""".format(args.get('GID'))
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.DIR_NOT_EXISTS)
        temp_img_dir = result[0]['gurl'][1:]
        image_file = request.files.getlist('file')
        if image_file == [] or image_file == '':
            return jsonify(status_code.FILE_NOT_EXISTS)
        # iamge_url = save_image(image_file, temp_img_dir)
        # insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type)
        #                         value ({},'{}', '{}', {},{})""".format(self.args['GID'], iamge_url,
        #                                                                image_file.filename[:-4],
        #                                                                result[0]['ptype'], result[0]['type'])
        # pid = self._db.insert(insert_sql)
        result = self.save_more_img(result[0]['ptype'], result[0]['type'], temp_img_dir, image_file)
        success = deepcopy(status_code.SUCCESS)
        success['data'] = result
        # success['id'] = pid
        # success['name'] = image_file.filename[:-4]
        # success['url'] = iamge_url
        return jsonify(success)


class AllLabor(AllCompanyID):

    def __init__(self):
        super(AllLabor, self).__init__()
        self.table = 'tb_laborinfo'

    def admin(self):
        """以项目ID为基准"""
        query_sql = r"""select ID from tb_project where DID in ({})""".format(self.get_session_ids())
        self.ids = self.set_ids(query_sql)
        return self.views()

    def get_query_sql(self):
        query_sql = r"""select ID,Name from {} """.format(self.table)
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            query_sql += """ where ProjectID in ({}) """.format(self.to_sql_where_id())
        return query_sql


class GetAllLaborLeader(LaborBase):

    def __init__(self):
        super(GetAllLaborLeader, self).__init__()

    def views(self):
        args = self.args
        query_sql = r"""select t1.ClassName,t1.ID as ClassID, t2.Name as SuperiorsName, t2.ID as SuperiorsID from tb_class as t1
            LEFT JOIN tb_laborinfo as t2 on t1.ProjectID = t2.ProjectID and t2.IsLeader = 1 
            where t1.ProjectID={}""".format(int(args.get('ProjectID')))
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['labor_group_info'] = result
        return jsonify(success)


class GetOnePAllL(LaborBase):

    def __init__(self):
        super(GetOnePAllL, self).__init__()

    def views(self):
        if self.args_is_null('projectid'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select id,name,avatar from tb_laborinfo where projectid = {};""".format(
            self.args.get('projectid'))
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['data'] = result
        return jsonify(success)
