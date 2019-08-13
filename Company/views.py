from json import loads, dumps

import shutil
from copy import deepcopy

import os

import random
from flask import request, jsonify, session

from APP.settings import upload_dir, BASE_DIR
from Company.utils import create_random_str, update_pic_and_group
from User.util import save_image, save_other_file
from utils import status_code
from utils.BaseView import BaseView, DelteBase


class CreatePicGroup(BaseView):
    """
    创建分组接口，
    Gtype表示分组类型，0表示公司分组，1表示公司执照分组
    CID：公司ID,新建的时候创建分组为0
    """

    def __init__(self):
        super(CreatePicGroup, self).__init__()
        self.dir = 'company/'
        self.ptype = 0
        self.db_dir = '/static/media/' + self.dir

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def views(self):
        args = self.args
        select_sql = r"""select id from tb_pic_group where name='{Name}' and type={Gtype} and Cid ={CID} and ptype={0}""".format(
            self.ptype, **args)
        exists_result = self._db.query(select_sql)
        if exists_result:
            return jsonify(status_code.DATA_HAS_EXISTS)
        random_url = create_random_str(random.randint(4, 10))
        dir_path = os.path.join(upload_dir, self.dir + random_url)
        while os.path.exists(dir_path):
            random_url = create_random_str(random.randint(4, 10))
            dir_path = os.path.join(upload_dir, self.dir + random_url)
        os.makedirs(dir_path)
        # print(args)
        insert_group = r"""insert into tb_pic_group(Name,Type,Gurl, CID, Ptype) 
                                value ('{Name}', {Gtype}, '{0}',{CID}, {1})""".format(
            self.db_dir + random_url, self.ptype, **args)
        id = self._db.insert(insert_group)
        success = deepcopy(status_code.SUCCESS)
        success['isgroup'] = True
        success['id'] = id
        success['name'] = self.args['Name']
        return jsonify(success)


class DeletePicGroup(DelteBase):

    def __init__(self):
        super(DeletePicGroup, self).__init__()
        self.table_name = 'tb_pic_group'
        self.ptype = 0

    def views(self):
        ID = self.args.get('ID', None)
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        querysql = r"""select GUrl from {} where id={}""".format(self.table_name, ID)
        db_list = self._db.query(querysql)
        for item in db_list:
            shutil.rmtree(BASE_DIR + item['GUrl'])
        delete_pics = r"""delete from tb_pics where GroupID={}""".format(ID)
        self._db.delete(delete_pics)
        delete_sql = r"""delete from {} where id={}""".format(self.table_name, ID)
        self._db.delete(delete_sql)
        return jsonify(status_code.SUCCESS)


class DeletePic(DelteBase):
    """
    图片表，
    ptype分别用0,1,2表示企业，项目，劳工
    type:表示ptype下边的子类，例如资质图片为0， 执照图片为1，公司照片为2
    """

    def __init__(self):
        super(DeletePic, self).__init__()
        self.table_name = 'tb_pics'
        self.ptype = 0

    def views(self):
        ID = self.args.get('ID', None)
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        query_sql = r"""select purl from {} where id={};""".format(self.table_name, int(ID))
        pic_list = self._db.query(query_sql)
        for item in pic_list:
            os.remove(BASE_DIR + item['purl'])
        delete_sql = r"""delete from {} where id={};""".format(self.table_name, int(ID))
        self._db.delete(delete_sql)
        return jsonify(status_code.SUCCESS)


class GetGroupList(BaseView):
    """
    ptype:为012代表企业，项目，劳工
    type：企业中用1表示公司执照，0表示公司图片
    """

    def __init__(self):
        super(GetGroupList, self).__init__()
        self.ptype = 0

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def views(self):
        ID = self.args.get('CID')
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        query_sql = r"""select * from tb_pic_group where CID={} and Ptype = {}""".format(ID, self.ptype)
        result_list = self._db.query(query_sql)
        Lgroup_list = []
        group_list = []
        success = deepcopy(status_code.SUCCESS)
        for item in result_list:
            if item['Type']:
                Lgroup_list.append(item)
            else:
                group_list.append(item)
        success['Lgroup_list'] = Lgroup_list
        success['group_list'] = group_list
        return jsonify(success)


