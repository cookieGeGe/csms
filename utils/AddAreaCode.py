# -*- coding: utf-8 -*-
# @Time : 2019/11/24
# @Author : zhang
# @Site :
# @File : AddAreaCode.py
# @Software: PyCharm
from json import dumps

from utils.sqlutils import OPMysql


class addAreaCode:

    def __init__(self):
        self.db = OPMysql()
        self.province = []
        self.export = {
            "province_list": {},
            "city_list": {},
            "county_list": {}
        }
        self.province = self.get_all_pro()

    def get_all_pro(self, fatherid=0):
        query_sql = r"""select * from tb_area where fatherid={};""".format(fatherid)
        return self.db.query(query_sql)

    def update_code(self, code, a_id):

        update_sql = r"""update tb_area set code = '{}' where id={};""".format(
            code, a_id
        )
        self.db.update(update_sql)

    def formatter(self):
        for index, item in enumerate(self.province):
            p_code = str(index + 1).zfill(2)
            self.update_code(p_code + '0000', item['ID'])
            print(p_code, item['Name'])
            city_list = self.get_all_pro(item['ID'])
            # 区循环
            for c_index, city in enumerate(city_list):
                c_code = str(c_index + 1).zfill(2)
                self.update_code(p_code + c_code + '00', city['ID'])
                distict_list = self.get_all_pro(city['ID'])
                for d_index, district in enumerate(distict_list):
                    d_code = str(d_index + 1).zfill(2)
                    self.update_code(p_code + c_code + d_code, district['ID'])

    def get_export_js(self):
        for index, item in enumerate(self.province):
            self.export['province_list'].update({
                item['Code']: item['Name']
            })

            city_list = self.get_all_pro(item['ID'])
            # 区循环
            for c_index, city in enumerate(city_list):
                self.export['city_list'].update({
                    city['Code']: city['Name']
                })
                distict_list = self.get_all_pro(city['ID'])
                for d_index, district in enumerate(distict_list):
                    self.export['county_list'].update({
                        district['Code']: district['Name']
                    })

        print('export default ' + dumps(self.export))


if __name__ == '__main__':
    add_code = addAreaCode()
    # add_code.formatter()
    add_code.get_export_js()
