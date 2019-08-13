import datetime
from json import loads, dumps

from copy import deepcopy

from flask import request, jsonify, sessions

from Company.utils import update_pic_and_group, update_progress_pic
from Company.views import CreatePicGroup, AllCompanyID
from User.util import save_image
from utils import status_code
from utils.BaseView import BaseView
from utils.pulic_utils import str_to_date, month_year_to_date


class CreateProject(BaseView):
    """
    创建项目
    """

    def __init__(self):
        super(CreateProject, self).__init__()
        self.api_permission = 'project_edit'

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def get_person_info(self, person):
        # query_sql = r"""select id,name,phone from tb_company where id={};""".format(int(companyid))
        # result = self._db.query(query_sql)
        person_list = person.split(',')
        temp = []
        if person_list:
            for item in person_list:
                temp_name_list = item.split('&nbsp;')
                if len(temp_name_list) == 3:
                    temp.append({
                        'panme': temp_name_list[0],
                        'post': temp_name_list[1],
                        'phone': temp_name_list[2]
                    })
        return dumps(temp)

    def calc_total_month(self, starttime, endtime):
        start_year = starttime.year
        start_month = starttime.month
        end_year = endtime.year
        end_month = endtime.month
        return (end_year - start_year) * 12 + (end_month - start_month)

    def views(self):
        isnull = self.args_is_null('Name', 'Type', 'GuaranType', 'Price', 'PID', 'CID', 'DID',
                                   'Build', 'Cons', 'ConsManager', 'OwnerManager', 'StartTime', 'EndTime',
                                   'WagePercent')
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        if eval(self.args.get('WagePercent')) == 0:
            return jsonify(status_code.WagePercent_IS_NULL)
        args = deepcopy(self.args)
        if args['StartTime'] != '':
            args['StartTime'] = str_to_date(args['StartTime'])
        if args['EndTime'] != '':
            args['EndTime'] = str_to_date(args['EndTime'])
        # if args['Duration'] != '':
        #     duration = datetime.datetime.strptime(args['Duration'], "%Y-%m-%d")
        #     if duration < args['EndTime']:
        #         return jsonify(status_code.Duration_TIME_TO_ERROR)
        if args['StartTime'] > args['EndTime']:
            return jsonify(status_code.PROJECT_TIME_ERROR)
        if args['Duration'] != '':
            duration = datetime.datetime.strptime(args['Duration'], "%Y-%m-%d")
            if duration < args['EndTime']:
                return jsonify(status_code.Duration_TIME_TO_ERROR)
            args['TotalMonth'] = self.calc_total_month(args['StartTime'], duration)
        else:
            args['TotalMonth'] = self.calc_total_month(args['StartTime'], args['EndTime'])
        # if args['Duration'] == '':
        #     args['TotalMonth'] = self.calc_total_month(args['StartTime'], args['EndTime'])
        # else:
        #     args['TotalMonth'] = self.calc_total_month(args['StartTime'], args['Duration'])
        args['Status'] = int(args['Status'])
        # args['ConsManager'] = self.get_person_info(args['ConsManager'])
        # args['OwnerManager'] = self.get_person_info(args['OwnerManager'])
        # args['LaborManager'] = self.get_person_info(loads(args['LaborManager']))
        # args['Supervisor'] = self.get_person_info(loads(args['Supervisor']))
        insert_sql = r"""insert into tb_project(name,type,guarantype,price,duration,gamount,prinpical,
            wagepercent,starttime,endtime,address,build,cons,consmanager,ownermanager,
            description,status,pid,cid,did,total,totalpay,issue, totalmonth) value('{Name}', {Type}, {GuaranType}, '{Price}', 
            '{Duration}', '{GAmount}', '{PrinPical}', '{WagePercent}', '{StartTime}', '{EndTime}', '{Address}', {Build},
            {Cons}, '{ConsManager}', '{OwnerManager}', '{Description}', {Status},
            {PID},{CID},{DID},'{Total}', '{TotalPay}', '{Issue}', {TotalMonth})"""
        # if args.get('PrinPical', 'null') != 'null':
        #     args['PrinPical'] = dumps(args['PrinPical'])
        # for i in ('ConsManager', 'OwnerManager'):
        #     args[i] = dumps(args[i])
        project_id = self._db.insert(insert_sql.format(**args))
        update_pic_and_group('tb_pic_group', project_id, self.args.get('group_list'), self._db)
        # update_pic_and_group('tb_pics', project_id, self.args.get('Img_list'), self._db)
        return jsonify(status_code.SUCCESS)