class GetGroupPicList(BaseView):

    def __init__(self):
        super(GetGroupPicList, self).__init__()
        self.ptype = 0

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def views(self):
        ID = self.args.get('ID')
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        query_sql = r"""select * from tb_pics where GroupID={}""".format(ID)
        result_list = self._db.query(query_sql)
        group_list = []
        success = deepcopy(status_code.SUCCESS)
        for item in result_list:
            group_list.append(item)
        success['pic_list'] = group_list
        return jsonify(success)


class GetCompanyList(BaseView):

    def __init__(self):
        super(GetCompanyList, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        # query_sql = r"""select t2.ID from tb_project as t1
        #                 LEFT JOIN tb_company as t2 on t1.Build = t2.id
        #                 LEFT JOIN tb_company as t3 on t1.Cons = t3.id
        #                 where t1.DID in ({})""".format(self.get_session_ids())
        # self.ids = self.set_ids(query_sql)
        return self.views()

    def guest(self):
        return self.admin()

    def views(self):
        args = self.args
        # print(args.get('Name'))
        for i in ('Name', 'PID', 'CID', 'DID', 'Page', 'PageSize'):
            temp = args.get(i, None)
            if temp == None:
                return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select SQL_CALC_FOUND_ROWS t1.*, t4.Name as ProName, t5.Name as CityName, t6.Name as DisName from tb_company as t1
                                LEFT JOIN tb_area as t4 on t1.ProvinceID = t4.id
                                LEFT JOIN tb_area as t5 on t1.CityID = t5.id
                                LEFT JOIN tb_area as t6 on t1.DistrictID = t6.id"""
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if args.get('Name', '') != '':
            if int(args.get('Type')) == 0:
                where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%'""".format(args.get('Name')))
            else:
                where_sql_list.append(r""" CONCAT(IFNULL(t1.Legal,'')) LIKE '%{}%'""".format(args.get('Name')))
        # print(query_sql)
        if int(args.get('PID', 0)):
            # args['PID'] = int(self.args['PID'])
            where_sql_list.append(' ProvinceID={} '.format(int(self.args['PID'])))
        if int(args.get('CID', 0)):
            # args['CID'] = int(self.args['CID'])
            where_sql_list.append('  CityID={} '.format(int(self.args['CID'])))
        if int(args.get('DID', 0)):
            # args['DID'] = int(self.args['DID'])
            where_sql_list.append('  DistrictID={} '.format(int(self.args['DID'])))
        if int(args.get('HasBadRecord', 0)) != 0:
            # args['HasBadRecord'] = int(args['HasBadRecord'])
            if int(args.get('HasBadRecord', 0)) == 2:
                where_sql_list.append(' HasBadRecord>={} '.format(args.get('HasBadRecord')))
            else:
                where_sql_list.append(' HasBadRecord={} '.format(args.get('HasBadRecord')))
        if self.ids:
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if where_sql_list:
            query_sql += ' where '
        for index, item in enumerate(where_sql_list):
            query_sql += item
            if index < len(where_sql_list) - 1:
                query_sql += ' and '
        query_sql += ' limit {0},{1};'
        start_limit = (int(args.get('Page', 1)) - 1) * int(args.get('PageSize'))
        query_sql = query_sql.format(start_limit, int(args.get('PageSize')), **args)
        # print(query_sql)
        result = self._db.query(query_sql)
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        success = deepcopy(status_code.SUCCESS)
        for item in result:
            item['Phone'] = loads(item['Phone'])

            # item['License'] = loads(item['License'])
        success['company_list'] = result
        success['total'] = total[0]['total_row']
        return jsonify(success)


