# -*- coding: utf-8 -*-
# @Time : 2020/1/21
# @Author : zhang
# @Site :
# @File : addpermission.py
# @Software: PyCharm
from utils.sqlutils import OPMysql


class AddPermission(object):

    def __init__(self):
        self.user_list = [1, 2, 3, 4, 17, 19, 28, 29, 30]
        self.add_permission_list = [i for i in range(25, 32, 1)]

    def insert(self, value_list):
        insert_sql = r"""
            insert into tb_user_per(uid, pid) values {};
        """.format(','.join(value_list))
        print(insert_sql)

    def get_value_list(self):
        for userid in self.user_list:
            value_list = []
            for perid in self.add_permission_list:
                value_list.append(r"""({},{})""".format(userid, perid))
            self.insert(value_list)


if __name__ == '__main__':
    addPer = AddPermission()
    addPer.get_value_list()
