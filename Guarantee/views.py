import datetime
import time
from json import dumps, loads

from copy import deepcopy

from flask import request, jsonify, session

from Company.views import CreatePicGroup
from User.util import save_image
from utils import status_code
from utils.BaseView import BaseView
from utils.pulic_utils import str_to_date


class GuaranteeBase(BaseView):

    def __init__(self):
        super(GuaranteeBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        return jsonify(status_code.SUCCESS)


class CreateGuarantee(GuaranteeBase):

    def __init__(self):
        super(CreateGuarantee, self).__init__()
        self.api_permission = 'guarantee_edit'

    def get_img_list(self, name):
        temp_files = request.files.get(name, '')
        img_url = ''
        if temp_files != '':
            img_url = save_image(temp_files, 'static/media/guarantee')
        return img_url

    def create_cguarantee(self, args, index):
        args['IDimg'] = self.get_img_list('IDimg_{}'.format(index))
        args['Pimg'] = self.get_img_list('Pimg_{}'.format(index))
        args['GID'] = 0
        insert_sql = r"""insert into tb_cguarantee(Name,IDCard,Address, Phone,Area,Pvalue,Proportion,Paddress,IDimg,
                            Pimg,GID) value ('{Name}','{IDCard}','{Address}','{Phone}','{Area}','{Pvalue}','{Proportion}',
                            '{Paddress}','{IDimg}','{Pimg}',{GID});""".format(**args)
        cguarantee_id = self._db.insert(insert_sql)
        return cguarantee_id

    def update_img(self, cid, ids):
        ids = loads(ids)
        if ids:
            temp_ids = ''
            for index, id in enumerate(ids):
                temp_ids += str(id)
                if index < len(ids) - 1:
                    temp_ids += ','

            update_sql = r"""update tb_pic_group set cid={} where id in ({});""".format(cid, temp_ids)
            self._db.update(update_sql)

    def views(self):
        is_null = self.args_is_null('Expiretime', 'Duration', 'ProjectID', 'CompanyID', 'GuaCompany', 'Capital',
                                    'Nature', 'Name', 'Amount', 'Kind', 'Deadline', 'SignTime', 'Category', 'Totalrate',
                                    'Total', 'RealAC', 'Marginratio', 'Margin', 'Bene', 'PID', 'CID', 'DID')
        if is_null:
            return jsonify(status_code.CONTENT_IS_NULL)
        args = self.args
        # 时间格式化
        # print(args)
        args['Expiretime'] = str_to_date(args['Expiretime'])
        args['Duration'] = str_to_date(args['Duration'])
        args['SignTime'] = str_to_date(args['SignTime'])
        # args['SignTime'] = datetime.datetime.now() + datetime.timedelta(hours=8)
        # args['Number'] = 'BSHS-' + str(int(time.time() * 1000))
        args['Number'] = args['Name']
        insert_sql = r"""insert into tb_guarantee(CompanyID,Capital, Nature,Name,Number,Amount,Kind,ProjectID,SignTime,
            Category, Deadline, Expiretime,Totalrate,Total,RealAC,Marginratio,Margin,Bene,PID,CID,DID,Description,
            Duration,GuaCompany,Address,createuser)
            value ('{CompanyID}','{Capital}','{Nature}','{Name}','{Number}','{Amount}','{Kind}','{ProjectID}','{SignTime}',
            {Category},'{Deadline}','{Expiretime}','{Totalrate}','{Total}','{RealAC}','{Marginratio}','{Margin}',
            '{Bene}',{PID},{CID},{DID},'{Description}','{Duration}', '{GuaCompany}','{Address}', {0});""".format(
            self._uid, **args
        )
        guarantee_id = self._db.insert(insert_sql)
        self.update_img(guarantee_id, args.get('group_list', '[]'))
        c_list = []
        if args.get('CGuarantee_list', '') != '':
            cguarantee_list = loads(args.get('CGuarantee_list', ''))
            for index, cguarantee in enumerate(cguarantee_list):
                c_list.append(self.create_cguarantee(cguarantee, index))
        if c_list:
            ids = ''
            for index, cgid in enumerate(c_list):
                ids += str(cgid)
                if index < len(c_list) - 1:
                    ids += ','
            update_sql = r"""update tb_cguarantee set GID={} where id in ({})""".format(guarantee_id, ids)
            self._db.update(update_sql)
        return jsonify(status_code.SUCCESS)


class QueryGuarantee(GuaranteeBase):

    def __init__(self):
        super(QueryGuarantee, self).__init__()
        self.is_admin = 0
        self.api_permission = 'guarantee_show'

    def admin(self):
        # query_sql = r"""select t2.* from tb_project as t1
        #                 right join tb_guarantee as t2 on t1.name = t2.projectid
        #                 where t1.id in ({})""".format(','.join(self.get_project_ids()))
        # self.ids = self.set_ids(query_sql)
        self.is_admin = 1
        return self.views()

    def main_query(self, query_sql, args, has_limit):
        where_list = []
        # if self.ids != None:
        #     if not self.ids:
        #         self.ids = [0, ]
        #     where_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if self.is_admin == 1:
            where_list.append(r""" t1.CreateUser = {} """.format(self._uid))
        for name in ('Number', 'Kind', 'Bene', 'Total'):
            if args.get(name, '') != '':
                where_list.append(r""" CONCAT(IFNULL(t1.{},'')) LIKE '%{}%' """.format(name, args.get(name)))
        if args.get('CompanyName', '') != '':
            where_list.append(r""" CONCAT(IFNULL(t1.GuaCompany, '')) like '%{}%' """.format(args.get('CompanyName')))
        if args.get('ProjectName', '') != '':
            where_list.append(r""" CONCAT(IFNULL(t1.ProjectID, '')) like '%{}%' """.format(args.get('ProjectName')))
        if int(args.get('DID', 0)):
            where_list.append(r""" t1.DID={} """.format(args.get('DID')))
        if int(args.get('CID', 0)):
            where_list.append(r""" t1.CID={} """.format(args.get('CID')))
        if int(args.get('PID', 0)):
            where_list.append(r""" t1.PID={} """.format(args.get('PID')))
        if args.get('StartTime', '') != '':
            starttime = str_to_date(args['StartTime'])
            where_list.append(r""" t1.SignTime > '{}' """.format(starttime))
        if args.get('EndTime', '') != '':
            endtime = str_to_date(args['EndTime'])
            where_list.append(r""" t1.Expiretime < '{}' """.format(endtime))
        if int(args.get('Category', 9)) != 9:
            where_list.append(r""" t1.Category = {} """.format(args.get('Category')))
        temp = ''
        if where_list:
            temp = ' where '
            for index, i in enumerate(where_list):
                temp += i
                if index < len(where_list) - 1:
                    temp += 'and'
        page = int(args.get('Page', 1))
        psize = int(args.get('PageSize', 10))
        if has_limit:
            limit_sql = r""" order by ID desc limit {},{};""".format((page - 1) * psize, psize)
            query_sql = query_sql + " " + temp + limit_sql
        else:
            query_sql = query_sql + ' ' + temp
        return query_sql

    def get_group_info(self, id):
        select_sql = r"""select * from tb_pic_group where cid={} and ptype=3;""".format(id)
        data = self._db.query(select_sql)
        return data

    def views(self):
        args = self.args
        query_sql = r"""select SQL_CALC_FOUND_ROWS t1.*, t4.name as Pname,t5.name as Cname, t6.name as Dname from tb_guarantee as t1
                        INNER JOIN tb_area as t4 on t1.PID = t4.id
                        INNER JOIN tb_area as t5 on t1.CID = t5.id
                        INNER JOIN tb_area as t6 on t1.DID = t6.id"""
        total_query_sql = r"""select SQL_CALC_FOUND_ROWS sum(t1.amount) as amount_total, sum(RealAC) as realac_total from tb_guarantee as t1
                        INNER JOIN tb_area as t4 on t1.PID = t4.id
                        INNER JOIN tb_area as t5 on t1.CID = t5.id
                        INNER JOIN tb_area as t6 on t1.DID = t6.id"""
        if int(args.get('ID', 0)) == 0:
            query_sql = self.main_query(query_sql, args, 1)
            total_query_sql = self.main_query(total_query_sql, args, 0)
        else:
            query_sql += r""" where t1.ID = {} """.format(args.get('ID'))
        # print(query_sql)
        result = self._db.query(query_sql)
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        nowdate = datetime.datetime.now()
        temp_result = []
        for item in result:
            item['SignTime'] = item['SignTime'].strftime("%Y-%m-%d")
            item['Expiretime'] = item['Expiretime'].strftime("%Y-%m-%d")
            if item['Duration'] != '':
                item['Duration'] = item['Duration'].strftime("%Y-%m-%d")
            item['IsExpire'] = '已过期' if datetime.datetime.strptime(item['Expiretime'],
                                                                   "%Y-%m-%d") < nowdate else '未过期'
            # item['Category'] = GKind[int(item['Category']) - 1]
            query_cg = r"""select * from tb_cguarantee where GID = {};""".format(item['ID'])
            item['CGuarantee'] = self._db.query(query_cg)
            temp_result.append(item)
        success = deepcopy(status_code.SUCCESS)
        if int(args.get('ID', 0)) != 0:
            temp_result[0]['group_list'] = self.get_group_info(args.get('ID'))
        else:
            total_result = self._db.query(total_query_sql)
            # print(total_result)
            success['amount_total'] = total_result[0]['amount_total']
            success['realac_total'] = total_result[0]['realac_total']
        success['result'] = temp_result
        success['total'] = total[0]['total_row']
        return jsonify(success)


class UpdateGuarantee(GuaranteeBase):

    def __init__(self):
        super(UpdateGuarantee, self).__init__()
        self.api_permission = 'guarantee_edit'

    def get_img_list(self, name):
        temp_files = request.files.get(name, '')
        img_url = ''
        if temp_files != '':
            img_url = save_image(temp_files, 'static/media/guarantee')
        return img_url

    def update_cguarantee(self, args, index):
        update_sql = r"""update tb_cguarantee set Name='{Name}',IDCard='{IDCard}',Address='{Address}',
                                  Phone='{Phone}',Area='{Area}',Pvalue='{Pvalue}',Proportion='{Proportion}',
                                  Paddress='{Paddress}' """
        args['IDimg'] = self.get_img_list('IDimg_{}'.format(index))
        args['Pimg'] = self.get_img_list('Pimg_{}'.format(index))
        if args['IDimg'] != '':
            update_sql = update_sql + r""",IDimg='{IDimg}'"""
        if args['Pimg'] != '':
            update_sql = update_sql + r""",Pimg='{Pimg}'"""
        update_sql = update_sql + r""" where ID={ID};"""
        self._db.update(update_sql.format(**args))

    def create_cguarantee(self, args, index):
        args['IDimg'] = self.get_img_list('IDimg_{}'.format(index))
        args['Pimg'] = self.get_img_list('Pimg_{}'.format(index))
        args['GID'] = self.args.get('ID')
        insert_sql = r"""insert into tb_cguarantee(Name,IDCard,Address, Phone,Area,Pvalue,Proportion,Paddress,IDimg,
                            Pimg,GID) value ('{Name}','{IDCard}','{Address}','{Phone}','{Area}','{Pvalue}','{Proportion}',
                            '{Paddress}','{IDimg}','{Pimg}',{GID});""".format(**args)
        self._db.insert(insert_sql)

    def views(self):
        is_null = self.args_is_null('Expiretime', 'Duration', 'ProjectID', 'CompanyID', 'GuaCompany', 'Capital',
                                    'Nature', 'Name', 'Amount', 'Kind', 'Deadline', 'SignTime', 'Category', 'Totalrate',
                                    'Total', 'RealAC', 'Marginratio', 'Margin', 'Bene', 'PID', 'CID', 'DID')
        if is_null:
            return jsonify(status_code.CONTENT_IS_NULL)
        args = self.args
        # 时间处理
        args['Expiretime'] = str_to_date(args['Expiretime'])
        args['Duration'] = str_to_date(args['Duration'])
        args['SignTime'] = str_to_date(args['SignTime'])
        # args['SignTime'] = datetime.datetime.now() + datetime.timedelta(hours=8)
        # args['Number'] = 'BSHS-' + str(int(time.time() * 1000))
        args['Number'] = args['Name']
        update_sql = r"""update tb_guarantee set CompanyID='{CompanyID}',Capital='{Capital}',Nature='{Nature}',Name='{Name}',
            Amount='{Amount}',Kind='{Kind}',ProjectID='{ProjectID}',Duration='{Duration}',SignTime='{SignTime}',Number='{Number}',
            Category={Category}, Deadline='{Deadline}', Expiretime='{Expiretime}',Totalrate='{Totalrate}',
            Total='{Total}',RealAC='{RealAC}',Marginratio='{Marginratio}',Margin='{Margin}',Bene='{Bene}',PID={PID},CID={CID},
            DID={DID},Description='{Description}',GuaCompany='{GuaCompany}',Address='{Address}'  where id={ID}""".format(
            **args)
        self._db.update(update_sql)
        if args.get('CGuarantee_list', '') != '':
            query_sql = r"""select id from tb_cguarantee where GID={}""".format(args.get('ID'))
            cg_id_list = self._db.query(query_sql)
            cg_id_len = len(cg_id_list)
            cguarantee_list = loads(args.get('CGuarantee_list', ''))
            for index, cguarantee in enumerate(cguarantee_list[:cg_id_len]):
                self.update_cguarantee(cguarantee, index)
            for index, cguarantee in enumerate(cguarantee_list[cg_id_len:]):
                self.create_cguarantee(cguarantee, index + cg_id_len)
        return jsonify(status_code.SUCCESS)


class CreateCGuarantee(GuaranteeBase):

    def __init__(self):
        super(CreateCGuarantee, self).__init__()
        self.api_permission = 'guarantee_edit'

    def get_img_list(self, name):
        temp_list = []
        temp_files = request.files.get(name, [])
        for img_file in temp_files:
            img_url = save_image(img_file, 'static/media/guarantee')
            temp_list.append(img_url)
        return temp_list

    def views(self):
        args = self.args
        args['IDimg'] = dumps(self.get_img_list('IDimg'))
        args['Pimg'] = dumps(self.get_img_list('Pimg'))
        insert_sql = r"""insert into tb_cguarantee(Name,IDCard,Address, Phone,Area,Pvalue,Proportion,Paddress,IDimg,
                    Pimg,GID,Description) value ('{Name}','{IDCard}','{Address}','{Phone}','{Area}','{Pvalue}','{Proportion}',
                    '{Paddress}','{IDimg}','{Pimg}',{GID},'{Description}');""".format(**args)
        cguarantee_id = self._db.insert(insert_sql)
        success = deepcopy(status_code.SUCCESS)
        success['cguarantee'] = cguarantee_id
        return jsonify(success)


class UpdateCGuarantee(CreateCGuarantee):

    def __init__(self):
        super(UpdateCGuarantee, self).__init__()
        self.api_permission = 'guarantee_edit'

    def views(self):
        args = self.args
        update_sql = r"""update tb_cguarantee set Name='{Name}',IDCard='{IDCard}',Address='{Address}',
                          Phone='{Phone}',Area='{Area}',Pvalue='{Pvalue}',Proportion='{Proportion}',
                          Paddress='{Paddress}', Description='{Description}' """

        if request.files.get('IDimg', []):
            args['IDimg'] = dumps(self.get_img_list('IDimg'))
            update_sql = update_sql + r""",IDimg='{IDimg}'"""
        if request.files.get('Pimg', []):
            args['Pimg'] = dumps(self.get_img_list('IsPimg'))
            update_sql = update_sql + r""",Pimg='{Pimg}'"""
        update_sql = update_sql + r""" where ID={ID};"""
        self._db.update(update_sql.format(**args))
        return jsonify(status_code.SUCCESS)


class CreateGuaranteePic(CreatePicGroup):

    def __init__(self):
        super(CreateGuaranteePic, self).__init__()
        self.dir = 'guarantee/'
        self.ptype = 3
        self.db_dir = '/static/media/' + self.dir


class GetPicGroupList(GuaranteeBase):

    def __init__(self):
        super(GetPicGroupList, self).__init__()
        self.ptype = 3

    def views(self):
        args = self.args
        query_sql = r"""select * from tb_pic_group where cid = {} and ptype={};""".format(args.get('ID'),
                                                                                          self.ptype)
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['group_list'] = result
        return jsonify(success)


class RemoveCGuatantee(GuaranteeBase):

    def __init__(self):
        super(RemoveCGuatantee, self).__init__()

    def views(self):
        args = self.args
        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        remove_sql = r"""delete from tb_cguarantee where id={};""".format(args.get('ID'))
        try:
            self._db.delete(remove_sql)
            # print(remove_sql)
        except Exception as e:
            print(e)
            return jsonify(status_code.DB_ERROR)
        return jsonify(status_code.SUCCESS)
