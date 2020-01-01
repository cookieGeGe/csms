import datetime
import os

from copy import deepcopy

from flask import request, jsonify, session

from APP.settings import static_dir
from User.util import save_image
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
        if self.args_is_null('ProjectID', 'WTime', 'RPay', 'Status', 'ActualPay'):
            return jsonify(status_code.CONTENT_IS_NULL)
        args = self.args
        args['WTime'] = datetime.datetime.strptime(args['WTime'], "%Y-%m")
        args['Year'] = args['WTime'].year
        args['Month'] = args['WTime'].month
        if args['WTime'] > datetime.datetime.now():
            return jsonify(status_code.CREATE_FEATURE_BANK_INFO)
        if int(args.get('ID', 0)) == 0:
            query_sql = r"""select id from tb_wage where projectid = {ProjectID} and year={Year} and month = {Month};""".format(
                **args)
            result = self._db.query(query_sql)
            if result:
                return jsonify(status_code.BANK_INFO_EXISTS)
            insert_sql = r"""insert into tb_wage(ProjectID, Status,WTime, RPay,year,month,actualpay) value 
                            ({ProjectID}, {Status}, '{WTime}', '{RPay}', '{Year}', '{Month}', '{ActualPay}')""".format(
                **args)
            self._db.insert(insert_sql)
        else:
            update_sql = r"""update tb_wage set Status={Status}, WTime='{WTime}', RPay='{RPay}', ActualPay='{ActualPay}'
                            where id={ID}""".format(**args)
            self._db.update(update_sql)
        return jsonify(status_code.SUCCESS)


class QueryOneBank(BankBase):

    def __init__(self):
        super(QueryOneBank, self).__init__()
        self.api_permission = 'bank_show'

    def views(self):
        """
        查询某一个单个银行
        :return:
        """
        query_sql = r"""select * from tb_wage where id={}""".format(
            self.args.get('ID'))
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['data'] = result[0]
        return jsonify(success)


