# -*- coding: utf-8 -*-
# @Time : 2019/11/12
# @Author : zhang
# @Site :
# @File : push_attend.py
# @Software: PyCharm
import datetime

from utils.sqlutils import OPMysql


class PushAttend:

    def __init__(self, args):
        self.db = OPMysql()
        self.args = args
        self.args['date_time'] = datetime.datetime.strptime(self.args['date_time'], '%Y-%m-%d %H:%M:%S')
        self.args['year'] = self.args['date_time'].year
        self.args['month'] = self.args['date_time'].month
        self.args['day'] = self.args['date_time'].day

    def check_in_or_out(self):
        if isinstance(self.args['pass_type'], str):
            self.args['pass_type'] = int(self.args['pass_type'])
        noon = datetime.datetime(self.args['year'], self.args['month'], self.args['day'], 13)
        if self.args['pass_type']:
            # 进
            if self.args['date_time'] < noon:
                return 1, 'amin'
            else:
                return 3, 'pmin'
        else:
            # 出
            if self.args['date_time'] < noon:
                return 2, 'amout'
            else:
                return 4, 'pmout'

    def check_has_data(self):
        query_sql = r"""select * from tb_attendance 
                where laborid = {laborid} and projectid ={projectid} and year={year} and month ={month} and day={day};
            """.format(**self.args)
        result = self.db.query(query_sql)
        if not result:
            return None
        return result[0]

    def insert_or_update(self, is_insert, in_out, pos):
        if is_insert:
            insert_sql = r"""insert into tb_attendance(laborid, projectid, year, month, day, {0}, {1})
                value ({laborid}, {projectid}, {year},{month},{day}, '{date_time}','{device_no}');
                """.format(in_out, pos, **self.args)
            self.db.insert(insert_sql)
        else:
            update_sql = r"""update tb_attendance set {0}='{date_time}', {1}='{device_no}'
                where laborid='{laborid}' and projectid='{projectid}' and year='{year}' and month='{month}' and day='{day}';
             """.format(in_out, pos, **self.args)
            self.db.update(update_sql)

    def str_to_datetime(self, str):
        return datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S")

    def need_deal_data(self, t_id, field, data):
        if data[field] is None or data[field] == '':
            return True
        data_time = self.str_to_datetime(data[field])
        if t_id % 2:
            if data_time > self.args['date_time']:
                return True
        else:

            if data_time < self.args['date_time']:
                return True
        return False
