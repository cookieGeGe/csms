import datetime

import xlrd
from xlrd import xldate_as_datetime


class TempColnames():
    ATTEND = ['name', 'idcard', 'atime', 'amin', 'amout', 'pmin', 'pmout']


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
