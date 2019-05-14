import datetime
from copy import deepcopy
from json import dumps, loads

from flask import jsonify, request

from Company.utils import update_pic_and_group
from Company.views import CreatePicGroup
from User.util import save_image
from utils import status_code
from utils.BaseView import BaseView


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

    def views(self):
        args = self.args
        args['Birthday'] = self.time_format(args['Birthday'])
        args['DepartureDate'] = self.time_format(args['DepartureDate'])
        args['EntryDate'] = self.time_format(args['EntryDate'])
        args['CreateTime'] = self.time_format(args[''])
        args['SVP'] = self.time_format(args['SVP'])
        args['EVP'] = self.time_format(args['EVP'])
        isnull = self.args_is_null('ProjectID', 'Name', 'PID', 'CID', 'DID', 'IDCard', 'Nationality', 'Sex', 'IsPM',
                                   'IssueAuth', 'CompanyID', 'Birthday', 'Address')
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = "select id from tb_laborinfo where IDCard = '{}';".format(args.get('IDCard'))
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.LABOR_IS_EXISTS)
        args['CreateTime'] = datetime.datetime.now()
        idp_img = request.files.get('IDP', '')
        if idp_img != '':
            args['IDP'] = save_image(idp_img, 'static/media/labor')
        idp_img = request.files.get('IDB', '')
        if idp_img != '':
            args['IDB'] = save_image(idp_img, 'static/media/labor')
        idp_img = request.files.get('CloseupPhoto', '')
        if idp_img != '':
            args['CloseupPhoto'] = save_image(idp_img, 'static/media/labor')
        idp_img = request.files.get('Train', '')
        if idp_img != '':
            args['Train'] = save_image(idp_img, 'static/media/labor')
        bad_list = []
        for item in request.files.get('BadRecord'):
            img_file = item['file']
            img_url = save_image(img_file, 'static/medis/labor')
            item['file'] = img_url
            bad_list.append(item)
        if bad_list:
            args['BadRecord'] = dumps(bad_list)
        else:
            args['BadRecord'] = '0'
        if args.get('IsLeader', False):
            create_class = r"""insert into tb_class(companyid, classname, projectid) 
                value ({},'{}', {})""".format(args.get('CompanyID'), args.get('classname'), args.get('ProjectID'))
            class_id = self._db.insert(create_class)
            args['ClassID'] = class_id
        insert_sql = r"""insert into tb_laborinfo(Name, Age,Sex,Birthday,Address, Nationality,IDCard,Phone,CompanyID,
                          JobType, ClassID, Identity, DepartureDate,EntryDate,Hardhatnum,Education,CreateTime,
                        ProjectID,IsPM,IssueAuth,Political,Train,EmerCon,IDP,IDB,PID,CID,DID,SVP,EVP,Superiors,IsLeader,
                         CloseupPhoto,Remark, BadRecord)
                         value ('{Name}',{Age},{Sex},'{Birthday}','{Address}','{Nationality}','{IDCard}','{Phone}',
                         {CompanyID},'{JobType}',{ClassID},{Identity},'{DepartureDate}','{EntryDate}','{Hardhatnum}',
                         '{Education}','{CreateTime}',{ProjectID},{IsPM},'{IssueAuth}','{Political}',
                         '{Train}','{EmerCon}','{IDP}','{IDB}',{PID},{CID},{DID},'{SVP}','{EVP}',{Superiors},{IsLeader},
                         '{CloseupPhoto}','{Remark}','{BadRecord}')""".format(**args)
        lid = self._db.query(insert_sql)
        update_pic_and_group('tb_pic_group', lid, args.get('Group_list'), self._db)
        update_pic_and_group('tb_pics', lid, args.get('Img_list'), self._db)
        return jsonify(status_code.SUCCESS)


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

    def views(self):
        args = self.args
        args['Birthday'] = self.time_format(args['Birthday'])
        args['DepartureDate'] = self.time_format(args['DepartureDate'])
        args['EntryDate'] = self.time_format(args['EntryDate'])
        args['CreateTime'] = self.time_format(args[''])
        args['SVP'] = self.time_format(args['SVP'])
        args['EVP'] = self.time_format(args['EVP'])
        isnull = self.args_is_null('ProjectID', 'Name', 'PID', 'CID', 'DID', 'IDCard', 'Nationality', 'Sex', 'IsPM',
                                   'IssueAuth', 'CompanyID', 'Birthday', 'Address')
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        idp_img = request.files.get('IDP', '')
        if idp_img != '':
            args['IDP'] = save_image(idp_img, 'static/media/labor')
        idp_img = request.files.get('IDB', '')
        if idp_img != '':
            args['IDB'] = save_image(idp_img, 'static/media/labor')
        idp_img = request.files.get('CloseupPhoto', '')
        if idp_img != '':
            args['CloseupPhoto'] = save_image(idp_img, 'static/media/labor')
        idp_img = request.files.get('Train', '')
        if idp_img != '':
            args['Train'] = save_image(idp_img, 'static/media/labor')
        bad_list = []
        for item in request.files.get('BadRecord'):
            img_file = item['file']
            img_url = save_image(img_file, 'static/medis/labor')
            item['file'] = img_url
            bad_list.append(item)
        if bad_list:
            args['BadRecord'] = dumps(bad_list)
        else:
            args['BadRecord'] = '0'
        if args.get('IsLeader', False):
            create_class = r"""insert into tb_class(companyid, classname, projectid) 
                        value ({},'{}', {})""".format(args.get('CompanyID'), args.get('classname'),
                                                      args.get('ProjectID'))
            class_id = self._db.insert(create_class)
            args['ClassID'] = class_id
        laborid = args['ID']
        del args['classname']
        del args['Group_list']
        del args['Img_list']
        del args['ID']
        update_sql = r"""update tb_laborinfo set """
        set_str = ''
        for index, item in enumerate(args):
            temp = ''
            if isinstance(item[1], int):
                temp = str(item[0]) + '=' + str(item[1])
            else:
                temp = str(item[0]) + "='" + str(item[1]) + "'"
            if index < len(args.keys()) - 1:
                temp += ','
            set_str += temp
        update_sql = update_sql + set_str + ' where id={}'.format(laborid)
        self._db.update(update_sql)
        return jsonify(status_code.SUCCESS)


