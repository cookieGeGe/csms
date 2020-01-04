# -*- coding: utf-8 -*-
# @Time : 2020/1/4
# @Author : zhang
# @Site :
# @File : twoMonthPro.py
# @Software: PyCharm
import datetime

from dateutil.relativedelta import relativedelta


class getTwoMonth():

    def __init__(self):
        self.today = datetime.date.today()
        self.last_2_month = self.today + relativedelta(months=-2)
        self.last_1_month = self.today + relativedelta(months=-1)
        self.lastTwoMonth = datetime.datetime(self.last_2_month.year, self.last_2_month.month, 1)
        self.lastOneMonth = datetime.datetime(self.last_1_month.year, self.last_1_month.month, 1)
        self.is_input_project_list = []

    def list_to_str(self, templist):
        return [str(item) for item in templist]

    def get_unexcept_project(self, project_ids):
        query_sql = r"""
            select id, name,starttime,endtime from tb_project
        """
        where_sql_list = []
        where_sql_list.append(r"""
            endtime>= '{}-{}-1'
        """.format(self.last_2_month.year, self.last_2_month.month))
        if project_ids:
            where_sql_list.append(r""" ID in ({}) """.format(','.join(self.list_to_str(project_ids))))
        if where_sql_list:
            query_sql += ' where '
            query_sql += ' and '.join(where_sql_list)
        # print(query_sql)
        result = self._db.query(query_sql)
        return result

    def get_has_progress(self):
        query_sql = r"""
            select id,projectid, year, month from tb_progress where year>={} and month >= {};
        """.format(self.last_2_month.year, self.last_2_month.month)
        result = self._db.query(query_sql)
        project_list = [item['projectid'] for item in result]
        self.is_input_project_list = project_list
        return project_list

    def is_input_progress(self, project_item):
        """
        没有填项目进度为false
        :param project_item:
        :return:
        """
        if project_item['id'] not in self.is_input_project_list:
            return False
        projectid = project_item['id']
        if project_item['endtime'] < self.lastOneMonth and self.is_input_project_list.count(projectid) < 1:
            return False
        elif project_item['endtime'] > self.lastOneMonth and self.is_input_project_list.count(projectid) < 2:
            return False
        else:
            return True

    def get_uninput_project_ids(self, projectids):
        unexcept_project = self.get_unexcept_project(projectids)
        self.get_has_progress()
        un_input_project = []
        for project in unexcept_project:
            if not self.is_input_progress(project):
                un_input_project.append(str(project['id']))
        return un_input_project
