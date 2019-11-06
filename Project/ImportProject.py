from json import dumps, loads

import re

from utils.ImportTemp import ImportFileBase


class FileImportProject(ImportFileBase):

    def __init__(self, files, colnames, db):
        super(FileImportProject, self).__init__(files, colnames, db)
        self.insert_sql = r"""insert into tb_project(name,type,guarantype,price,duration,gamount,prinpical,
            wagepercent,starttime,endtime,address,build,cons,consmanager,ownermanager,
            description,status,pid,cid,did,total,totalpay,issue, subcompany, bank, account) value('{Name}', {Type}, {GuaranType}, '{Price}', 
            {Duration}, '{GAmount}', '{PrinPical}', '{WagePercent}', '{StartTime}', '{EndTime}', '{Address}', {Build},
            {Cons}, {ConsManager}, {OwnerManager}, '{Description}', 0,
            {Province}, {City}, {District},'0', '0', '0', '{SubCompany}', '{Bank}', '{Account}')"""

    def formatter_type(self):
        type_list = ['政府投资', '民营开发', '国企分包', '其他']
        guarantype_list = ['投标', '履约', '预付款', '农民工工资支付', '业主支付', '质量', '资本金', '房屋质量', '其他']
        if self.item.get('Type', '') in type_list:
            self.item['Type'] = type_list.index(self.item.get('Type'))
            return False
        if self.item.get('GuaranType', '') in guarantype_list:
            self.item['GuaranType'] = guarantype_list.index(self.item.get('GuaranType'))
            return False
        return True

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

    def formatter_bank(self):
        if self.item.get('Bank') != '':
            query_sql = r"""select id from tb_bank where name='{}';""".format(self.item.get('Bank'))
            result = self.db.query(query_sql)
            if result:
                self.item['Bank'] = result[0]['id']
                return False
        return True

    def formatter_build_cons(self):
        for key in ('Build', 'Cons'):
            if self.item.get(key, '') != '':
                query_sql = r"""select id from tb_company where name = '{}';""".format(self.item.get(key))
                result = self.db.query(query_sql)
                if result:
                    self.item[key] = result[0]['id']
                else:
                    return True
            else:
                return True
        return False

    def formatter_subcompany(self):
        sub = []
        if self.item.get('SubCompany', '') != '':
            subcompany = self.item.get('SubCompany').replace('；', ';').plit(';')
            for info in subcompany:
                temp_list = info.split(',')
                if temp_list != 2:
                    continue
                query_sql = r"""select id from tb_company where name='{}';""".format(temp_list[0])
                result = self.db.query(query_sql)
                if not result:
                    continue
                temp = {
                    'ID': result[0]['id'],
                    'Person': temp_list[1]
                }
                sub.append(temp)
        return sub

    def formatter_prinpical(self):
        if self.item.get('PrinPical', '') != '':
            con_str = self.item.get('PrinPical')
            if con_str != '':
                self.item['PrinPical'] = re.sub('；', ';', self.item.get('PrinPical'))
                person_list = self.item['Connection'].split(';')
                persons = []
                for person in person_list:
                    person = re.sub('，', ',', person)
                    one_person = person.split(',')
                    if len(one_person) == 4:
                        persons.append({
                            'name': one_person[0],
                            'post': one_person[1],
                            'phone': one_person[2],
                            'projectName': one_person[3]
                        })
                    else:
                        continue
                self.item['PrinPical'] = dumps(persons)
            else:
                self.item['PrinPical'] = dumps([])
        else:
            self.item['PrinPical'] = dumps([])

    def formatter_manager(self):
        for key in ('ConsManager', 'OwnerManager'):
            temp_manager = self.item.get(key, '')
            if temp_manager != '':
                temp_manager = re.sub('，', ',', temp_manager)
                manager_list = temp_manager.split(',')
                if len(manager_list) == 4:
                    query_company = r"""select id,name,PrinPical from tb_project where name ='{}';""".format(
                        manager_list[0])
                    result = self.db.query(query_company)
                    if result:
                        self.item[key] = dumps({
                            'id': result[0]['id'],
                            'name': manager_list[0],
                            'pname': manager_list[1],
                            'post': manager_list[2],
                            'phone': manager_list[3]
                        })
                    else:
                        return True
                else:
                    return True
            else:
                return True
        return False

    def check_field(self):
        try:
            self.formatter_area()
            result = self.formatter_subcompany()
            if not result:
                return True
            self.item['SubCompany'] = dumps(result)
            if self.formatter_type() or self.formatter_bank() or self.formatter_build_cons() or self.formatter_manager():
                return True
            self.formatter_prinpical()
            return False
        except:
            return True

    def check_mysql(self):
        query_sql = r"""select id from tb_project where name='{}';""".format(self.item.get('Name'))
        result = self.db.query(query_sql)
        if result:
            return True
        return False