class DeleteLabor(LaborBase):

    def __init__(self):
        super(DeleteLabor, self).__init__()

    def views(self):
        return jsonify(status_code.SUCCESS)


class QueryLabor(LaborBase):

    def __init__(self):
        super(QueryLabor, self).__init__()

    def admin(self):
        """以项目ID为基准"""
        query_sql = r"""select ID from tb_project where DID in ({})""".format(self.get_session_ids())
        self.ids = self.set_ids(query_sql)
        return self.views()

    def views(self):
        args = self.args
        query_sql_base = r"""select t1.*, t2.ClassName as ClassName, t3.Name as ProjectName, t4.Name as CompanyName from 
                                tb_laborinfo as t1
                                left join tb_class as t2 on t1.ClassID = t2.id
                                left join tb_project as t3 on t1.projectid = t3.id
                                left join tb_company as t4 on t1.CompanyID = t4.id"""
        where_sql_list = []
        if self.ids:
            where_sql_list.append(r""" t1.projectid in ({}) """.format(self.to_sql_where_id()))
        if args.get('ProjectName', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t3.Name,'')) LIKE '%{}%' """.format(args.get('ProjectName')))
        if args.get('CompanyName', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t4.Name,'')) LIKE '%{}%' """.format(args.get('CompanyName')))
        if int(args.get('DID', 0)):
            where_sql_list.append(r""" t1.DID={} """.format(args.get('DID')))
        if int(args.get('CID', 0)):
            where_sql_list.append(r""" t1.CID={} """.format(args.get('CID')))
        if int(args.get('PID', 0)):
            where_sql_list.append(r""" t1.PID={} """.format(args.get('PID')))
        if int(args.get('Isbad', 0)):
            where_sql_list.append(r""" t1.BadRecord != '0' """)
        if args.get('Name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('Name')))
        if args.get('IDCard', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.IDCard,''))='{}' """.format(args.get('IDCard')))
        if int(args.get('Sex', 2)) != 2:
            where_sql_list.append(r""" t1.Sex={} """.format(args.get('Sex')))
        if args.get('JobType', '') != '':
            where_sql_list.append(r""" t1.JobType='{}' """.format(args.get('JobType')))
        if args.get('Education', '') != '':
            where_sql_list.append(r""" t1.Education='{}' """.format(args.get('Education')))
        temp = ' where '
        for index, i in enumerate(where_sql_list):
            temp += i
            if index < len(where_sql_list) - 1:
                temp += 'and'
        page = int(args.get('Page', 1))
        psize = int(args.get('PageSize', 10))
        limit_sql = r""" limit {},{};""".format((page - 1) * psize, psize)
        query_sql = query_sql_base + " " + temp + limit_sql
        result = self._db.query(query_sql)
        labors = []
        for item in result:
            for i in ('Birthday', 'DepartureDate', 'EntryDate', 'CreateTime', 'SVP', 'EVP'):
                item[i] = self.time_to_str(item[i])
            item['BadRecord'] = loads(item['BadRecord'])
            labors.append(item)
        success = deepcopy(status_code.SUCCESS)
        success['labor_list'] = labors
        return jsonify(success)


class LaborInfo(LaborBase):

    def __init__(self):
        super(LaborInfo, self).__init__()

    def views(self):
        args = self.args
        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select t1.*, t2.ClassName as ClassName, t3.Name as ProjectName, t4.Name as CompanyName from 
                        tb_laborinfo as t1
                        left join tb_class as t2 on t1.ClassID = t2.id
                        left join tb_project as t3 on t1.projectid = t3.id
                        left join tb_company as t4 on t1.CompanyID = t4.id
                        where t1.id = {};""".format(args.get('ID'))
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.LABOR_IS_NOT_EXISTS)
        labor_info = result[0]
        query_pic_group = r"""select * from tb_pic_group where cid={} and ptype=2;""".format(args.get('ID'))
        pic_group = self._db.query(query_pic_group)
        labor_info['BadRecord'] = loads(labor_info['BadRecord'])
        # labor_info['Birthday'] = self.time_to_str(labor_info['Birthday'])
        for i in ('Birthday', 'DepartureDate', 'EntryDate', 'CreateTime', 'SVP', 'EVP'):
            labor_info[i] = self.time_to_str(labor_info[i])
        success = deepcopy(status_code.SUCCESS)
        success['labor'] = labor_info
        success['labor']['pic_group'] = pic_group
        return jsonify(success)


class UploadLaborImg(LaborBase):

    def __init__(self):
        super(UploadLaborImg, self).__init__()

    def views(self):
        args = self.args
        query_sql = r"""select gurl,type,ptype from tb_pic_group 
                                where id={GID}""".format(args)
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.DIR_NOT_EXISTS)
        temp_img_dir = result[0]['gurl'][1:]
        image_file = request.files.get('file', None)
        if image_file is None:
            return jsonify(status_code.FILE_NOT_EXISTS)
        iamge_url = save_image(image_file, temp_img_dir)
        insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type) 
                                value ({},'{}', '{}', {},{})""".format(self.args['GID'], iamge_url,
                                                                       image_file.filename[:-4],
                                                                       result[0]['ptype'], result[0]['type'])
        pid = self._db.insert(insert_sql)
        success = deepcopy(status_code.SUCCESS)
        success['id'] = pid
        success['name'] = image_file.filename[:-4]
        success['url'] = iamge_url
        return jsonify(success)
