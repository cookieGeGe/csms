# -*- coding: utf-8 -*-
# @Time : 2019/11/20
# @Author : zhang
# @Site :
# @File : company_view.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time : 2019/11/20
# @Author : zhang
# @Site :
# @File : project_view.py
# @Software: PyCharm
from copy import deepcopy
from json import loads

from flask import jsonify

from utils import status_code
from utils.BaseView import BaseView


class WechatComBase(BaseView):

    def __init__(self):
        super(WechatComBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        self.ids = self.get_company_ids()
        return self.views()

    def views(self):
        pass


class WechatComQuery(WechatComBase):

    def __init__(self):
        super(WechatComQuery, self).__init__()

    def admin(self):
        self.ids = self.get_company_ids()
        return self.views()

    def get_total_query(self, query_sql):
        result = self._db.query(query_sql)
        total = self._db.query(self.get_total_row)
        return result, total

    def main_list_query(self):
        """
        首页和列表页面搜索
        :return:
        """
        query_sql = r"""
            select t1.id,t1.legal,t1.name,t1.type, t1.address,t1.hasbadrecord, t1.createtime from tb_company as t1
        """
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if int(self.args.get('type', '0')) != 0:
            where_sql_list.append(r""" t1.type={} """.format(self.args.get('type')))
        if self.args.get('status') != '' and self.args.get('status') == 'false':
            where_sql_list.append(r""" t1.HasBadRecord>1 """)
        else:
            if int(self.args.get('status', '0')) != 0:
                where_sql_list.append(r""" t1.HasBadRecord={} """.format(self.args.get('status')))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t1.provinceid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t1.cityid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t1.districtid={} """.format(self.args.get('did')))
        if self.args.get('time', '') != '':
            where_sql_list.append(r""" t1.createtime > '{}' """.format(self.args.get('time')))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            where_sql += ' and '.join(where_sql_list)
        page = int(self.args.get('page', '1'))
        limit_sql = r""" limit {},{} """.format((page - 1) * 10, 10)
        total_query_sql = query_sql + where_sql + limit_sql
        result, total = self.get_total_query(total_query_sql)
        alarm = 0
        for item in result:
            if item['createtime'] is not None and item['createtime'] != '':
                item['createtime'] = self.time_to_str(item['createtime'])
            if item['hasbadrecord'] > 1:
                alarm += 1
        self.success['company'] = result
        self.success['total'] = total[0]['total_row']
        self.success['alarm'] = alarm
        return self.success

    def get_all_file(self, companyid, ptype):
        query_sql = r"""select * from tb_otherfile where companyid={} and type={}""".format(companyid, ptype)
        file_list = self._db.query(query_sql)
        return file_list

    def one_company_query(self):
        ID = self.args.get('id')
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        query_sql = r"""select t1.ID, t1.Address, t1.BadRecord,t1.Description, t1.Legal, t1.License, t1.HasBadRecord,
                                t1.Name, t1.Phone, t1.Type, t1.url, t1.OtherInfo, t2.Name as ProvinceID, t3.Name as CityID, t4.Name as DistrictID, 
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
        for index, item in enumerate(result['Phone']):
            if 'projectName' not in item.keys():
                result['Phone'][index]['projectName'] = ''
        result['other_file_list'] = self.get_all_file(result['ID'], 0)
        result['license_list'] = self.get_all_file(result['ID'], 1)
        # result['License'] = loads(result['License'])
        if result['OtherInfo'] is None:
            result['OtherInfo'] = ''
        self.success['company'] = result
        self.group_info()
        return self.response_lower(self.success)

    def group_info(self):
        ID = self.args.get('id')
        if ID is None:
            return jsonify(status_code.ID_ERROR)
        query_sql = r"""select * from tb_pic_group where CID={} and Ptype = 0""".format(ID)
        result_list = self._db.query(query_sql)
        Lgroup_list = []
        group_list = []
        for item in result_list:
            if item['Type']:
                Lgroup_list.append(item)
            else:
                group_list.append(item)
        self.success['license_photo_list'] = Lgroup_list
        self.success['company_photo_list'] = group_list

    def views(self):
        if int(self.args.get('id', '0')) == 0:
            success = self.main_list_query()
        else:
            success = self.one_company_query()

        return self.make_response(success)


class WechatComQueryPro(WechatComBase):

    def __init__(self):
        super(WechatComQueryPro, self).__init__()

    def views(self):
        query_sql = r"""select SQL_CALC_FOUND_ROWS t1.id, t1.name, t1.address, t1.`status`, t1.type, t1.gamount, t1.starttime, t1.endtime, t1.guarantype,t1.wagepercent, t2.name as bank, t1.createtime  from tb_project as t1
                        left join tb_bank as t2 on t1.bank = t2.id
                        LEFT JOIN tb_company as t3 on t1.Build = t3.ID or t1.Cons =t3.ID
                        where (t3.ID = {}  or CONCAT(IFNULL(t1.SubCompany,'')) LIKE '%"ID":"{}"%')
                        """.format(int(self.args.get('id')), int(self.args.get('id')))
        where_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0]
            where_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if where_list:
            query_sql += ' and '
        for index, i in enumerate(where_list):
            query_sql += i
            if index < len(where_list) - 1:
                query_sql += ' and '
        page = int(self.args.get('page', 1))
        limit_sql = r""" limit {},{};""".format((page - 1) * 10, 10)
        query_sql = query_sql + " " + limit_sql
        result = self._db.query(query_sql)
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        for item in result:
            if item['starttime'] is not None and item['starttime'] != '':
                item['starttime'] = self.time_to_str(item['starttime'])
            if item['endtime'] is not None and item['endtime'] != '':
                item['endtime'] = self.time_to_str(item['endtime'])
        self.success['data'] = result
        self.success['total'] = total[0]['total_row']
        return jsonify(self.success)
