from json import loads

from copy import deepcopy

import os

import random
from flask import request, jsonify, sessions

from APP.settings import upload_dir, BASE_DIR
from Company.utils import create_random_str
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
        return self.views()

    def views(self):
        args = request.form
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
        ID = request.args.get('ID', None)
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
        ID = request.args.get('ID', None)
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
        return self.views()

    def views(self):
        ID = request.args.get('CID')
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
        return self.views()

    def views(self):
        ID = request.args.get('ID')
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
        return self.views()

    def views(self):
        args = request.args
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
        start_limit = (int(args.get('Page', 1) - 1 * int(args.get('PageSize'))))
        query_sql = query_sql.format(start_limit, int(args.get('PageSize')), **args)
        result = self._db.query(query_sql)
        success = status_code.SUCCESS
        success['company_list'] = result
        return jsonify(success)


class CompanyInfo(BaseView):
    def __init__(self):
        super(CompanyInfo, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.views()

    def views(self):
        ID = request.args.get('ID', None)
        if ID is None:
            return status_code.ID_ERROR
        query_sql = r"""select * from tb_company where id={}""".format(ID)
        result = self._db.query(query_sql)
        result['Phone'] = loads(result['Phone'])
        success = status_code.SUCCESS
        success['company_info'] = result
        return jsonify(success)
