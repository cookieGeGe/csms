from json import dumps

import re

from utils.ImportTemp import ImportFileBase


class FileImportCompany(ImportFileBase):

    def __init__(self, files, colnames, db):
        super(FileImportCompany, self).__init__(files, colnames, db)
        self.insert_sql = r""" insert into tb_company(Name, Legal, Address, Type, ProvinceID, CityID, Districtid, Phone, 
        Description,BadRecord, HasBadRecord, otherinfo) value ('{Name}', '{Leage}', '{Address}', {Type}, {Province}, {City}, {District}, 
        '{Phone}', '{Description}','{BadRecord}',{HasBadRecord}, '{OtherInfo}')"""

    def formatter_area(self):
        for key in ('Province', 'City', 'District'):
            if self.item.get(key, '') != '':
                query_sql = r"""select id from tb_area where Name='{}';""".format(self.item.get(key))
                result = self.db.query(query_sql)
                if result:
                    self.item[key] = result[0]['id']
                else:
                    self.item[key] = 0
            else:
                self.item[key] = 0

    def formatter_type(self):
        type_list = ['施工企业', '监理单位', '勘察设计', '劳务公司', '房地产开发', '政府及事业单位', '其他业主单位', '其他']
        if self.item.get('Type', '') in type_list:
            self.item['Type'] = type_list.index(self.item.get('Type'))
            return False
        return True

    def formatter_connection(self):
        """
        格式化联系人
        :return:
        """
        if self.item.get('Connection', '') != '':
            con_str = self.item.get('Connection')
            if con_str != '':
                self.item['Connection'] = re.sub('；', ';', self.item.get('Connection'))
                person_list = self.item['Connection'].split(';')
                persons = []
                for person in person_list:
                    person = re.sub('，', ',', person)
                    one_person = person.split(',')
                    if len(one_person) != 4:
                        continue
                    persons.append({
                        'name': one_person[0],
                        'pos': one_person[1],
                        'phone': one_person[2],
                        'projectName': one_person[3]
                    })
                self.item['Phone'] = dumps(persons)
            else:
                self.item['Phone'] = dumps([])
        else:
            self.item['Phone'] = dumps([])

    def check_field(self):
        try:
            if self.formatter_type():
                return True
            self.formatter_area()
            if self.item.get('HasBadRecord', '') != '':
                badrecord_list = ['正常', '风险', '黑名单']
                self.item['HasBadRecord'] = badrecord_list.index(self.item.get('HasBadRecord', '正常'))
                if self.item['HasBadRecord'] == -1:
                    self.item['HasBadRecord'] = 0
            else:
                self.item['HasBadRecord'] = 0
            self.item['BadRecord'] = self.item['HasBadRecord']
            self.formatter_connection()
            return False
        except:
            return True

    def check_mysql(self):
        query_sql = r"""select id from tb_company where name='{}';""".format(self.item.get('Name'))
        result = self.db.query(query_sql)
        if result:
            return True
        return False
