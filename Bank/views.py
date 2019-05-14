from copy import deepcopy

from flask import request, jsonify, session

from utils import status_code
from utils.BaseView import BaseView


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

    def views(self):
        args = self.args
        args['WTime'] = self.time_format(args['WTime'])
        insert_sql = r"""insert into tb_wage(ProjectID, Status,WTime, RPay) value 
                    ({ProjectID}, {Status}, '{WTime}', '{RPay}')""".format(**args)
        self._db.insert(insert_sql)
        return jsonify(status_code.SUCCESS)


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

    def data_format(self, filter_data):
        real_result_dict = {}
        for item in filter_data:
            item['WagePercent'] = eval(item['WagePercent'])
            item['Price'] = eval(item['Price'])
            Month_info = {
                'Date': self.time_to_str(item['WTime']),
                'Status': item['Status'],
                'RPay': item['RPay']
            }
            # item['Month_info'] = Month_info
            if item['Name'] in real_result_dict.keys():
                real_result_dict[item['Name']]['Month_info'].append(Month_info)
            else:
                item['Month_info'] = [Month_info, ]
                real_result_dict[item['Name']] = item
        return list(real_result_dict.values())

    def views(self):
        args = self.args
        query_sql = r"""select t2.*, t1.Name,t1.Price,t1.WagePercent,t1.Duration from tb_wage as t2
                        LEFT JOIN tb_project as t1 on t2.ProjectID = t1.id """
        where_sql_list = []
        if self.ids:
            where_sql_list.append(r""" t2.ProjectID in ({}) """.format(self.to_sql_where_id()))
        if args.get('Name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('Name')))
        if int(args.get('Status', 3)) != 3:
            where_sql_list.append(r""" t2.Status = {}  """.format(args.get('Status')))
        where_sql = ''
        if where_sql_list:
            where_sql += ' where '
            for index, item in enumerate(where_sql_list):
                where_sql += item
                if index < len(where_sql_list) - 1:
                    where_sql += ' and '
        page = int(args.get('Page', 1))
        pagesize = int(args.get('Pagesize', 10))
        order_sql = r""" ORDER BY t2.WTime limit {},{};""".format((page - 1) * pagesize, pagesize)
        result = self._db.query(query_sql + where_sql + order_sql)
        filter_data = result
        success = deepcopy(status_code.SUCCESS)
        success['bank_data'] = self.data_format(filter_data)
        return jsonify(success)
