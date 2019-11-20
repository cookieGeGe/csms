# -*- coding: utf-8 -*-
# @Time : 2019/11/19
# @Author : zhang
# @Site :
# @File : views.py
# @Software: PyCharm
import os
import random
import time

from flask import jsonify

from APP.settings import static_dir
from utils import status_code
from utils.BaseView import BaseView


class QuestionBase(BaseView):

    def __init__(self):
        super(QuestionBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        pass


class QueryQuestion(QuestionBase):

    def __init__(self):
        super(QueryQuestion, self).__init__()
        self.api_permission = 'question_show'
        self.query_sql = r"""
        select SQL_CALC_FOUND_ROWS t1.id, t1.Name, t1.Type, t1.Answer,t1.Updatetime as Time, t2.LoginName as Creator from tb_question as t1
        left join tb_user as t2 on t1.creator = t2.id
        """

    def read_file(self, path):
        try:
            with open(os.path.join(static_dir, *path.split('/')), 'r') as f:
                lines = f.readlines()
                if lines:
                    return ''.join(lines)
        except Exception as e:
            print(e)
            return ''

    def main_query(self, args):
        where_sql_list = []
        if args.get('Name', '') != '':
            where_sql_list.append(r"""  CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%'  """.format(args.get('Name')))
        if int(args.get('Type', '0')) != 0:
            where_sql_list.append(r""" t1.type = {} """.format(args.get('Type')))
        if 'question_all_show' not in self._permissions:
            where_sql_list.append(r""" t1.type = 2 """)
        page = int(args.get('Page', '1'))
        pagesize = int(args.get('PageSize', '10'))
        temp = ''
        if where_sql_list:
            temp += ' where '
            temp += ' and '.join(where_sql_list)
        temp += ' limit {}, {};'.format((page - 1) * pagesize, pagesize)
        return temp

    def views(self):
        args = self.args
        if int(args.get('ID', '0')) == 0:
            query_sql = self.query_sql + self.main_query(args)
        else:
            query_sql = self.query_sql + r""" where t1.id={}; """.format(args.get('ID'))
        result = self._db.query(query_sql)
        total = self._db.query(self.get_total_row)
        for item in result:
            if item['Answer'] is not None and item['Answer'] != '':
                item['Answer'] = self.read_file(item['Answer'])
            if item['Time'] is not None and item['Time'] != '':
                item['Time'] = self.time_to_str(item['Time'])
        self.success['result'] = result
        self.success['total'] = total[0]['total_row']
        return jsonify(self.success)


class InsertQuestion(QuestionBase):

    def __init__(self):
        super(InsertQuestion, self).__init__()
        self.api_permission = 'question_edit'

    def save_file(self, content, base='/file'):
        ticket = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
        temp = ''
        for i in range(10):
            temp += random.choice(ticket)
        new_base = os.path.join(static_dir, *base.split(r'/'))
        if not os.path.exists(new_base):
            os.makedirs(new_base)
        new_name = str(int(time.time())) + '_' + temp + '.txt'
        try:
            with open(os.path.join(new_base, new_name), 'w') as f:
                f.write(content)
        except Exception as e:
            print(e)
        return base + '/' + new_name

    def rewrite_file(self, content, path):
        try:
            with open(os.path.join(static_dir, *path.split('/')), 'w') as f:
                f.write(content)
        except Exception as e:
            print(e)

    def views(self):
        args = self.args
        if self.args_is_null('Name', 'Type'):
            return jsonify(status_code.CONTENT_IS_NULL)
        if int(args.get('ID', '0')) == 0:
            # 创建
            file_path = self.save_file(args.get('Answer'))
            insert_sql = r"""insert into tb_question(Name, Type, Answer, Creator) 
                        value ('{}', {}, '{}', {})
                        """.format(
                args.get('Name'),
                args.get('Type'),
                file_path, self._uid
            )
            self._db.insert(insert_sql)
        else:
            query_sql = r"""select id, answer from tb_question where id = {};""".format(args.get('ID', 0))
            result = self._db.query(query_sql)
            if not result:
                return jsonify(status_code.CONTENT_IS_NULL)
            self.rewrite_file(args.get('Answer', ''), result[0]['answer'])
            update_sql = r"""update tb_question set Name='{}',Type={}, Creator={} where id={}""".format(
                args.get('Name'),
                args.get('Type'), self._uid, args.get('ID')
            )
            self._db.update(update_sql)
        return jsonify(self.success)


class DeleteQuestion(QuestionBase):

    def __init__(self):
        super(DeleteQuestion, self).__init__()
        self.api_permission = 'question_all_show'
        self._tb_name = 'tb_question'

    def views(self):
        args = self.args
        delete_sql = r"""delete from {} where id = {}""".format(self._tb_name, args.get('ID'))
        try:
            self._db.delete(delete_sql)
            return jsonify(status_code.SUCCESS)
        except Exception as e:
            return jsonify(status_code.DB_ERROR)
