import datetime
from json import dumps, loads

import re

from utils.ImportTemp import ImportFileBase


class FileImportLabor(ImportFileBase):

    def __init__(self, files, colnames, db):
        super(FileImportLabor, self).__init__(files, colnames, db)
        self.insert_sql = r"""insert into tb_laborinfo(Name, Age,Sex,Birthday,Address, Nationality,IDCard,Phone,CompanyID,
                          JobType, ClassID, Identity, DepartureDate,EntryDate,Hardhatnum,Education,CreateTime,
                        ProjectID,IsPM,IssueAuth,Political,Train,EmerCon,PID,CID,DID,SVP,EVP,Superiors,IsLeader,
                        Remark, FeeStand, isFeeStand,Badrecord,isbadrecord)
                         value ('{Name}',{Age},{Sex},'{Birthday}','{Address}','{Nationality}','{IDCard}','{Phone}',
                         {CompanyID},{JobType},{ClassID},0,'{DepartureDate}','{EntryDate}','{Hardhatnum}',
                         '{Education}','{CreateTime}',{ProjectID},{IsPM},'{IssueAuth}','{Political}',
                         '{Train}','{EmerCon}',{Province},{City},{District},'{SVP}','{EVP}',{SuperiorsID},{IsLeader},
                         '{Remark}','{FeeStand}', {isFeeStand}, '{Badrecord}','{BadRecord}')"""

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
                self.item.get('ProjectID'), self.item.get('ClassID', self.item.get('CompanyID')))
            id = self.db.insert(insert_sql)
            self.item['IsLeader'] = 1
            self.item['ClassID'] = id
            return False
        else:
            query_sql = r"""select id from tb_class where projectid={} and companyid={} and classname='{}';""".format(
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
                query_sql = r"""select id in tb_area where Name='{}';""".format(self.item.get(key))
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
        self.item['Badrecord'] = '0'
        self.item['Sex'] = 1 if self.item.get('Sex', '男') == '男' else 0
        self.item['IsPM'] = 1 if self.item.get('IsPM', '否') != '否' else 0
        self.item['isFeeStand'] = 1 if self.item.get('isFeeStand', '否') != '否' else 0
        jobtype_list = ['钢筋工', '架子工', '模板工', '通风工', '机械设备安装工']
        self.item['JobType'] = jobtype_list.index(self.item.get('JobType', '钢筋工'))

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

    def check_mysql(self):
        query_sql = r"""select id from tb_laborinfo where idcard='{}';""".format(self.item.get('IDCard'))
        result = self.db.query(query_sql)
        if result:
            return True
        return False
