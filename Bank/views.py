import datetime

from copy import deepcopy

from flask import request, jsonify, session

from utils import status_code
from utils.BaseView import BaseView
from utils.pulic_utils import str_to_date


class BankBase(BaseView):

    def __init__(self):
        super(BankBase, self).__init__()

    def admin(self):
        return self.views()

    def administrator(self):
        return self.views()

    def views(self):
        return jsonify(status_code.SUCCESS)


class CreateBank(BankBase):
    """
    创建银行管理
    """

    def __init__(self):
        super(CreateBank, self).__init__()
        self.api_permission = 'bank_edit'

    def views(self):
        args = self.args
        args['WTime'] = datetime.datetime.strptime(args['WTime'], "%Y-%m")
        args['Year'] = args['WTime'].year
        args['Month'] = args['WTime'].month
        if args['WTime'] > datetime.datetime.now():
            return jsonify(status_code.CREATE_FEATURE_BANK_INFO)
        if int(args.get('ID', 0)) == 0:
            query_sql = r"""select id from tb_wage where projectid = {ProjectID} and year={Year} and month = {Month};""".format(**args)
            result = self._db.query(query_sql)
            if result:
                return jsonify(status_code.BANK_INFO_EXISTS)
            insert_sql = r"""insert into tb_wage(ProjectID, Status,WTime, RPay,year,month) value 
                            ({ProjectID}, {Status}, '{WTime}', '{RPay}', '{Year}', '{Month}')""".format(**args)
            self._db.insert(insert_sql)
        else:
            update_sql = r"""update tb_wage set Status={Status}, WTime='{WTime}', RPay='{RPay}'
                            where id={ID}""".format(**args)
            self._db.update(update_sql)
        return jsonify(status_code.SUCCESS)


class QueryOneBank(BankBase):

    def __init__(self):
        super(QueryOneBank, self).__init__()

    def views(self):
        query_sql = r"""select * from tb_wage where id={}""".format(
            self.args.get('ID'))
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['data'] = result[0]
        return jsonify(success)


class QueryBank(BankBase):
    """
    创建银行管理
    """

    def __init__(self):
        super(QueryBank, self).__init__()

    def admin(self):
        query_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
        self.ids = self.set_ids(query_sql)
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
                all_month[str(start_year)].append(i)
        else:
            for temp_year in range(start_year, end_year + 1):
                all_month[str(temp_year)] = []
                if temp_year == start_year:
                    for i in range(start_month, 13):
                        all_month[str(temp_year)].append(i)
                elif temp_year == end_year:
                    for i in range(1, end_month + 1):
                        all_month[str(temp_year)].append(i)
                else:
                    for i in range(1, 13):
                        all_month[str(temp_year)].append(i)
        return all_month

    def get_one_month_data(self, args, year, month):
        """
        获取每一个月的数据
        :param args: 项目对象信息
        :param year:  哪一年
        :param month:  那一月
        :return:
        """
        query_sql = r"""select * from tb_wage where year = {} and month={} and projectid = {};""".format(
            year, month, args['ID']
        )
        temp_result = self._db.query(query_sql)
        args['MonthPay'] = eval(args['Price']) * eval(args['WagePercent']) / 100 / args['Duration']
        args['ID'] = 0
        args['Date'] = str(year) + '-' + str(month)
        args['Status'] = 2
        args['RPay'] = ''
        if temp_result:
            args['ID'] = temp_result[0]['ID']
            # if temp_result[0]['WTime'] != '':
            #     args['Date'] = temp_result[0]['WTime'].strftime("%Y-%m-%d")
            args['Status'] = temp_result[0]['Status']
            args['RPay'] = temp_result[0]['RPay']
        return deepcopy(args)

    def data_format(self, filter_data):
        real_result_dict = []
        for item in filter_data:
            now_time = datetime.datetime.now()
            start_time = item['StartTime']
            end_time = item['EndTime']
            item['ProjectID'] = item['ID']
            if start_time > now_time:
                all_month = {}
            elif start_time < now_time and now_time < end_time:
                all_month = self.create_all_month(start_time, now_time)
            else:
                all_month = self.create_all_month(start_time, end_time)
            for year in all_month.keys():
                for month in all_month[year]:
                    real_result_dict.append(self.get_one_month_data(deepcopy(item), year, month))
        return real_result_dict

    def views(self):
        args = self.args
        query_sql = r"""select SQL_CALC_FOUND_ROWS distinct(t1.ID), t1.Name,t1.Price,t1.WagePercent,t1.Duration, t1.StartTime, t1.EndTime, t3.TotalPay from tb_project as t1 
                        left join (select projectid,sum(rpay) as totalpay from tb_wage GROUP BY ProjectID) as t3 on t3.projectid = t1.id
                        left JOIN tb_wage as t2 on t2.ProjectID = t1.id"""
        where_sql_list = []
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            where_sql_list.append(r""" t2.ProjectID in ({}) """.format(self.to_sql_where_id()))
        if args.get('Name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('Name')))
        if int(args.get('Status', 3)) != 3:
            if int(args.get('Status', 2)) != 2:
                where_sql_list.append(r""" t2.Status = {}  """.format(args.get('Status')))
            else:
                where_sql_list.append(r""" t2.Status = {} or t2.Status is null """.format(args.get('Status')))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            for index, item in enumerate(where_sql_list):
                where_sql += item
                if index < len(where_sql_list) - 1:
                    where_sql += ' and '
        page = int(args.get('Page', 1))
        pagesize = int(args.get('PageSize', 1))
        order_sql = r""" limit {},{};""".format((page - 1) * pagesize, pagesize)
        result = self._db.query(query_sql + where_sql + order_sql)  # 所有公司
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        filter_data = result
        success = deepcopy(status_code.SUCCESS)
        success['bank_data'] = self.data_format(filter_data)
        success['total'] = total[0]['total_row']
        return jsonify(success)
