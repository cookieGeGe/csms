from json import dumps, loads

import re

from utils.ImportTemp import ImportFileBase


class FileImportProject(ImportFileBase):

    def __init__(self, files, colnames, db):
        super(FileImportProject, self).__init__(files, colnames, db)
        self.table_name = 'tb_project'
        self.insert_sql = r"""insert into tb_project(name,type,guarantype,price,duration,gamount,prinpical,
            wagepercent,starttime,endtime,address,build,cons,consmanager,ownermanager,
            description,status,pid,cid,did,total,totalpay,issue, subcompany, bank, account) value('{Name}', {Type}, {GuaranType}, '{Price}', 
            {Duration}, '{GAmount}', '{PrinPical}', '{WagePercent}', '{StartTime}', '{EndTime}', '{Address}', {Build},
            {Cons}, {ConsManager}, {OwnerManager}, '{Description}', 0,
            {Province}, {City}, {District},'0', '0', '0', '{SubCompany}', '{Bank}', '{Account}')"""

    def formatter_type(self):
        type_list = ['政府投资', '民营开发', '国企分包', '其他']
        guarantype_list = ['投标', '履约', '预付款', '农民工工资支付', '业主支付', '质量', '资本金', '房屋质量', '其他']
        type_back = True
        g_back = True
        if self.item.get('Type', '') in type_list:
            self.item['Type'] = type_list.index(self.item.get('Type'))
            type_back = False
        if self.item.get('GuaranType', '') in guarantype_list:
            self.item['GuaranType'] = guarantype_list.index(self.item.get('GuaranType'))
            g_back = False
        if type_back or g_back:
            return True
        else:
            return False

    def formatter_area(self):
        for key in ('PID', 'CID', 'DID'):
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
            subcompany = self.item.get('SubCompany').replace('；', ';').split(';')
            for info in subcompany:
                temp_list = info.split(',')
                if len(temp_list) != 4:
                    continue
                query_sql = r"""select id, phone from tb_company where name='{}';""".format(temp_list[0])
                result = self.db.query(query_sql)
                if not result:
                    continue
                name_index = result[0]['phone'].find(temp_list[1])
                if name_index == -1:
                    continue
                temp = {
                    'ID': result[0]['id'],
                    'Person': ' '.join(temp_list[1:])
                }
                sub.append(temp)
        return sub

    def formatter_prinpical(self):
        if self.item.get('PrinPical', '') != '':
            con_str = self.item.get('PrinPical')
            if con_str != '':
                self.item['PrinPical'] = re.sub('；', ';', self.item.get('PrinPical'))
                person_list = self.item['PrinPical'].split(';')
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
                self.item['PrinPical'] = dumps(persons, ensure_ascii=False)
            else:
                self.item['PrinPical'] = dumps([], ensure_ascii=False)
        else:
            self.item['PrinPical'] = dumps([], ensure_ascii=False)

    def formatter_manager(self):
        for key in ('Cons', 'Owner'):
            temp_manager = self.item.get(key + 'Manager', '')
            if temp_manager != '':
                temp_manager = re.sub('，', ',', temp_manager)
                temp_manager = re.sub('；', ';', temp_manager)
                manager_list = temp_manager.split(';')
                if manager_list:
                    result = []
                    for item in manager_list:
                        split_item = item.split(',')
                        if len(split_item) != 3:
                            continue
                        tempid = self.item[key] if key != 'Owner' else self.item['Build']
                        query_sql = r"""select phone from tb_company where id = {} 
                                        and  CONCAT(IFNULL(phone,'')) LIKE '%{}%' ;""".format(
                            tempid, split_item[0]
                        )
                        temp_result = self.db.query(query_sql)
                        if temp_result:
                            result.append(' '.join(split_item))
                    if not result:
                        return True
                    else:
                        self.item[key + 'Manager'] = ';'.join(result)
                        return False
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
            self.item['SubCompany'] = dumps(result, ensure_ascii=False)
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
