import datetime
from abc import ABCMeta, abstractmethod

import xlrd
from xlrd import xldate_as_datetime


class TempColnames():
    ATTEND = ['name', 'idcard', 'atime', 'amin', 'amout', 'pmin', 'pmout']
    COMPANY = ['Name', 'Leage', 'Address', 'Type', 'Province', 'City', 'District', 'Connection', 'Description',
               'BadRecord']
    PROJECT = ['Name', 'Type', 'GuaranType', '{Price}', 'Duration', 'GAmount', 'PrinPical', 'WagePercent', 'StartTime',
               'EndTime', 'Address', 'Build', 'Cons', 'ConsManager', 'OwnerManager', 'LaborManager', 'Supervisor',
               'Description', 'Province', 'City', 'District']
    LABOR = ['Name', 'Age', 'Sex', 'Birthday', 'Address', 'Nationality', 'IDCard', 'Phone', 'CompanyID', 'JobType',
             'ClassID', 'DepartureDate', 'EntryDate', 'Hardhatnum', 'Education', 'CreateTime', 'ProjectID', 'IsPM',
             'IssueAuth', 'Political', 'Train', 'EmerCon', 'Province', 'City', 'District', 'SVP', 'EVP', 'SuperiorsID',
             'IsLeader', 'Remark', 'FeeStand', 'isFeeStand', 'Badrecord']


class Data_Excel():


    def __init__(self, excel_file, col_names):
        self.file = excel_file
        self.dict_name = col_names

    def init(self):
        self.data = xlrd.open_workbook(file_contents=self.file)
        self.table = self.data.sheet_by_index(0)
        self.colnames = self.table.row_values(0)
        self.nrows = self.table.nrows

    def data_format(self, cell, ctype):
        # ctype = sheet.cell(i, j).ctype  # 表格的数据类型
        # cell = sheet.cell_value(i, j)
        if ctype == 2 and cell % 1 == 0:  # 如果是整形
            cell = int(cell)
        elif ctype == 3:
            # 转成datetime对象
            cell = xldate_as_datetime(cell, 0)
        elif ctype == 4:
            cell = True if cell == 1 else False
        return cell

    def excel_data(self):
        self.init()
        if self.colnames.__len__() == self.dict_name.__len__():
            for rownum in range(1, self.nrows):
                row = self.table.row_values(rownum)
                app = {}  # 以字典返回，至于字典中有多少元素主要看有多少列
                if row:
                    for i in range(len(self.colnames)):  # 在这个Excel中，列所在的行有两个数据，所以没循环一行就以这两个数据为键，行数的值为键的值，保存在一个字典里
                        ctype = self.table.cell(rownum, i).ctype
                        cell = self.table.cell_value(rownum, i)
                        app[self.dict_name[i]] = self.data_format(cell, ctype)
                yield app
        else:
            yield {}


class ImportFileBase(metaclass=ABCMeta):

    def __init__(self, files, colnames, db):
        self.colnames = colnames
        self.db = db
        self.file = files
        self.insert_sql = r""""""
        self.file_data = Data_Excel(self.file, self.colnames)
        self.item = {}
        self.bad_info = []
        self.total_bad = 0

    @abstractmethod
    def check_field(self):
        pass

    @abstractmethod
    def check_mysql(self):
        pass

    @property
    def bad_list(self):
        return self.bad_info, self.total_bad

    def save(self):
        for item in self.file_data.excel_data():
            self.item = item
            try:
                check_field = self.check_field()
                check_mysql = self.check_mysql()
                if check_mysql or check_field:
                    if len(self.bad_info) < 20:
                        self.bad_info.append(item.get('Name'))
                    self.total_bad += 1
                    continue
                self.db.insert(self.insert_sql.format(**item))
            except:
                if len(self.bad_info) < 20:
                    self.bad_info.append(item.get('Name'))
                self.total_bad += 1
                continue
