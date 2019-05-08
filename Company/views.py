from json import loads, dumps

from copy import deepcopy

import os

import random
from flask import request, jsonify, sessions

from APP.settings import upload_dir, BASE_DIR
from Company.utils import create_random_str, update_pic_and_group
from User.util import save_image
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
        random_url = create_random_str(random.randint(4, 10))
        dir_path = os.path.join(upload_dir, self.dir + random_url)
        while os.path.exists(dir_path):
            random_url = create_random_str(random.randint(4, 10))
            dir_path = os.path.join(upload_dir, self.dir + random_url)
        os.makedirs(dir_path)
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
            os.removedirs(os.path.join(BASE_DIR, item['GUrl']))
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
            os.remove(os.path.join(BASE_DIR, item['purl']))
        delete_sql = r"""delete from {} where id={};""".format(self.table_name, int(ID))
        self._db.delete(delete_sql)
        return jsonify(status_code.SUCCESS)


class GetGroupList(BaseView):
    """
    ptype:为012代表企业，项目，劳工
    type：企业中用0表示公司执照，1表示公司图片
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
        return self.views()

    def guest(self):
        return self.admin()

    def views(self):
        args = self.args
        for i in ('Name', 'PID', 'CID', 'DID', 'Page', 'PageSize'):
            temp = args.get(i, None)
            if temp == None:
                return jsonify(status_code.CONTENT_IS_NULL)
        if int(args.get('Type')) == 0:
            query_sql = r"""select * from tb_company where CONCAT(IFNULL(Name,'')) LIKE '%{Name}%'"""
        else:
            query_sql = r"""select * from tb_company where CONCAT(IFNULL(Legal,'')) LIKE '%{Name}%'"""
        if args.get('PID', False):
            query_sql += ' and ProvinceID={PID}'
        if args.get('CID', False):
            query_sql += ' and CityID={CID}'
        if args.get('DID', False):
            query_sql += ' and DistrictID={DID}'
        if args.get('HasBadRecord', False):
            query_sql += ' and HasBadRecord=1'
        query_sql += ' limit {0},{1};'
        start_limit = (int(args.get('Page', 1)) - 1) * int(args.get('PageSize'))
        query_sql = query_sql.format(start_limit, int(args.get('PageSize')), **args)
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['company_list'] = result
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

    def views(self):
        query_sql = r"""select gurl,type from tb_pic_group 
                        where id={GID} and cid={CID} and Ptype = {0}""".format(self.ptype, **self.args)
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.DIR_NOT_EXISTS)
        temp_img_dir = result[0]['gurl'][1:]
        image_file = request.files.get('file', None)
        if image_file is None:
            return jsonify(status_code.FILE_NOT_EXISTS)
        iamge_url = save_image(image_file, temp_img_dir)
        insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type) 
                        value ({},'{}', '{}', {},{})""".format(self.args['GID'], iamge_url, image_file.filename[:-4],
                                                               self.ptype, result[0]['type'])
        id = self._db.insert(insert_sql)
        success = deepcopy(status_code.SUCCESS)
        success['id'] = id
        success['name'] = image_file.filename[:-4]
        success['url'] = iamge_url
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

    def views(self):
        ID = self.args.get('ID')
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        query_sql = r"""select t1.ID, t1.Address, t1.BadRecord,t1.Description, t1.Legal, t1.License, t1.HasBadRecord,t1.Name, t1.Phone, t1.Type,t2.Name as ProvinceID, t3.Name as CityID, t4.Name as DistrictID from tb_company as t1
                        LEFT JOIN tb_area as t2 on t1.ProvinceID = t2.ID
                        LEFT JOIN tb_area as t3 on t1.CityID = t3.ID
                        LEFT JOIN tb_area as t4 on t1.DistrictID = t4.ID
                        where t1.id = {};""".format(ID)
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.GET_COMPANY_INFO_FAILD)
        result = result[0]
        # result['Phone'] = loads(result['Phone'])
        # result['License'] = loads(result['License'])
        success = deepcopy(status_code.SUCCESS)
        success['company_info'] = result
        return jsonify(success)


class CreateCompany(BaseView):

    def __init__(self):
        super(CreateCompany, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def views(self):
        self.args['Phone'] = dumps(self.args['Phone'])
        self.args['HasBadRecord'] = 1 if self.args['HasBadRecord'] else 0
        file_list = request.files.get('License', [])
        file_url_list = []
        for image_file in file_list:
            if os.name == 'nt':
                file_url_list.append(save_image(image_file, r'static\\media\\company'))
            else:
                file_url_list.append(save_image(image_file, 'static/media/company'))
        self.args['License'] = dumps(file_url_list)
        insert_sql = r"""insert into tb_company(Name, Legal,Address,Phone,License,Type,ProvinceID,CityID,DistrictID,
        BadRecord,HasBadRecord,Description) value ('{Name}','{Legal}','{Address}','{Phone}','{License}',{Type},
        {ProvinceID},{CityID},{DistrictID}, '{BadRecord}', {HasBadRecord}, '{Description}')""".format(**self.args)
        cid = self._db.insert(insert_sql)
        update_pic_and_group('tb_pic_group', cid, self.args.get('group_list', []), self._db)
        update_pic_and_group('tb_pics', cid, self.args.get('pic_list', []), self._db)
        return jsonify(status_code.SUCCESS)


class UpdateCompany(BaseView):
    def __init__(self):
        super(UpdateCompany, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        query_sql = r"""select License from tb_company where id={}""".format(self.args.get('ID'))
        result = self._db.query(query_sql)[0]
        self.args['Phone'] = dumps(self.args['Phone'])
        self.args['HasBadRecord'] = 1 if self.args['HasBadRecord'] else 0
        file_list = request.files.get('License', [])
        file_url_list = []
        for image_file in file_list:
            if os.name == 'nt':
                file_url_list.append(save_image(image_file, r'static\\media\\company'))
            else:
                file_url_list.append(save_image(image_file, 'static/media/company'))
        file_url_list += loads(result['License'])
        self.args['License'] = dumps(file_url_list)
        ID = self.args.get('ID')
        del self.args['ID']
        temp = ''
        for index, item in enumerate(self.args.keys()):
            if isinstance(self.args[item], int):
                temp = temp + str(item) + '=' + str(self.args[item])
            else:
                temp = temp + str(item) + "='" + str(self.args[item]) + "'"
            if index < len(self.args) - 1:
                temp += ','
        update_sql = r"""update tb_company set """ + temp + r""" where id={};""".format(ID)
        self._db.update(update_sql)
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

    def __init__(self):
        super(AllCompanyID, self).__init__()
        self.table = 'tb_company'

    def administrator(self):
        self.views()

    def admin(self):
        self.views()

    def views(self):
        query_sql = r"""select ID,Name from {};""".format(self.table)
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['list'] = result
        return jsonify(result)
