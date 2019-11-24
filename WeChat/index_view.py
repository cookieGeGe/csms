# -*- coding: utf-8 -*-
# @Time : 2019/11/20
# @Author : zhang
# @Site :
# @File : index_view.py
# @Software: PyCharm
from flask import jsonify

from utils.BaseView import BaseView


class WechatIndexBase(BaseView):

    def __init__(self):
        super(WechatIndexBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        pass


class WechatIndexCount(WechatIndexBase):

    def __init__(self):
        super(WechatIndexCount, self).__init__()

    def query_count_data(self, query_sql):
        result = self._db.query(query_sql)
        if result:
            return result[0]
        return {}

    def project_count(self):
        query_sql = r"""
            select * from (select count(id) as total from tb_project) as t1, 
            (select count(id) as alarm from tb_project where `Status`>1) as t2,
            (select count(id) as month from tb_project where DATE_FORMAT(CreateTime, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) as t3
        """
        return self.query_count_data(query_sql)

    def company_count(self):
        query_sql = r"""
        select * from (select count(id) as total from tb_company) as t1, 
        (select count(id) as alarm from tb_company where HasBadRecord>1) as t2,
        (select count(id) as month from tb_company where DATE_FORMAT(CreateTime, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) as t3
        """
        return self.query_count_data(query_sql)

    def labor_count(self):
        query_sql = r"""
        select * from (select count(id) as total from tb_laborinfo) as t1, 
        (select count(id) as alarm from tb_laborinfo where Isbadrecord>0) as t2,
        (select count(id) as month from tb_laborinfo where DATE_FORMAT(`Create`, '%Y%m' ) = DATE_FORMAT( CURDATE( ) , '%Y%m' )) as t3
        """
        return self.query_count_data(query_sql)

    def views(self):
        self.success['project'] = self.project_count()
        self.success['company'] = self.company_count()
        self.success['labor'] = self.labor_count()
        return jsonify(self.success)