class UploadPic(BaseView):
    """
    上传图片接口：
    返回上传图片ID，url,name
    新建时CID为0
    """

    def __init__(self):
        super(UploadPic, self).__init__()
        self.ptype = 0

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def save_more_img(self, r_type, img_dir, file_list):
        result_file_list = []
        for one_file in file_list:
            try:
                iamge_url = save_image(one_file, img_dir)
                insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type) 
                                        value ({},'{}', '{}', {},{})""".format(self.args['GID'], iamge_url,
                                                                               one_file.filename[:-4],
                                                                               self.ptype, r_type)
                pid = self._db.insert(insert_sql)
                temp = {'id': pid, 'name': one_file.filename[:-4], 'url': iamge_url}
                result_file_list.append(deepcopy(temp))
            except:
                continue
        return result_file_list

    def views(self):
        query_sql = r"""select gurl,type from tb_pic_group 
                        where id={GID} and cid={CID} and Ptype = {0}""".format(self.ptype, **self.args)
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.DIR_NOT_EXISTS)
        temp_img_dir = result[0]['gurl'][1:]
        image_file = request.files.getlist('file')
        if image_file == [] or image_file == '':
            return jsonify(status_code.FILE_NOT_EXISTS)
        # iamge_url = save_image(image_file, temp_img_dir)
        # insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type)
        #                 value ({},'{}', '{}', {},{})""".format(self.args['GID'], iamge_url, image_file.filename[:-4],
        #                                                        self.ptype, result[0]['type'])
        # id = self._db.insert(insert_sql)
        result = self.save_more_img(result[0]['type'], temp_img_dir, image_file)
        success = deepcopy(status_code.SUCCESS)
        success['data'] = result
        return jsonify(success)


class GetCompanyInfo(BaseView):

    def __init__(self):
        super(GetCompanyInfo, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def get_all_file(self, companyid, ptype):
        query_sql = r"""select * from tb_otherfile where companyid={} and type={}""".format(companyid, ptype)
        file_list = self._db.query(query_sql)
        return file_list

    def views(self):
        ID = self.args.get('ID')
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        query_sql = r"""select t1.ID, t1.Address, t1.BadRecord,t1.Description, t1.Legal, t1.License, t1.HasBadRecord,
                        t1.Name, t1.Phone, t1.Type,t1.url,t2.Name as ProvinceID, t3.Name as CityID, t4.Name as DistrictID, 
                        t1.ProvinceID as province, t1.CityID as city, t1.DistrictID as district from tb_company as t1
                        LEFT JOIN tb_area as t2 on t1.ProvinceID = t2.ID
                        LEFT JOIN tb_area as t3 on t1.CityID = t3.ID
                        LEFT JOIN tb_area as t4 on t1.DistrictID = t4.ID
                        where t1.id = {};""".format(ID)
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.GET_COMPANY_INFO_FAILD)
        result = result[0]
        result['Phone'] = loads(result['Phone'])
        result['other_file_list'] = self.get_all_file(result['ID'], 0)
        result['license_list'] = self.get_all_file(result['ID'], 1)
        # result['License'] = loads(result['License'])
        success = deepcopy(status_code.SUCCESS)
        success['company_info'] = result
        return jsonify(success)


class CreateCompany(BaseView):

    def __init__(self):
        super(CreateCompany, self).__init__()
        self.api_permission = 'company_edit'

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def insert_otherfile(self, companyid, file_list, ptype):
        dir_path = os.path.join(upload_dir, 'otherfile')
        while not os.path.exists(dir_path):
            os.makedirs(dir_path)
        insert_sql = 'insert into tb_otherfile(companyid, filename, filepath,type) values {}'
        temp = ''
        for index, one_file in enumerate(file_list):
            filename, filepath = save_other_file(one_file)
            temp += r"""({}, '{}', '{}', {})""".format(companyid, filename, filepath, ptype)
            if index < len(file_list) - 1:
                temp += ','
        if temp != '':
            self._db.insert(insert_sql.format(temp))

    def insert_license(self, companyid, file_list, ptype):
        dir_path = os.path.join(upload_dir, 'otherfile')
        while not os.path.exists(dir_path):
            os.makedirs(dir_path)
        insert_sql = 'insert into tb_otherfile(companyid, filename, filepath,type) values {}'
        temp = ''
        for index, one_file in enumerate(file_list):
            filepath = save_image(one_file, 'static/media/otherfile')
            temp += r"""({}, '{}', '{}', {})""".format(companyid, one_file.filename, filepath, ptype)
            if index < len(file_list) - 1:
                temp += ','
        if temp != '':
            self._db.insert(insert_sql.format(temp))

    def views(self):
        # self.args['Phone'] = dumps(self.args['Phone'])
        if self.args_is_null('Name', 'ProvinceID', 'CityID', 'DistrictID', 'Type', 'Legal', 'Address'):
            return jsonify(status_code.CONTENT_IS_NULL)
        if self.has_data('tb_company', 'name', self.args.get('Name'), None):
            return jsonify(status_code.DATA_HAS_EXISTS)
        # self.args['HasBadRecord'] = 2 if self.args['HasBadRecord'] == 'true' else 1
        # file_list = request.files.get('License', '')
        # file_img_url = ''
        # if file_list != '':
        #     if file_list == 'undefined':
        #         return jsonify(status_code.CONTENT_IS_NULL)
        #     if os.name == 'nt':
        #         file_img_url = save_image(file_list, r'static\\media\\company')
        #     else:
        #         file_img_url = save_image(file_list, 'static/media/company')
        # else:
        #     return jsonify(status_code.CONTENT_IS_NULL)
        # self.args['License'] = file_img_url
        # self.args['License'] = '[]'
        insert_sql = r"""insert into tb_company(Name, Legal,Address,Phone,License,Type,ProvinceID,CityID,DistrictID,
        HasBadRecord,Description) value ('{Name}','{Legal}','{Address}','{Phone}','0',{Type},
        {ProvinceID},{CityID},{DistrictID}, {HasBadRecord}, '{Description}')""".format(**self.args)
        cid = self._db.insert(insert_sql)
        update_pic_and_group('tb_pic_group', cid, self.args.get('group_list', []), self._db)
        if isinstance(request.files.getlist('otherfile[]'), list):
            self.insert_otherfile(cid, request.files.getlist('otherfile[]'), 0)
        if isinstance(request.files.getlist('License[]'), list):
            self.insert_otherfile(cid, request.files.getlist('License[]'), 1)
        return jsonify(status_code.SUCCESS)


class UpdateCompany(BaseView):
    def __init__(self):
        super(UpdateCompany, self).__init__()
        self.api_permission = 'company_edit'

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def insert_otherfile(self, companyid, file_list, ptype):
        dir_path = os.path.join(upload_dir, 'otherfile')
        while not os.path.exists(dir_path):
            os.makedirs(dir_path)
        insert_sql = 'insert into tb_otherfile(companyid, filename, filepath,type) values {}'
        temp = ''
        for index, one_file in enumerate(file_list):
            filename, filepath = save_other_file(one_file)
            temp += r"""({}, '{}', '{}', {})""".format(companyid, filename, filepath, ptype)
            if index < len(file_list) - 1:
                temp += ','
        if temp != '':
            self._db.insert(insert_sql.format(temp))

    def insert_license(self, companyid, file_list, ptype):
        dir_path = os.path.join(upload_dir, 'otherfile')
        while not os.path.exists(dir_path):
            os.makedirs(dir_path)
        insert_sql = 'insert into tb_otherfile(companyid, filename, filepath,type) values {}'
        temp = ''
        for index, one_file in enumerate(file_list):
            filepath = save_image(one_file, 'static/media/otherfile')
            temp += r"""({}, '{}', '{}', {})""".format(companyid, one_file.filename, filepath, ptype)
            if index < len(file_list) - 1:
                temp += ','
        if temp != '':
            self._db.insert(insert_sql.format(temp))

    def views(self):
        if self.args_is_null('Name', 'ProvinceID', 'CityID', 'DistrictID', 'Type', 'Legal', 'Address'):
            return jsonify(status_code.CONTENT_IS_NULL)
        if self.has_data('tb_company', 'name', self.args.get('Name'), self.args.get('ID')):
            return jsonify(status_code.DATA_HAS_EXISTS)
        query_sql = r"""select License from tb_company where id={}""".format(int(self.args.get('ID')))
        result = self._db.query(query_sql)[0]
        # self.args['Phone'] = dumps(self.args['Phone'])
        # self.args['HasBadRecord'] = 2 if self.args['HasBadRecord'] == 'true' else 1
        file_list = request.files.get('License', '')
        file_img_url = result['License']
        if file_list != '':
            if os.name == 'nt':
                file_img_url = save_image(file_list, r'static\\media\\company')
            else:
                file_img_url = save_image(file_list, 'static/media/company')
        self.args['License'] = file_img_url
        ID = self.args.get('ID')
        del self.args['ID']
        temp = ''
        if 'BadRecord' in self.args.keys():
            del self.args['BadRecord']
        for index, item in enumerate(self.args.keys()):
            if isinstance(self.args[item], int):
                temp = temp + str(item) + '=' + str(self.args[item])
            else:
                temp = temp + str(item) + "='" + str(self.args[item]) + "'"
            if index < len(self.args) - 1:
                temp += ','
        update_sql = r"""update tb_company set """ + temp + r""" where id={};""".format(ID)
        self._db.update(update_sql)
        if isinstance(request.files.getlist('otherfile[]'), list):
            self.insert_otherfile(ID, request.files.getlist('otherfile[]'), 0)
        if isinstance(request.files.getlist('License[]'), list):
            self.insert_otherfile(ID, request.files.getlist('License[]'), 1)
        return jsonify(status_code.SUCCESS)


class EditGroup(BaseView):
    def __init__(self):
        super(EditGroup, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        self.args_is_null('Name', 'ID')
        update_sql = r"""update tb_pic_group set name='{}' where id ={}""".format(self.args.get('Name'),
                                                                                  self.args.get('ID'))
        self._db.update(update_sql)
        return jsonify(status_code.SUCCESS)


class GetOnePic(BaseView):
    """
    获取单张图片
    """

    def __init__(self):
        super(GetOnePic, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        self.args_is_null('ID')
        query_sql = r"""select Purl from tb_pics where id = {}""".format(self.args.get('ID'))
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['url'] = result[0]['Purl']
        return jsonify(success)


class AllCompanyID(BaseView):
    """返回所有的公司ID和名字"""

    def __init__(self):
        super(AllCompanyID, self).__init__()
        self.table = 'tb_company'

    def administrator(self):
        return self.views()

    def admin(self):
        # query_sql = r"""select t2.ID from tb_project as t1
        #                 LEFT JOIN tb_company as t2 on t1.Build = t2.id
        #                 LEFT JOIN tb_company as t3 on t1.Cons = t3.id
        #                 where t1.DID in ({})""".format(self.get_session_ids())
        # self.ids = self.set_ids(query_sql)
        return self.views()

    def get_query_sql(self):
        query_sql = r"""select ID,Name from {} """.format(self.table)
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            query_sql += """ where ID in ({}) """.format(self.to_sql_where_id())
        return query_sql

    def views(self):
        query_sql = self.get_query_sql()
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['list'] = result
        return jsonify(success)


class QueryCompanyProject(BaseView):
    """
    企业中查找项目表格
    """

    def __init__(self):
        super(QueryCompanyProject, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        self.ids = []
        if self.get_session_ids() != '':
            query_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
            self.ids = self.set_ids(query_sql)
        return self.views()

    def views(self):
        args = self.args
        query_sql = r"""select SQL_CALC_FOUND_ROWS t1.ID,t1.Name,t1.Status from tb_project as t1
                        LEFT JOIN tb_company as t2 on t1.Build = t2.ID or t1.Cons =t2.ID
                        where t2.ID = {} """.format(int(args.get('id')))
        where_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0]
            where_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if args.get('projectname', '') != '':
            where_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('projectname')))
        if int(args.get('status', 4)) != 4:
            where_list.append(r""" t1.Status = {} """.format(int(args.get('status'))))
        if where_list:
            query_sql += ' and '
        for index, i in enumerate(where_list):
            query_sql += i
            if index < len(where_list) - 1:
                query_sql += ' and '
        page = int(args.get('page', 1))
        psize = int(args.get('pagesize', 10))
        limit_sql = r""" limit {},{};""".format((page - 1) * psize, psize)
        query_sql = query_sql + " " + limit_sql
        result = self._db.query(query_sql.format(**args))
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        success = deepcopy(status_code.SUCCESS)
        success['data'] = result
        success['total'] = total[0]['total_row']
        return jsonify(success)


class DeleteOtherfile(BaseView):

    def __init__(self):
        super(DeleteOtherfile, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        args = self.args
        if self.args_is_null('id'):
            return jsonify(status_code.CONTENT_IS_NULL)
        rm_sql = r"""delete from tb_otherfile where id={};""".format(args.get('id'))
        self._db.delete(rm_sql)
        return jsonify(self.success)
