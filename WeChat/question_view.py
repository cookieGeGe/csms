# -*- coding: utf-8 -*-
# @Time : 2019/11/28
# @Author : zhang
# @Site :
# @File : question_view.py
# @Software: PyCharm
import os

from APP.settings import static_dir
from utils.BaseView import BaseView


class WechatQuestionBase(BaseView):

    def __init__(self):
        super(WechatQuestionBase, self).__init__()
        self.is_admin = 0

    def administrator(self):
        return self.views()

    def admin(self):
        self.is_admin = 1
        return self.views()

    def views(self):
        pass


class WechatQuestion(WechatQuestionBase):

    def __init__(self):
        super(WechatQuestion, self).__init__()

    def main_query(self):
        query_sql = r"""select SQL_CALC_FOUND_ROWS id, name from tb_question """
        where_sql_list = []
        if self.args.get('name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(name,'')) LIKE '%{}%' """.format(self.args.get('name')))
        if 'question_all_show' not in self._permissions:
            where_sql_list.append(r""" t1.type = 2 """)
        where_sql = self.get_where_sql(where_sql_list)
        result = self._db.query(query_sql + where_sql)
        self.success['data'] = result
        return self.success

    def read_file(self, path):
        try:
            with open(os.path.join(static_dir, *path.split('/')), 'r') as f:
                lines = f.readlines()
                if lines:
                    return ''.join(lines)
        except Exception as e:
            print(e)
            return ''

    def get_question(self):
        query_sql = r"""select id, name, answer from tb_question where id='{}';""".format(self.args.get('id'))
        result = self._db.query(query_sql)
        data = result[0]
        data['answer'] = '' if data['answer'] == '' else self.read_file(data['answer'])
        self.success['question'] = data
        return self.success

    def views(self):
        if int(self.args.get('id', '0')) == 0:
            success = self.main_query()
        else:
            success = self.get_question()
        return self.make_response(success)