class UpdateProject(BaseView):
    """项目编辑"""

    def __init__(self):
        super(UpdateProject, self).__init__()
        self.api_permission = 'project_edit'

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def get_person_info(self, companyid, person):
        query_sql = r"""select id,name,phone from tb_company where id={};""".format(int(companyid))
        result = self._db.query(query_sql)
        temp = []
        if result:
            for item in loads(result[0]['phone']):
                if item['name'] in person:
                    temp.append({
                        'panme': item['name'],
                        'post': item['post'],
                        'phone': item['pone']
                    })
        return dumps(temp)

    def calc_total_month(self, starttime, endtime):
        start_year = starttime.year
        start_month = starttime.month
        end_year = endtime.year
        end_month = endtime.month
        return (end_year - start_year) * 12 + (end_month - start_month)

    def views(self):
        isnull = self.args_is_null('Name', 'Type', 'GuaranType', 'Price', 'PID', 'CID', 'DID', 'WagePercent',
                                   'Build', 'Cons', 'ConsManager', 'OwnerManager', 'StartTime', 'EndTime')
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        if eval(self.args.get('WagePercent')) == 0:
            return jsonify(status_code.WagePercent_IS_NULL)
        args = self.args
        # print(args)
        args['StartTime'] = str_to_date(args['StartTime'])
        args['EndTime'] = str_to_date(args['EndTime'])
        if args['StartTime'] > args['EndTime']:
            return jsonify(status_code.PROJECT_TIME_ERROR)
        if args['Duration'] != '':
            duration = datetime.datetime.strptime(args['Duration'], "%Y-%m-%d")
            if duration < args['EndTime']:
                return jsonify(status_code.Duration_TIME_TO_ERROR)
            args['TotalMonth'] = self.calc_total_month(args['StartTime'], duration)
        else:
            args['TotalMonth'] = self.calc_total_month(args['StartTime'], args['EndTime'])
        # else:
        #     args['TotalMonth'] = self.calc_total_month(args['StartTime'], args['Duration'])
        args['Status'] = int(args['Status'])
        # if args.get('PrinPical', 'null') != 'null':
        #     args['PrinPical'] = loads(args['PrinPical'])
        # for i in ('ConsManager', 'OwnerManager'):
        #     args[i] = self.get_person_info(loads(args[i]))
        # args['ConsManager'] = self.get_person_info(int(args.get('Cons')), loads(args['ConsManager']))
        # args['OwnerManager'] = self.get_person_info(int(args.get('Build')), loads(args['OwnerManager']))
        # print(args)
        update_sql = r"""update tb_project set Name='{Name}',Type={Type}, GuaranType={GuaranType},Price='{Price}',
                Duration='{Duration}',GAmount='{GAmount}',PrinPical='{PrinPical}',WagePercent='{WagePercent}',Status={Status},
                StartTime='{StartTime}', EndTime='{EndTime}',Address='{Address}',Build={Build},Build={Build},
                ConsManager='{ConsManager}',OwnerManager='{OwnerManager}', Description='{Description}', PID={PID},CID={CID},DID={DID},
                Total='{Total}',TotalPay='{TotalPay}',Issue='{Issue}',TotalMonth={TotalMonth} WHERE ID={ID}""".format(
            **args)
        self._db.update(update_sql)
        return jsonify(status_code.SUCCESS)


