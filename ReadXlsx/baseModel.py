# -*- coding: utf-8 -*- 
# @Time : 2019/12/23 16:16 
# @Author :  
# @Site :  
# @File : baseModel.py 
# @Software: PyCharm
import pandas as pd
from abc import ABCMeta, abstractmethod


class BaseXlsxModel(metaclass=ABCMeta):
    columns_map = {}

    def __init__(self):
        self.columns = self.columns_map.values()
        self.parsefile = None
        self.check_columns_map = self.set_check_columns_map()
        self.check_columns = self.check_columns_map.keys()

    @abstractmethod
    def set_check_columns_map(self):
        pass

    def check_columns_func(self, check_func):
        self.parsefile.not_has_none_datas = self.parsefile.not_has_none_datas[
            self.parsefile.not_has_none_datas.apply(check_func, axis=1)]
        print(self.parsefile.not_has_none_datas)

    def check_field(self, parsefile: object):
        """
        字段校验
        :return:
        """
        self.parsefile = parsefile
        for func in self.check_columns_map.values():
            if func is None or func == '':
                continue
            self.check_columns_func(func)


class BankModel(BaseXlsxModel):
    columns_map = {
        "name": "姓名",
        "number": "身份证号码",
        "type": "工资",
    }

    def __init__(self, db, wage_id):
        super(BaseXlsxModel, self).__init__()
        self.db = db
        self.wage_id = wage_id

    def set_check_columns_map(self) -> dict:
        return {
            "工资": self.check_wage,
        }

    def formatter_wage(self, value):
        if value is None or value == '':
            return 0
        if isinstance(value, str):
            return eval(value)
        return value

    def check_wage(self, item):
        # return True if item['电话'] % 2 == 1 else False
        query_sql = r"""
            select t2.id,t2.total from tb_wage as t1
            left join tb_salary as t2 on t1.year=t2.year and t1.month = t2.month
            left join tb_laborinfo as t3 on t1.projectid = t3.ProjectID
            where t1.id = {} and t3.IDCard = {}
        """.format(self.wage_id, item['身份证号码'])
        result = self.db.query(query_sql)
        if result:
            if self.formatter_wage(result[0]['totel']) == self.formatter_wage(item['工资']):
                update_sql = """
                    update tb_salary set realtotal='{}' where id='{}';
                """.format(item['工资'])
                self.db.update(update_sql)