class QueryBank(BankBase):
    """
    查询银行管理
    """

    def __init__(self):
        super(QueryBank, self).__init__()
        self.api_permission = 'bank_show'
        self.total_balance = 0

    def admin(self):
        # query_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
        # self.ids = self.set_ids(query_sql)
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
        获取单个项目每一个月的数据
        :param args: 项目对象信息
        :param year:  哪一年
        :param month:  那一月
        :return:
        """
        query_sql = r"""select t1.*, t2.Workers from tb_wage as t1 
                        left join tb_progress as t2 on t1.year = t2.year and t1.month = t2.month and t1.projectid = t2.projectid 
                        where t1.year = {} and t1.month={} and t1.projectid = {};""".format(
            year, month, args['ID']
        )
        temp_result = self._db.query(query_sql)
        if args['TotalMonth'] == 0:
            args['MonthPay'] = 0
        else:
            args['MonthPay'] = eval(args['Price']) * eval(args['WagePercent']) / 100 / args['TotalMonth']
        args['ID'] = 0
        args['Date'] = str(year) + '-' + str(month)
        args['Status'] = 2
        args['RPay'] = 0  # 实际到账金额
        args['ActualPay'] = 0  # 实际支付情况
        args['Receipt'] = ''  # 银行回单
        args['Balance'] = 0  # 银行差值
        args['Workers'] = 0
        if temp_result:
            args['ID'] = temp_result[0]['ID']
            # if temp_result[0]['WTime'] != '':
            #     args['Date'] = temp_result[0]['WTime'].strftime("%Y-%m-%d")
            args['Status'] = temp_result[0]['Status']
            args['RPay'] = temp_result[0]['RPay']
            args['ActualPay'] = eval(
                temp_result[0]['ActualPay'] if temp_result[0]['ActualPay'] is not None else '0'
            )  # 实际支付情况
            args['Receipt'] = temp_result[0]['Receipt']  # 银行回单
            args['Balance'] = args['RPay'] - args['ActualPay']  # 银行差值
            args['Workers'] = temp_result[0]['Workers'] if temp_result[0]['Workers'] is not None else 0
        self.total_balance += args['Balance']
        return deepcopy(args)

    def data_format(self, filter_data):
        """
        格式化一个项目多个月份的数据
        :param filter_data:
        :return:
        """
        real_result_dict = []
        for item in filter_data:
            now_time = datetime.datetime.now()
            start_time = item['StartTime']
            end_time = item['EndTime']
            item['BankName'] = item['BankName'] if item['BankName'] is not None else ''
            item['Account'] = item['Account'] if item['Account'] is not None else ''
            # duration = datetime.datetime.strptime(item['Duration'], "%Y-%m-%d")
            item['ProjectID'] = item['ID']
            if start_time > now_time:
                all_month = {}
            elif start_time < now_time and now_time < end_time:
                all_month = self.create_all_month(start_time, now_time)
            else:
                if item['Duration'] == '':
                    all_month = self.create_all_month(start_time, end_time)
                else:
                    duration = datetime.datetime.strptime(item['Duration'], "%Y-%m-%d")
                    if now_time < duration:
                        all_month = self.create_all_month(start_time, now_time)
                    else:
                        all_month = self.create_all_month(start_time, duration)
            for year in all_month.keys():
                for month in all_month[year]:
                    real_result_dict.append(self.get_one_month_data(deepcopy(item), year, month))
        return real_result_dict

    def views(self):
        args = self.args
        query_sql = r"""select SQL_CALC_FOUND_ROWS distinct(t1.ID), t1.Name,t1.Price,t1.WagePercent,t1.TotalMonth, 
                          t1.StartTime, t1.EndTime, t3.TotalPay,t1.Duration, t4.Name as BankName, t1.Account 
                        from tb_project as t1 
                        left join (select projectid,sum(rpay) as totalpay from tb_wage GROUP BY ProjectID) as t3 on t3.projectid = t1.id
                        left JOIN tb_wage as t2 on t2.ProjectID = t1.id
                        left join tb_bank as t4 on t4.id = t1.bank"""
        where_sql_list = []
        if self.ids != None:
            if not self.ids:
                self.ids = [0, ]
            where_sql_list.append(r""" t2.ProjectID in ({}) """.format(self.to_sql_where_id()))
        # print(args)
        if int(args.get('qtype', '0')) == 1:
            if args.get('BankName', '') != '':
                where_sql_list.append(r""" concat(ifnull(t4.Name, '')) like '%{}%' """.format(args.get('BankName', '')))
        else:
            if args.get('Name', '') != '':
                where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('Name')))
            if int(args.get('DID', 0)) != 0:
                where_sql_list.append(r""" t1.DID={} """.format(int(args.get('DID'))))
            if int(args.get('CID', 0)) != 0:
                where_sql_list.append(r""" t1.CID={} """.format(int(args.get('CID'))))
            if int(args.get('PID', 0)) != 0:
                where_sql_list.append(r""" t1.PID={} """.format(int(args.get('PID'))))
        if int(args.get('Status', 3)) != 3:
            if int(args.get('Status', 2)) != 2:
                where_sql_list.append(r""" t2.Status = {}  """.format(args.get('Status')))
            else:
                where_sql_list.append(r""" (t2.Status = {} or t2.Status is null) """.format(args.get('Status')))
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
        # print(query_sql + where_sql + order_sql)
        result = self._db.query(query_sql + where_sql + order_sql)  # 所有公司
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        filter_data = result
        success = deepcopy(status_code.SUCCESS)
        success['bank_data'] = self.data_format(filter_data)
        success['total_balance'] = self.total_balance
        success['total'] = total[0]['total_row']
        # print(success)
        return jsonify(success)


class AddBankReceipt(BankBase):

    def __init__(self):
        super(AddBankReceipt, self).__init__()

    def views(self):
        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        files = request.files.getlist('file')
        if not files:
            return jsonify(status_code.FILE_NOT_EXISTS)
        img_dir = os.path.join(static_dir, 'media', 'bankreceipt')
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)
        img_url = save_image(files[0], 'static/media/bankreceipt')
        update_sql = r"""update tb_wage set receipt='{}', rectime='{}' where id={};""".format(
            img_url, datetime.datetime.now(), self.args.get('ID')
        )
        self._db.update(update_sql)
        return jsonify(self.success)


class DeleteBankOneInfo(BankBase):

    def __init__(self):
        super(DeleteBankOneInfo, self).__init__()

    def views(self):
        if self.args_is_null('id'):
            return jsonify(status_code.CONTENT_IS_NULL)
        print(self.args)
        delete_sql = r"""
            delete from alarm where id={}
        """.format(self.args.get('id'))
        try:
            self._db.delete(delete_sql)
            return jsonify(self.success)
        except:
            return jsonify(status_code.DB_ERROR)
