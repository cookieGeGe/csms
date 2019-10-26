# -*- coding: utf-8 -*-
# @Time : 2019/10/13
# @Author : zhang
# @Site :
# @File : ImportGuarantee.py
# @Software: PyCharm
from utils.ImportTemp import ImportFileBase


class FileImportGuarantee(ImportFileBase):

    def __init__(self, files, colnames, db):
        super(FileImportGuarantee, self).__init__(files, colnames, db)
        self.table_name = 'tb_guarantee'
        self.key_list = {
            'Province': 'PID',
            'City': 'CID',
            'District': 'DID'
        }

    def formatter_key(self):
        for key in self.key_list.keys():
            self.item[self.key_list[key]] = self.item[key]
            del self.item[key]

    def check_field_is_null(self):
        for key in self.item.keys():
            if key == 'Description':
                continue
            if self.item[key] == '' or self.item[key] is None:
                return True
        return False

    def formatter_category(self):
        category_list = ['投标', '履约', '预付款', '农民工工资支付', '业主支付', '质量', '资本金', '房屋质量', '其他']
        self.item['Category'] = category_list.index(self.item.get('Category'))
        if self.item.get('Category', '') == -1:
            return True
        return False

    def check_field(self):
        self.formatter_area()
        self.item['Name'] = self.item['Number']
        field_is_null = self.check_field_is_null()
        in_category = self.formatter_category()
        if field_is_null or in_category:
            return True
        return False

    def check_mysql(self):
        query_sql = r"""select id from {} where Number='{}'""".format(self.table_name, self.item.get('Number'))
        result = self.db.query(query_sql)
        if result:
            return True
        return False

    def save(self):
        data_list = self.file_data.excel_data()
        for item in data_list:
            self.item = item
            try:
                check_field = self.check_field()
                self.formatter_key()
                check_mysql = self.check_mysql()
                # print(self.formatter_insert_sql())
                if check_mysql or check_field:
                    if len(self.bad_info) < 20:
                        self.bad_info.append(item.get('Name'))
                    self.total_bad += 1
                    continue
                # print(self.formatter_insert_sql())
                self.db.insert(self.formatter_insert_sql())
            except Exception as e:
                print(e)
                if len(self.bad_info) < 20:
                    self.bad_info.append(item.get('Name'))
                self.total_bad += 1
                continue
