from json import loads, dumps

from copy import deepcopy

import os

import random
from flask import request, jsonify, sessions

from APP.settings import upload_dir, BASE_DIR
from Company.utils import create_random_str
from User.util import save_image
from utils import status_code
from utils.BaseView import BaseView, DelteBase


class CreatePicGroup(BaseView):

    def __init__(self):
        super(CreatePicGroup, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def views(self):
        args = self.args
        random_url = create_random_str(random.randint(4, 10))
        dir_path = os.path.join(upload_dir, 'company/' + random_url)
        while os.path.exists(dir_path):
            random_url = create_random_str(random.randint(4, 10))
            dir_path = os.path.join(upload_dir, 'company/' + random_url)
        os.makedirs(dir_path)
        insert_group = r"""insert into tb_pic_group(Name,Type,Gurl, CID) 
                                value ('{Name}', {Gtype}, '{0}',{CID})""".format('/static/media/company' + random_url,
                                                                                 **dict(args.items()))
        self._db.insert(insert_group)
        return jsonify(status_code.SUCCESS)


class DeletePicGroup(DelteBase):

    def __init__(self):
        super(DeletePicGroup, self).__init__()
        self.table_name = 'tb_pic_group'

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
    def __init__(self):
        super(DeletePic, self).__init__()
        self.table_name = 'tb_pics'

    def views(self):
        ID = self.args.get('ID', None)
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        query_sql = r"""select purl from {} where id={}""".format(self.table_name, int(ID))
        pic_list = self._db.query(query_sql)
        for item in pic_list:
            os.remove(os.path.join(BASE_DIR, item['purl']))
        delete_sql = r"""delete from {} where id={}""".format(self.table_name, int(ID))
        self._db.delete(delete_sql)
        return jsonify(status_code.SUCCESS)


class GetGroupList(BaseView):

    def __init__(self):
        super(GetGroupList, self).__init__()

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
        query_sql = r"""select * from tb_pic_group where CID={}""".format(ID)
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
            query_sql = r"""select * from tb_company where CONCAT(IFNULL(Name,'')) LIKE '%{Name}%'
                        OR CONCAT(IFNULL(ProvinceID,'')) LIKE '%{PID}%'
                        OR CONCAT(IFNULL(CityID,'')) LIKE '%{CID}%'
                        OR CONCAT(IFNULL(DistrictID,'')) LIKE '%{DID}%' """
        else:
            query_sql = r"""select * from tb_company where CONCAT(IFNULL(Legal,'')) LIKE '%{Name}%'
                                    OR CONCAT(IFNULL(ProvinceID,'')) LIKE '%{PID}%'
                                    OR CONCAT(IFNULL(CityID,'')) LIKE '%{CID}%'
                                    OR CONCAT(IFNULL(DistrictID,'')) LIKE '%{DID}%'"""
        if args.get('HasBadRecord', False):
            query_sql += 'and HasBadRecord=1'
        query_sql += 'limit {0},{1};'
        start_limit = (int(args.get('Page', 1)) - 1) * int(args.get('PageSize'))
        query_sql = query_sql.format(start_limit, int(args.get('PageSize')), **args)
        result = self._db.query(query_sql)
        success = status_code.SUCCESS
        success['company_list'] = result
        return jsonify(success)


class UploadPic(BaseView):

    def __init__(self):
        super(UploadPic, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.admin()

    def views(self):
        query_sql = r"""select gurl from tb_pic_group where id={GID} and cid={CID}""".format(**self.args)
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.FILE_NOT_EXISTS)
        temp_img_dir = result[0]['gurl'][1:]
        image_file = request.files.get('file')
        iamge_url = save_image(image_file, temp_img_dir)
        insert_sql = r"""insert into tb_pics(GroupID, prul, name) 
                        value ({},'{}', '{}')""".format(self.args['GID'], iamge_url, image_file.filename[:-4])
        self._db.insert(insert_sql)
        return jsonify(status_code.SUCCESS)


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
        file_list = request.files.get('License')
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
        self._db.insert(insert_sql)
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
        result = self._db.query(query_sql)
        self.args['Phone'] = dumps(self.args['Phone'])
        self.args['HasBadRecord'] = 1 if self.args['HasBadRecord'] else 0
        file_list = request.files.get('License')
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
            temp = temp + str(item) + '=' + str(self.args[item])
            if index < len(self.args) - 1:
                temp += ','
        update_sql = r"""update tb_company set """ + temp + r""" where id={}""".format(ID)
        self._db.update(update_sql)
        return jsonify(status_code.SUCCESS)
