# -*- coding: utf-8 -*- 
# @Time : 2019/12/23 15:34 
# @Author :  
# @Site :  
# @File : parseCSVBase.py 
# @Software: PyCharm
import pandas as pd
from pandas import DataFrame


class analyseFile:

    def __init__(self, file_path: str, model: object, sheetname: str = None):
        self.file = file_path
        self.data = None
        self.model = model
        self.sheetname = sheetname
        self.has_none_row_indexs = []
        self.error_data_list = []
        self.not_has_none_datas = None
        self.get_data()

    def get_data(self):
        if self.sheetname:
            self.data = pd.read_excel(self.file, sheet_name=self.sheetname, dtype=str)
        else:
            self.data = pd.read_excel(self.file, dtype=str)

    @staticmethod
    def check_file_type(file_path: str) -> bool:
        """
        检查文件类型
        :return:如果格式正确则返回True
        """
        if file_path.split('.')[1].lower() not in ['xls', 'xlsx']:
            return False
        return True

    def get_none_data(self) -> (list, DataFrame):
        """
        以必填字段切割有效数据和无效数据
        :return:必填字段为空的错误数据行的索引， 有数据的行构成的DataFrame
        """
        # 修改为自己的列名：转化为模型里面的列名
        self.data.rename(columns=self.model.columns_map, inplace=True)
        self.has_none_row_indexs = []
        self.not_has_none_datas = self.data
        if self.model.check_columns:
            self.has_none_row_indexs = self.data[
                self.data[self.model.check_columns].isnull().any(axis=1)].index.tolist()
            self.not_has_none_datas = self.data[self.data[self.model.check_columns].notnull().all(axis=1)]
        return self.has_none_row_indexs, self.not_has_none_datas

    def to_dict_list(self):
        """
        把不为空的数据行转换为对象列表
        :return:
        """
        # temp = self.not_has_none_datas.isnull()
        # self.not_has_none_datas = self.not_has_none_datas.astype(str)
        self.not_has_none_datas.fillna('', inplace=True)
        temp_list = []
        for i in range(self.not_has_none_datas.shape[0]):
            # 检查模型字段是否为空
            item = self.not_has_none_datas.iloc[i].to_dict()
            temp_list.append(item)
        return temp_list

    def model_check_data(self):
        self.model.check_field(self)

    @property
    def error_data(self) -> DataFrame:
        return self.data.iloc[list(set(self.data.index.to_list()) - set(self.not_has_none_datas.index.to_list()))]
