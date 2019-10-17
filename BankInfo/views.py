from flask import jsonify

from utils import status_code
from utils.BaseView import BaseView, DelteBase


class BankInfoBase(BaseView):

    def __init__(self):
        super(BankInfoBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.views()

    def views(self):
        pass


class AddUpdateBankInfo(BankInfoBase):

    def __init__(self):
        super(AddUpdateBankInfo, self).__init__()

    def views(self):
        if self.args_is_null('name', 'id'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select id from tb_bank where name ='{}';""".format(self.args.get('name'))
        result = self._db.query(query_sql)
        if int(self.args.get('id')) == 0:
            # 添加
            if result:
                return jsonify(status_code.DATA_HAS_EXISTS)
            insert_sql = r"""insert into tb_bank(name, description) 
                            value ('{}', '{}');""".format(self.args.get('name'), self.args.get('description', ''))
            try:
                self._db.insert(insert_sql)
                is_success = True
            except:
                is_success = False
        else:
            # 编辑
            if result:
                if result[0]['id'] != self.args.get('id'):
                    return jsonify(status_code.DATA_HAS_EXISTS)
            update_sql = r"""update tb_bank 
                            set name='{}', description='{}' 
                            where id={};""".format(self.args.get('name'),
                                                   self.args.get('description', ''),
                                                   self.args.get('id'))
            try:
                self._db.update(update_sql)
                is_success = True
            except:
                is_success = False
        if is_success:
            return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.DB_ERROR)


class QueryBankInfo(BankInfoBase):

    def __init__(self):
        super(QueryBankInfo, self).__init__()

    def main_query(self):
        if self.args_is_null('Page', 'PageSize'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select SQL_CALC_FOUND_ROWS * from tb_bank """
        if self.args.get('name', '') != '':
            query_sql += r""" where CONCAT(IFNULL(t3.Name,'')) LIKE '%{}%' """.format(self.args.get('Name', ''))
        start = (int(self.args.get('Page', 1)) - 1) * int(self.args.get('PageSize', 10))
        end = int(self.args.get('Page', 1)) * int(self.args.get('PageSize', 10))
        limit_sql = r""" limit {},{}; """.format(start, end)
        query_sql += limit_sql
        return query_sql

    def views(self):
        if int(self.args.get('id', 0)) == 0:
            query_sql = self.main_query()
        else:
            query_sql = r"""select SQL_CALC_FOUND_ROWS * from tb_bank where id={};""".format(self.args.get('id'))
        try:
            result, total = self._db.query(query_sql), self._db.query(self.get_total_row)
        except Exception as e:
            return jsonify(status_code.DB_ERROR)
        self.success['data'] = result
        self.success['total'] = total[0]['total_row']
        return jsonify(self.success)


class DeleteBankInfo(DelteBase):

    def __init__(self):
        super(DeleteBankInfo, self).__init__()
        self.table_name = 'tb_bank'


class QueryAllBank(BankInfoBase):

    def __init__(self):
        super(QueryAllBank, self).__init__()

    def views(self):
        query_sql = r"""select id, name from tb_bank;"""
        result = self._db.query(query_sql)
        self.success['data'] = result
        return jsonify(self.success)
