import datetime
from json import dumps, loads

import re

from utils.ImportTemp import ImportFileBase


class FileImportLabor(ImportFileBase):

    def __init__(self, files, colnames, db):
        super(FileImportLabor, self).__init__(files, colnames, db)
        self.table_name = 'tb_laborinfo'
        self.insert_sql = r"""insert into tb_laborinfo(Name, Age,Sex,Birthday,Address, Nationality,IDCard,Phone,CompanyID,
                          JobType, ClassID, Identity, DepartureDate,EntryDate,Hardhatnum,Education,CreateTime,
                        ProjectID,IsPM,IssueAuth,Political,EmerCon,PID,CID,DID,Superiors,IsLeader,
                        Remark, FeeStand, isFeeStand,Badrecord,isbadrecord,Train)
                         value ('{Name}',{Age},{Sex},'{Birthday}','{Address}','{Nationality}','{IDCard}','{Phone}',
                         {CompanyID},{JobType},{ClassID},0,'{DepartureDate}','{EntryDate}','{Hardhatnum}',
                         '{Education}','{CreateTime}',{ProjectID},{IsPM},'{IssueAuth}','{Political}',
                         '{EmerCon}',{Province},{City},{District},{SuperiorsID},{IsLeader},
                         '{Remark}','{FeeStand}', {isFeeStand}, '{Badrecord}','{isBadRecord}','{Train}')"""
        self.key_list = {
            'Province': 'PID',
            'City': 'CID',
            'District': 'DID',
            'SuperiorsID': 'Superiors',
        }

    def formatter_company(self):
        query_sql = r"""select id from tb_company where name='{}';""".format(self.item.get('CompanyID', ''))
        result = self.db.query(query_sql)
        if result:
            self.item['CompanyID'] = result[0]['id']
            return False
        return True

    def formatter_project(self):
        query_sql = r"""select id from tb_project where name='{}';""".format(self.item.get('ProjectID', ''))
        result = self.db.query(query_sql)
        if result:
            self.item['ProjectID'] = result[0]['id']
            return False
        return True

    def formatter_classID(self):
        if self.item.get('IsLeader', '是') == '是':
            insert_sql = r"""insert into tb_class(projectid, classname, companyid) value ({},'{}',{});""".format(
                self.item.get('ProjectID'), self.item.get('ClassID'), self.item.get('CompanyID'))
            id = self.db.insert(insert_sql)
            self.item['IsLeader'] = 1
            self.item['ClassID'] = id
            return False
        else:
            query_sql = r"""select id from tb_class where projectid='{}' and companyid='{}' and classname='{}';""".format(
                self.item.get('ProjectID'),
                self.item.get('CompanyID'),
                self.item.get('ClassID'))
            result = self.db.query(query_sql)
            if not result:
                return True
            else:
                self.item['IsLeader'] = 0
                self.item['ClassID'] = result[0]['id']
                return False

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

    def formatter_superiors(self):
        if self.item.get('SuperiorsID', '') == '':
            self.item['SuperiorsID'] = 0
            return False
        else:
            query_sql = r"""select id from tb_laborinfo where name='{}' and projectid={} and companyid={};""".format(
                self.item.get('Name'), self.item.get('ProjectID'), self.item.get('CompanyID'))
            result = self.db.query(query_sql)
            if result:
                self.item['SuperiorsID'] = result[0]['id']
                return False
            else:
                return True

    def formatter_public(self):
        self.item['CreateTime'] = datetime.datetime.now()
        self.item['Identity'] = 0
        self.item['Badrecord'] = 1 if self.item.get('Badrecord', '') != '' else 0
        # self.item['isBadRecord'] = self.item['Badrecord']
        self.item['Sex'] = 1 if self.item.get('Sex', '男') == '男' else 0
        self.item['IsPM'] = 1 if self.item.get('IsPM', '否') != '否' else 0
        self.item['isFeeStand'] = 1 if self.item.get('isFeeStand', '否') != '否' else 0
        self.item['Train'] = 1 if self.item.get('Train', '否') != '否' else 0
        if self.item.get('JobType', '') != '':
            jobtype_list = ['钢筋工', '架子工', '模板工', '通风工', '机械设备安装工']
            self.item['JobType'] = jobtype_list.index(self.item.get('JobType', '钢筋工'))
            if self.item['JobType'] == -1:
                self.item['JobType'] = ''
        if self.item.get('Education', '') != '':
            jobtype_list = ['无', '小学', '初中', '高中', '大学', '硕士', '博士']
            self.item['Education'] = jobtype_list.index(self.item.get('Education', '无'))
            if self.item['Education'] == -1:
                self.item['Education'] = ''
        else:
            self.item['JobType'] = 0
        if self.item.get('isbadrecord', '') != '':
            badrecord_list = ['正常', '不良', '黑名单']
            self.item['isbadrecord'] = badrecord_list.index(self.item.get('isbadrecord', '正常'))
            if self.item['isbadrecord'] == -1:
                self.item['isbadrecord'] = 0
        else:
            self.item['isbadrecord'] = 0

    def check_field(self):
        self.formatter_area()
        self.formatter_public()
        for_company = self.formatter_company()
        for_project = self.formatter_project()
        for_class = self.formatter_classID()
        for_super = self.formatter_superiors()
        if for_company or for_project or for_class or for_super:
            return True
        return False

    def formatter_key(self):
        for key in self.key_list.keys():
            self.item[self.key_list[key]] = self.item[key]
            del self.item[key]

    def check_mysql(self):
        query_sql = r"""select id from tb_laborinfo where idcard='{}';""".format(self.item.get('IDCard'))
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
