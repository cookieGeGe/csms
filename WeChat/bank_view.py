# -*- coding: utf-8 -*-
# @Time : 2019/11/27
# @Author : zhang
# @Site :
# @File : bank_view.py
# @Software: PyCharm
import datetime

from flask import jsonify

from utils.BaseView import BaseView


class WechatBankBase(BaseView):

    def __init__(self):
        super(WechatBankBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        pass


class WechatBankQuery(WechatBankBase):

    def __init__(self):
        super(WechatBankQuery, self).__init__()

    def admin(self):
        self.ids = self.get_project_ids()
        return self.views()

    def create_all_month(self, start_time, end_time):
        """
        获取所有的月份
        :param start_time:
        :param end_time:
        :return:
        """
        start_year, end_year = start_time.year, end_time.year
        start_month, end_month = start_time.month, end_time.month
        all_month = {}
        if start_year == end_year:
            all_month[str(start_year)] = []
            for i in range(start_month, end_month + 1):
                all_month[str(start_year)].append(self.get_temp(i))
        else:
            for temp_year in range(start_year, end_year + 1):
                all_month[str(temp_year)] = []
                if temp_year == start_year:
                    for i in range(start_month, 13):
                        all_month[str(temp_year)].append(self.get_temp(i))
                elif temp_year == end_year:
                    for i in range(1, end_month + 1):
                        all_month[str(temp_year)].append(self.get_temp(i))
                else:
                    for i in range(1, 13):
                        all_month[str(temp_year)].append(self.get_temp(i))
        return all_month

    def get_temp(self, i):
        return {
            'month': i,
            'id': 0,
            'is_input': 0,
            'is_now_month': 0,
            'is_current': 0,
        }

    def project_wage_info(self):
        query_sql = r"""
                    select t1.id, t1.name, t3.name as bank, t1.starttime, t1.endtime, t1.WagePercent, t1.TotalMonth, t1.account,t1.price, sum(t2.ActualPay+0) as totalpay from tb_project as t1
                    right join tb_wage as t2 on t2.ProjectID = t1.id
                    left join tb_bank as t3 on t1.Bank = t3.id where t1.id = {} group by id
                """.format(self.args.get('id'))
        result = self._db.query(query_sql)
        result = result[0]
        query_bank_info = r"""
            select t1.* from tb_wage as t1
            left join tb_progress as t2 on t1.ProjectID = t2.ProjectID and t1.year=t2.year and t1.month =t2.month
            where t1.ProjectID = {} order by year, month desc
        """.format(self.args.get('id'))
        allYearMonth = self.create_all_month(result['starttiem'], result['endtime'])
        bank_info = self._db.query(query_bank_info)
        now_time = datetime.datetime.now()
        bankinfo = {}
        if bank_info:
            for index, bank in enumerate(bank_info):
                temp_year = int(bank['year'])
                temp_month = int(bank['month'])
                for index, item in enumerate(allYearMonth[str(temp_year)]):
                    if item['month'] == temp_month:
                        allYearMonth[str(temp_year)][index]['is_input'] = 1
                        allYearMonth[str(temp_year)][index]['id'] = bank['ID']
                    if temp_year == now_time.year and item['month'] == now_time.month:
                        allYearMonth[str(temp_year)][index]['is_now_month'] = 1
                    if index == len(bank_info) - 1 and item['month'] == temp_month:
                        allYearMonth[str(temp_year)][index]['is_current'] = 1
            bankinfo = bank_info[-1]
        self.success['bankinfo'] = bankinfo
        self.success['project'] = result
        self.success['allmonth'] = allYearMonth
        return self.success

    def main_query(self):
        query_sql = r"""
            select SQL_CALC_FOUND_ROWS t1.id, t1.name, t3.name as bank, t1.starttime, t1.WagePercent, t1.TotalMonth, t1.account,t1.price, sum(t2.ActualPay+0) as totalpay from tb_project as t1
            right join tb_wage as t2 on t2.ProjectID = t1.id
            left join tb_bank as t3 on t1.Bank = t3.id
        """
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if int(self.args.get('bank', '0')) != 0:
            where_sql_list.append(r""" t3.id={} """.format(self.args.get('bank')))
        if int(self.args.get('pid', '0')) != 0:
            where_sql_list.append(r""" t1.pid={} """.format(self.args.get('pid')))
        if int(self.args.get('cid', '0')) != 0:
            where_sql_list.append(r""" t1.cid={} """.format(self.args.get('cid')))
        if int(self.args.get('did', '0')) != 0:
            where_sql_list.append(r""" t1.did={} """.format(self.args.get('did')))
        if self.args.get('time', '') != '':
            where_sql_list.append(r""" t1.starttime > '{}' """.format(self.args.get('time')))
        where_sql = self.get_where_sql(where_sql_list)
        page = int(self.args.get('page', '1'))
        limit_sql = r""" limit {},{} """.format((page - 1) * 10, 10)
        total_query_sql = query_sql + where_sql + ' group by id ' + limit_sql
        result, total = self._db.query(total_query_sql), self._db.query(self.get_total_row)
        for item in result:
            item['starttime'] = item['starttime'].strftime("%Y-%m-%d")
            item['totalpay'] = 0 if item['totalpay'] is None or item['totalpay'] == '' else item['totalpay']
            item['bank'] = '' if item['bank'] is None or item['bank'] == '' else item['bank']
            item['account'] = '' if item['account'] is None or item['account'] == '' else item['account']
        self.success['data'] = result
        self.success['total'] = total[0]['total_row']
        return self.success

    def views(self):
        if int(self.get('id', '0')) == 0:
            success = self.main_query()
        else:
            success = self.project_wage_info()
        return self.make_response(success)


class WechatBankInfo(WechatBankBase):

    def __init__(self):
        super(WechatBankInfo, self).__init__()

    def views(self):
        query_bank_info = r"""
                    select t1.* from tb_wage as t1
                    left join tb_progress as t2 on t1.ProjectID = t2.ProjectID and t1.year=t2.year and t1.month =t2.month
                    where t1.id = {} order by year, month desc
                """.format(self.args.get('id'))
        result = self._db.query(query_bank_info)
        bankinfo = {}
        if result:
            bankinfo = result[0]
            bankinfo['WTime'] = bankinfo['WTime'].strftime("%Y-%m-%d %H:%M:%S")
        self.success['bankinfo'] = bankinfo
        return self.make_response(self.success)