class DeleteProject(BaseView):
    """
    删除项目
    """

    def __init__(self):
        super(DeleteProject, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        delete_sql = r"""delete from tb_project where id={}""".format(self.args.get('ID'))
        self._db.delete(delete_sql)
        return jsonify(status_code.SUCCESS)


class QueryProject(BaseView):
    """
    项目查询
    """

    def __init__(self):
        super(QueryProject, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def calc_month(self, nowtime, oldtime):
        nowyear = nowtime.year
        oldyear = oldtime.year
        nowmonth = nowtime.month
        oldmonth = oldtime.month
        return (nowyear - oldyear) * 12 + (nowmonth - oldmonth)

    def views(self):
        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select t1.*,t2.Name as PID_Name,t3.Name as CID_Name,t4.Name as DID_Name, t5.Name as BuildName, t6.Name as ConsName from tb_project as t1
                        LEFT JOIN tb_area as t2 on t1.PID = t2.ID
                        LEFT JOIN tb_area as t3 on t1.CID = t3.ID
                        LEFT JOIN tb_area as t4 on t1.DID = t4.ID
                        LEFT JOIN tb_company as t5 on t5.id = t1.Build
                        LEFT JOIN tb_company as t6 on t6.id = t1.Cons
                        where t1.id={}""".format(self.args.get('ID'))
        result = self._db.query(query_sql)[0]
        if result.get('PrinPical', 'null') != 'null':
            result['PrinPical'] = loads(result['PrinPical'])
        # for i in ('ConsManager', 'OwnerManager'):
        #     result[i] = loads(result[i])
        progress_sql = r"""select ID,ProjectID,UploadTime,year,month from tb_progress where ProjectID={} 
                            order by year,month""".format(self.args.get('ID'))
        query_sql = r"""select count(id) as persons from tb_laborinfo where ProjectID = {}""".format(self.args['ID'])
        persons = self._db.query(query_sql)[0]
        result['Persons'] = persons['persons']
        result['NowTime'] = self.calc_month(datetime.datetime.now(), result['StartTime'])
        progress_result = self._db.query(progress_sql)
        success = deepcopy(status_code.SUCCESS)
        for x in ('PID', 'CID', 'DID'):
            if result[x] is None:
                result[x] = ''
            if result[x + '_Name'] is None:
                result[x + '_Name'] = ''
        All_year_month = self.create_all_month(result['StartTime'], result['EndTime'])
        for i in ('StartTime', 'EndTime'):
            result[i] = result[i].strftime("%Y-%m-%d")
        # if result['Duration'] != None and result['Duration'] != '':
        #     result['Duration'] = result['Duration'].strftime("%Y-%m-%d")
        now_time = datetime.datetime.now()
        success['project'] = result
        success['all_year'] = list(All_year_month.keys())
        success['progress'] = []
        if progress_result:
            total = len(progress_result)
            for pindex, gress in enumerate(progress_result):
                temp_year = int(gress['year'])
                temp_month = int(gress['month'])
                for index, item in enumerate(All_year_month[str(temp_year)]):
                    if item['month'] == temp_month:
                        All_year_month[str(temp_year)][index]['is_input'] = 1
                        All_year_month[str(temp_year)][index]['id'] = gress['ID']
                    if temp_year == now_time.year and item['month'] == now_time.month:
                        All_year_month[str(temp_year)][index]['is_now_month'] = 1
                    if pindex == total - 1 and item['month'] == temp_month:
                        All_year_month[str(temp_year)][index]['is_current'] = 1
                gress['Year'] = temp_year
                gress['Month'] = temp_month
                gress['UploadTime'] = gress['UploadTime'].strftime("%Y-%m-%d")
            success['progress'] = self.get_default_progress(progress_result[-1]['ID'])
        success['year_month_info'] = All_year_month
        return jsonify(success)

    def get_temp(self, i):
        return {
            'month': i,
            'id': 0,
            'is_input': 0,
            'is_now_month': 0,
            'is_current': 0,
        }

    def create_all_month(self, start_time, end_time):
        start_year, end_year = start_time.year, end_time.year
        start_month, end_month = start_time.month, end_time.month
        all_month = {}
        if start_year == end_year:
            all_month[str(start_year)] = []
            for i in range(start_month, end_month + 1):
                temp = self.get_temp(i)
                all_month[str(start_year)].append(temp)
        else:
            for temp_year in range(start_year, end_year + 1):
                all_month[str(temp_year)] = []
                if temp_year == start_year:
                    for i in range(start_month, 13):
                        temp = self.get_temp(i)
                        all_month[str(temp_year)].append(temp)
                elif temp_year == end_year:
                    for i in range(1, end_month + 1):
                        temp = self.get_temp(i)
                        all_month[str(temp_year)].append(temp)
                else:
                    for i in range(1, 13):
                        temp = self.get_temp(i)
                        all_month[str(temp_year)].append(temp)
        return all_month

    def get_default_progress(self, progressid):
        query_sql = r"""select * from tb_progress where id = {}""".format(progressid)
        result = self._db.query(query_sql)[0]
        result['Person'] = loads(result['Person'])
        query_all_pics = r"""select * from tb_pics where progressid={} and ptype=1 
                        and type>0;""".format(progressid)
        pics_result = self._db.query(query_all_pics)
        group_list = ['Progress', 'Contract', 'RealName', 'Attend', 'Wage', 'Rights',
                      'Lwages', 'LAB', 'PAB', 'Arrears', 'LPayCert']
        for i in group_list:
            temp = i + '_list'
            result[temp] = []
        for item in pics_result:
            temp_key = group_list[int(item['Type']) - 1] + '_list'
            result[temp_key].append(item)
        result['UploadTime'] = result['UploadTime'].strftime("%Y-%m-%d")
        return result


class ProgressProject(BaseView):
    """
    项目进度查询
    """

    def __init__(self):
        super(ProgressProject, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def get_total_labor(self, pid, year, month):
        start_time = datetime.datetime(year, month, 1)
        if month == 12:
            end_time = datetime.datetime(year + 1, 1, 1)
        else:
            end_time = datetime.datetime(year, month + 1, 1)
        total_labor_sql = r"""select count(id) as total from tb_laborinfo
                            where ProjectID={2} and EntryDate < '{1}' and (DepartureDate is null or (DepartureDate<'{1}' and DepartureDate > '{0}'))"""
        total = self._db.query(total_labor_sql.format(start_time, end_time, pid))[0]['total']
        attend_total_sql = r"""select count(id) as total from tb_attendance where projectid = {0} and year='{1}' and month='{2}'"""
        attend_total = self._db.query(attend_total_sql.format(pid, year, month))[0]['total']
        if total == 0:
            return total, 0
        else:
            return total, round(attend_total / total * 100, 2)

    def get_bank_info(self, pid, year, month):
        query_project = r"""select * from tb_project where id={};""".format(pid)
        result = self._db.query(query_project)
        if result:
            args = result[0]
            # print(args)
            should_pay = eval(args['Price']) * eval(args['WagePercent']) / 100 / args['TotalMonth']
        else:
            should_pay = 0
        bank_query = r"""select * from tb_wage where projectid={0} and year={1} and month={2};"""
        result = self._db.query(bank_query.format(pid, year, month))
        if result:
            args = result[0]
            real_pay = args['RPay']
            status = args['Status']
        else:
            real_pay = 0
            status = 2
        return should_pay, real_pay, status

    def views(self):
        if self.args_is_null('ProgressID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select * from tb_progress where id = {}""".format(self.args.get('ProgressID'))
        result = self._db.query(query_sql)
        if result:
            result = result[0]
            result['Person'] = loads(result['Person'])
            query_all_pics = r"""select t1.* from tb_pics as t1 where t1.progressid={} and t1.ptype=1 
                    and t1.type>0;""".format(self.args.get('ProgressID'))
            pics_result = self._db.query(query_all_pics)
            group_list = ['Progress', 'Contract', 'RealName', 'Attend', 'Wage', 'Rights',
                          'Lwages', 'LAB', 'PAB', 'Arrears', 'LPayCert']
            for i in group_list:
                temp = i + '_list'
                result[temp] = []
            for item in pics_result:
                temp_key = group_list[int(item['Type']) - 1] + '_list'
                result[temp_key].append(item)
            result['UploadTime'] = result['UploadTime'].strftime("%Y-%m-%d")
            result['labor_total'], result['attend_percent'] = self.get_total_labor(result['ProjectID'],
                                                                                   int(result['year']),
                                                                                   int(result['month']))
            result['bank_should_pay'], result['bank_real_pay'], result['bank_status'] = self.get_bank_info(
                result['ProjectID'], int(result['year']), int(result['month']))
        success = deepcopy(status_code.SUCCESS)
        success['progress_info'] = result
        return jsonify(success)


class ADDProgressProject(BaseView):
    """
    增加项目进度
    """

    def __init__(self):
        super(ADDProgressProject, self).__init__()
        self.api_permission = 'project_edit'

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def views(self):
        isnull = self.args_is_null('Status', 'RealName', 'Attend', 'Wage', 'Rights', 'Lwage',
                                   'LAB', 'PAB', 'Arrears', 'LPayCert', 'Contract', 'ProjectID', 'Total', 'PPay',
                                   'LPay', 'Percent')
        for i in ('Total', 'PPay', 'LPay'):
            if not self.is_number(self.args.get(i)):
                return jsonify(status_code.INPUT_NUMBER_ERROR)
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        args = self.args
        args['UploadTime'] = month_year_to_date(args['UploadTime'])
        args['year'] = args['UploadTime'].year
        args['month'] = args['UploadTime'].month
        now_time = datetime.datetime.now()
        if args['UploadTime'] > now_time:
            return jsonify(status_code.PROGRESS_TIME_TO_ERROR)
        query_sql = r"""select * from tb_project where id={};""".format(args.get('ProjectID'))
        result = self._db.query(query_sql)
        reload_start = datetime.datetime.strptime(result[0]['StartTime'].strftime("%Y-%m"), "%Y-%m")
        if reload_start > args['UploadTime'] or args['UploadTime'] > result[0]['EndTime']:
            return jsonify(status_code.PROGRESS_TIME_ERROR)
        for i in ('Status', 'RealName', 'Attend', 'Wage', 'Rights', 'Lwage',
                  'LAB', 'PAB', 'Arrears', 'LPayCert', 'Contract', 'Progress'):
            if args[i] == 'true':
                args[i] = 1
            else:
                args[i] = 0
        insert_sql = r"""insert into tb_progress(ProjectID, Status, UploadTime, Person, Remark,Rtype,Contract,Content,
            RealName,Attend,Wage,Rights,Lwage, LAB, PAB, Arrears, LPayCert,PPay, LPay, Total, Percent,year,month) value ({ProjectID},
            {Status}, '{UploadTime}', '{Person}','{Remark}',{Rtype},{Contract},'{Content}',{RealName},{Attend},{Wage},
            {Rights},{Lwage},{LAB},{PAB},{Arrears},{LPayCert},'{PPay}', '{LPay}','{Total}', '{Percent}', '{year}', '{month}');"""
        args['UploadTime'] = datetime.datetime.now()
        progress_id = self._db.insert(insert_sql.format(**args))
        if self.args.get('ImgGroupID', []):
            update_progress_pic(progress_id, self.args.get('ImgGroupID'), self._db)
        # for i in ('RealName', 'Attend', 'Wage', 'Rights', 'Lwages', 'LAB', 'PAB',
        #           'Arrears', 'LPayCert', 'Contract'):
        #     temp = i + '_list'
        #     if args.get(i):
        #         if args.get(temp, []):
        #             update_progress_pic(progress_id, args.get(temp), self._db)
        update_sql = r"""update tb_project set Total='{}', TotalPay='{}', Issue='{}', status={} where id={};""".format(
            str(float(result[0]['Total']) + float(args['Total'])),
            str(float(result[0]['TotalPay']) + float(args['PPay'])),
            str(float(result[0]['Issue']) + float(args['LPay'])),
            2,
            args['ProjectID']
        )
        self._db.update(update_sql)
        success = deepcopy(status_code.SUCCESS)
        success['msg'] = '上传成功'
        return jsonify(success)


class UpdateProgressProject(BaseView):
    """
    编辑项目进度
    """

    def __init__(self):
        super(UpdateProgressProject, self).__init__()
        self.api_permission = 'project_edit'

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def views(self):
        isnull = self.args_is_null('Status', 'RealName', 'Attend', 'Wage', 'Rights', 'Lwage',
                                   'LAB', 'PAB', 'Arrears', 'LPayCert', 'Contract', 'ProjectID', 'ID', 'Total', 'PPay',
                                   'LPay', 'Percent')
        for i in ('Total', 'PPay', 'LPay'):
            if not self.is_number(self.args.get(i)):
                return jsonify(status_code.INPUT_NUMBER_ERROR)
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        args = self.args
        args['UploadTime'] = month_year_to_date(args['UploadTime'])
        args['year'] = args['UploadTime'].year
        args['month'] = args['UploadTime'].month
        now_time = datetime.datetime.now()
        if args['UploadTime'] > now_time:
            return jsonify(status_code.PROGRESS_TIME_TO_ERROR)
        query_sql = r"""select * from tb_project where id={};""".format(args.get('ProjectID'))
        result = self._db.query(query_sql)
        reload_start = datetime.datetime.strptime(result[0]['StartTime'].strftime("%Y-%m"), "%Y-%m")
        if reload_start > args['UploadTime'] or args['UploadTime'] > result[0]['EndTime']:
            return jsonify(status_code.PROGRESS_TIME_ERROR)
        for i in ('Status', 'RealName', 'Attend', 'Wage', 'Rights', 'Lwage',
                  'LAB', 'PAB', 'Arrears', 'LPayCert', 'Contract', 'Progress'):
            if args[i] == 'true':
                args[i] = 1
            else:
                args[i] = 0

        old_data_sql = r"""select PPay,LPay,Total from tb_progress where id={}""".format(self.args.get('ID'))
        old_data = self._db.query(old_data_sql)

        update_progress_sql = r"""update tb_progress set ProjectID={ProjectID}, Status={Status},
                    Person='{Person}',Remark='{Remark}',Rtype={Rtype},Contract={Contract},Content='{Content}',RealName={RealName},
                    Attend={Attend},Wage={Wage}, Rights={Rights},Lwage={Lwage},LAB={LAB},PAB={PAB},Arrears={Arrears}, 
                    LPayCert={LPayCert},PPay='{PPay}', LPay='{LPay}', Total='{Total}',Percent='{Percent}',year='{year}',
                    month='{month}' where id ={ID}"""
        args['UploadTime'] = datetime.datetime.now()
        self._db.update(update_progress_sql.format(**args))
        if self.args.get('ImgGroupID', []):
            update_progress_pic(self.args.get('ID'), self.args.get('ImgGroupID'), self._db)
        if old_data:
            update_sql = r"""update tb_project set Total='{}', TotalPay='{}', Issue='{}' where id={};""".format(
                str(eval(result[0]['Total']) - eval(old_data[0]['Total']) + eval(args['Total'])),
                str(eval(result[0]['TotalPay']) - eval(old_data[0]['PPay']) + eval(args['PPay'])),
                str(eval(result[0]['Issue']) - eval(old_data[0]['LPay']) + eval(args['LPay'])),
                args['ProjectID']
            )
            self._db.update(update_sql)
        success = deepcopy(status_code.SUCCESS)
        success['msg'] = '上传成功'
        return jsonify(success)


class CreateProPicGroup(CreatePicGroup):
    """
    创建项目图片分组
    """

    def __init__(self):
        super(CreateProPicGroup, self).__init__()
        self.dir = 'project/'
        self.ptype = 1
        self.db_dir = '/static/media/' + self.dir


class GetComAndPer(BaseView):
    """
    获取所有公司和责任人
    """

    def __init__(self):
        super(GetComAndPer, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        args = self.args
        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select id, name, Phone from tb_company where id={};""".format(int(args.get('ID')))
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['companyinfo'] = []
        if result:
            success['companyinfo'] = loads(result[0]['Phone'])
        return jsonify(success)


class GetProgressGicList(BaseView):
    """
    获取项目进度分组列表
    ID：项目ID
    """

    def __init__(self):
        super(GetProgressGicList, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):

        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select * from tb_pic_group where CID={} and ptype={};""".format(self.args.get('ID'), 1)
        reslut = self._db.query(query_sql)
        group_list = {
            'project': [],  # 项目分组
            'Progress_list': [],  # 进度分组
            'Contract_list': [],  # 签到合同分组
            'RealName_list': [],  # 实名制分组
            'Attend_list': [],  # 考勤分组
            'Wage_list': [],  # 工资专户分组
            'Rights_list': [],  # 维权公示牌
            'Lwages_list': [],  # 工资公示牌
            'LAB_list': [],  # 劳务专员
            'PAB_list': [],  # 项目经理
            'Arrears_list': [],  # 欠薪预案
            'LPayCert_list': [],  # 工资支付分组

        }
        for item in reslut:
            temp_type = int(item['Type'])
            if temp_type == 0:
                group_list['project'].append(item)
            elif temp_type == 1:
                group_list['Progress_list'].append(item)
            elif temp_type == 2:
                group_list['Contract_list'].append(item)
            elif temp_type == 3:
                group_list['RealName_list'].append(item)
            elif temp_type == 4:
                group_list['Attend_list'].append(item)
            elif temp_type == 5:
                group_list['Wage_list'].append(item)
            elif temp_type == 6:
                group_list['Rights_list'].append(item)
            elif temp_type == 7:
                group_list['Lwages_list'].append(item)
            elif temp_type == 8:
                group_list['LAB_list'].append(item)
            elif temp_type == 9:
                group_list['PAB_list'].append(item)
            elif temp_type == 10:
                group_list['Arrears_list'].append(item)
            else:
                group_list['LPayCert_list'].append(item)
        success = deepcopy(status_code.SUCCESS)
        success['group'] = group_list
        return jsonify(success)


class UploadProjectIMG(BaseView):
    """
    项目图片上传
    """

    def __init__(self):
        super(UploadProjectIMG, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def save_more_img(self, gid, p_type, r_type, img_dir, file_list):
        result_file_list = []
        for one_file in file_list:
            try:
                iamge_url = save_image(one_file, img_dir)
                if int(self.args.get('IsCreate', 1)):
                    insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type) 
                                        value ({},'{}', '{}', {},{})""".format(gid, iamge_url,
                                                                               one_file.filename[:-4],
                                                                               p_type,
                                                                               r_type)
                else:
                    insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type,progressid) 
                                                    value ({},'{}', '{}', {},{},{})""".format(gid, iamge_url,
                                                                                              one_file.filename[:-4],
                                                                                              p_type,
                                                                                              r_type,
                                                                                              self.args.get(
                                                                                                  'ProgressID'))
                pid = self._db.insert(insert_sql)
                temp = {'id': pid, 'name': one_file.filename[:-4], 'url': iamge_url}
                result_file_list.append(deepcopy(temp))
            except:
                continue
        return result_file_list

    def views(self):
        if self.args_is_null('ID', 'IsCreate', 'ProgressID', ):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select id,gurl,ptype,type,name,cid from tb_pic_group where id={}""".format(self.args.get('ID'))
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.DIR_NOT_EXISTS)
        temp_img_dir = result[0]['gurl'][1:]
        image_file = request.files.getlist('file')
        if image_file == '' or image_file == []:
            return jsonify(status_code.FILE_NOT_EXISTS)
        # iamge_url = save_image(image_file, temp_img_dir)
        result_img_list = self.save_more_img(result[0]['id'], result[0]['ptype'], result[0]['type'], temp_img_dir,
                                             image_file)
        success = deepcopy(status_code.SUCCESS)
        # if int(self.args.get('IsCreate', 1)):
        #     insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type)
        #                         value ({},'{}', '{}', {},{})""".format(result[0]['id'], iamge_url,
        #                                                                image_file.filename[:-4],
        #                                                                result[0]['ptype'],
        #                                                                result[0]['type'])
        #     id = self._db.insert(insert_sql)
        # else:
        #     insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type,progressid)
        #                                     value ({},'{}', '{}', {},{},{})""".format(result[0]['id'], iamge_url,
        #                                                                               image_file.filename[:-4],
        #                                                                               result[0]['ptype'],
        #                                                                               result[0]['type'],
        #                                                                               self.args.get('ProgressID'))
        #     id = self._db.insert(insert_sql)
        # success['id'] = id
        # success['name'] = image_file.filename[:-4]
        # success['url'] = iamge_url
        success['data'] = result_img_list
        return jsonify(success)


class ProjectMainQuery(BaseView):
    """
    项目查询，包括不良查询
    """

    def __init__(self):
        super(ProjectMainQuery, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        if self.get_session_ids() != '':
            query_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
            self.ids = self.set_ids(query_sql)
        else:
            self.ids = []
        return self.views()

    def views(self):
        args = self.args
        # now_time = datetime.datetime.now()
        query_sql_base = r"""select SQL_CALC_FOUND_ROWS t1.*,t1.Issue as oldissue, t2.Name as ConsName,t7.Name as BuildName, t4.Status as WStatus, t6.rapy as Issue from tb_project as t1
            left join tb_company as t2 on t2.id = t1.cons
            left join tb_company as t7 on t7.id = t1.build
            left join (select sum(t5.rpay) as rapy,t5.ProjectID from tb_wage as t5 GROUP BY ProjectID) as t6 on t6.ProjectID = t1.id 
            {left} join (select id,projectID,Status from tb_wage {WStatus} group by projectID) as t4 on t4.ProjectID = t1.id  
            """
        wstatus = {}
        # print(args.get('WStatus'))
        if int(args.get('WStatus', 3)) != 3:
            wstatus['left'] = 'right'
            wstatus['WStatus'] = ' where status={} '.format(args.get('WStatus'))
        else:
            wstatus['left'] = 'left'
            wstatus['WStatus'] = ''
            # where_sql_list.append(r""" t4.Status={} """.format(int(args.get('WStatus'))))
        where_sql_list = []
        if self.ids != None:
            if self.ids == []:
                self.ids = [0, ]
            where_sql_list.append(r""" t1.ID in ({}) """.format(self.to_sql_where_id()))
        if args.get('ProjectName', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('ProjectName')))
        if args.get('CompanyName', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t2.Name,'')) LIKE '%{}%' """.format(args.get('CompanyName')))
        if int(args.get('DID', 0)) != 0:
            where_sql_list.append(r""" t1.DID={} """.format(int(args.get('DID'))))
        if int(args.get('CID', 0)) != 0:
            where_sql_list.append(r""" t1.CID={} """.format(int(args.get('CID'))))
        if int(args.get('PID', 0)) != 0:
            where_sql_list.append(r""" t1.PID={} """.format(int(args.get('PID'))))
        if int(args.get('Status', 4)) != 4:
            if int(args.get('Status')) == 5:
                where_sql_list.append(r""" t1.Status > 1 """)
            else:
                where_sql_list.append(r""" t1.Status={} """.format(int(args.get('Status'))))

        temp = ''
        if where_sql_list:
            temp = ' where '
            for index, i in enumerate(where_sql_list):
                temp += i
                if index < len(where_sql_list) - 1:
                    temp += 'and'
        page = int(args.get('Page', 1))
        psize = int(args.get('PageSize', 10))
        limit_sql = r""" limit {},{};""".format((page - 1) * psize, psize)
        query_sql = query_sql_base + " " + temp + limit_sql
        # print(query_sql.format(**wstatus))
        result = self._db.query(query_sql.format(**wstatus))
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        # print(query_sql.format(**args))
        projects = []
        if result:
            for item in result:
                # item['BadRecord'] = loads(item['BadRecord'])
                # for i in ('ConsManager', 'OwnerManager'):
                #     if item[i] is not None:
                #         item[i] = loads(item[i])
                # if item[i] is not None:
                item['EndTime'] = item['EndTime'].strftime("%Y-%m-%d")
                item['StartTime'] = item['StartTime'].strftime("%Y-%m-%d")
                query_sql = r"""select count(id) as persons from tb_laborinfo where ProjectID = {}""".format(item['ID'])
                persons = self._db.query(query_sql)[0]
                item['Persons'] = persons['persons']
                # if eval(item['TotalPay']) != 0:
                #     item['Lpercent'] = eval(item['Issue']) / eval(item['TotalPay']) * 100
                # else:
                # item['Lpercent'] = 0
                if item['Issue'] is None:
                    item['Issue'] = 0
                projects.append(item)
        success = deepcopy(status_code.SUCCESS)
        # print(projects)
        success['project'] = projects
        success['total'] = total[0]['total_row']
        return jsonify(success)


class ALLProjectID(AllCompanyID):
    """
    获取所有项目的名称和ID
    """

    def __init__(self):
        super(ALLProjectID, self).__init__()
        self.table = 'tb_project'

    def admin(self):
        query_sql = r"""select ID from tb_project where DID in ({});""".format(self.get_session_ids())
        self.ids = self.set_ids(query_sql)
        return self.views()

    def get_labor_group_info(self, projectid):
        query_sql = r"""select t1.ClassName,t1.ID as ClassID, t2.Name as SuperiorsName, t2.ID as SuperiorsID from tb_class as t1
                    RIGHT JOIN tb_laborinfo as t2 on t1.ID = t2.ClassID and t2.IsLeader = 1 
                    where t1.ProjectID={}""".format(projectid)
        result = self._db.query(query_sql)
        return result

    def distinct(self, result):
        data = []
        id_s = []
        for item in result:
            if item['ClassID'] not in id_s:
                id_s.append(item['ClassID'])
                data.append(item)
        return data

    def get_project_company(self, projectid):
        build_query_sql = r"""select t2.id as ID, t2.Name as Name from tb_project as t1
                                right JOIN tb_company as t2 on t1.Build = t2.ID
                                where t1.id = {}""".format(projectid)
        cons_query_sql = r"""select t2.id as ID, t2.Name as Name from tb_project as t1
                                        right JOIN tb_company as t2 on t1.cons = t2.ID
                                        where t1.id = {}""".format(projectid)
        build_result = self._db.query(build_query_sql)
        cons_result = self._db.query(cons_query_sql)
        build_result.extend(cons_result)
        return build_result

    def views(self):
        query_sql = self.get_query_sql()
        result = self._db.query(query_sql)
        for item in result:
            item['companyinfo'] = self.get_project_company(item['ID'])
            item['labor_group_info'] = self.distinct(self.get_labor_group_info(item['ID']))
        success = deepcopy(status_code.SUCCESS)
        success['list'] = result
        return jsonify(success)


class GetProjectCompany(BaseView):

    def __init__(self):
        super(GetProjectCompany, self).__init__()

    def admin(self):
        return self.views()

    def administrator(self):
        return self.views()

    def get_labor_group_info(self, projectid):
        query_sql = r"""select t1.ClassName,t1.ID as ClassID, t2.Name as SuperiorsName, t2.ID as SuperiorsID from tb_class as t1
                    LEFT JOIN tb_laborinfo as t2 on t1.ProjectID = t2.ProjectID and t2.IsLeader = 1 
                    where t1.ProjectID={}""".format(projectid)
        result = self._db.query(query_sql)
        return result

    def views(self):
        args = self.args
        build_query_sql = r"""select t2.id as ID, t2.Name as Name from tb_project as t1
                        right JOIN tb_company as t2 on t1.Build = t2.ID
                        where t1.id = {}""".format(int(args.get('ProjectID')))
        cons_query_sql = r"""select t2.id as ID, t2.Name as Name from tb_project as t1
                                right JOIN tb_company as t2 on t1.cons = t2.ID
                                where t1.id = {}""".format(int(args.get('ProjectID')))
        build_result = self._db.query(build_query_sql)
        cons_result = self._db.query(cons_query_sql)
        build_result.extend(cons_result)
        success = deepcopy(status_code.SUCCESS)
        success['companyinfo'] = build_result
        success['labor_group_info'] = self.get_labor_group_info(int(args.get('ProjectID')))
        return jsonify(success)
