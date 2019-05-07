from json import loads, dumps

from copy import deepcopy

from flask import request, jsonify, sessions

from Company.utils import update_pic_and_group, update_progress_pic
from Company.views import CreatePicGroup
from User.util import save_image
from utils import status_code
from utils.BaseView import BaseView


class CreateProject(BaseView):
    """
    创建项目
    """

    def __init__(self):
        super(CreateProject, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        isnull = self.args_is_null('Name', 'Type', 'GuanranType', 'Price', 'PID', 'CID', 'DID',
                                   'Build', 'Cons', 'ConsManager', 'OwnerManager', 'LaborManager',
                                   'Supervisor')
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        args = self.args
        args['Status'] = int(args['Status'])
        insert_sql = r"""insert into tb_project(name,type,guarantype,price,duration,gamount,prinpical,
            wagepercent,starttime,endtime,address,build,cons,consmanager,ownermanager,labormanager,supervisor,
            description,status,pid,cid,did,total,totalpay,issue) value('{Name}', Type, {GuaranType}, '{Price}', 
            {Daration}, '{GAmount}', '{PrinPical}', '{WagePercent}', '{StartTime}', '{EndTime}', '{Address}', {Build},
            {Build}, '{ConsManager}', '{OwnerManager}', '{LaborManager}', '{Supervisor}','{Description}', {Status},
            {PID},{CIS},{DID},'{Total}', '{TotalPay}', '{Issue}')"""
        if args.get('PrinPical', 'null') != 'null':
            args['PrinPical'] = dumps(args['PrinPical'])
        for i in ('ConsManager', 'OwnerManager', 'LaborManager', 'Supervisor'):
            args[i] = dumps(args[i])
        project_id = self._db.insert(insert_sql.format(args))
        update_pic_and_group('tb_pic_group', project_id, self.args.get('Group_list'), self._db)
        update_pic_and_group('tb_pics', project_id, self.args.get('Img_list'), self._db)
        return jsonify(status_code.SUCCESS)


class UpdateProject(BaseView):
    """项目编辑"""

    def __init__(self):
        super(UpdateProject, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        isnull = self.args_is_null('Name', 'Type', 'GuanranType', 'Price', 'PID', 'CID', 'DID',
                                   'Build', 'Cons', 'ConsManager', 'OwnerManager', 'LaborManager',
                                   'Supervisor')
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        args = self.args
        args['Status'] = int(args['Status'])
        if args.get('PrinPical', 'null') != 'null':
            args['PrinPical'] = dumps(args['PrinPical'])
        for i in ('ConsManager', 'OwnerManager', 'LaborManager', 'Supervisor'):
            args[i] = dumps(args[i])
        update_sql = r"""update tb_project set Name='{Name}',Type={Type}, GuaranType={GuaranType},Price='{Price}',
                Daration={Daration},GAmount='{GAmount}',PrinPical='{PrinPical}',WagePercent='{WagePercent}',
                StartTime='{StartTime}', EndTime='{EndTime}',Address='{Address}',Build={Build},Build={Build},
                ConsManager='{ConsManager}',OwnerManager='{OwnerManager}',LaborManager='{LaborManager}',
                Supervisor='{Supervisor}', Description='{Description}', Status={Status},PID={PID},CID={CID},DID={DID},
                Total='{Total}',TotalPay='{TotalPay}',Issue='{Issue}' WHERE ID={ID}""".format(**args)
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

    def views(self):
        if self.args_is_null('ID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select * from tb_project where id={}""".format(self.args.get('ID'))
        result = self._db.query(query_sql)[0]
        if result.get('PrinPical', 'null') != 'null':
            result['PrinPical'] = dumps(result['PrinPical'])
        for i in ('ConsManager', 'OwnerManager', 'LaborManager', 'Supervisor'):
            result[i] = loads(result[i])
        progress_sql = r"""select ID,ProjectID,UploadTime from tb_progress where ProjectID={} 
                            order by UploadTime""".format(self.args.get('ID'))
        progress_result = self._db.query(progress_sql)
        success = deepcopy(status_code.SUCCESS)
        success['project'] = result
        success['progress'] = progress_result
        return jsonify(success)


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

    def views(self):
        if self.args_is_null('ProgressID'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select * from tb_progress where id = {}""".format(self.args.get('ProgressID'))
        result = self._db.query(query_sql)[0]
        result['Person'] = loads(result['Person'])
        query_all_pics = r"""select * from tb_pics where progressid={} and ptype=1 
                and type>0;""".format(self.args.get('ProgressID'))
        pics_result = self._db.query(query_all_pics)
        group_list = ['Progress', 'Contract', 'RealName', 'Attend', 'Wage', 'Rights',
                      'Lwages', 'LAB', 'PAB', 'Arrears', 'LPayCert']
        for i in group_list:
            temp = i + '_list'
            result[temp] = []
        for item in pics_result:
            temp_key = group_list[int(item['type']) - 1] + '_list'
            result[temp_key].append(item)
        success = deepcopy(status_code.SUCCESS)
        success['progress_info'] = result
        return jsonify(success)


class ADDProgressProject(BaseView):
    """
    增加项目进度
    """

    def __init__(self):
        super(ADDProgressProject, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        isnull = self.args_is_null('Status', 'RealName', 'Attend', 'Wage', 'Rights', 'Lwages',
                                   'LAB', 'PAB', 'Arrears', 'LPayCert', 'Contract', 'ProjectID')
        if isnull:
            return jsonify(status_code.CONTENT_IS_NULL)
        args = self.args
        query_sql = r"""select * from tb_project where id={};""".format(args.get('ProjectID'))
        result = self._db.query(query_sql)
        args['Person'] = dumps(args['Person'])
        for i in ('Status', 'RealName', 'Attend', 'Wage', 'Rights', 'Lwages',
                  'LAB', 'PAB', 'Arrears', 'LPayCert', 'Contract'):
            if args[i]:
                args[i] = 1
            else:
                args[i] = 0
        insert_sql = r"""insert into tb_progress(ProjectID, Status, UploadTime, Person, Remark,Rtype,Contract,Content,
            RealName,Attend,Wage,Rights,Lwages, LAB, PAB, Arrears, LPayCert,PPay, LPay, Total) value ({ProjectID},
            {Status}, '{UploadTime}', '{Person}','{Remark}',{Rtype},{Contract},'{Content}',{RealName},{Attend},{Wage},
            {Rights},{Lwages},{LAB},{PAB},{Arrears},{LPayCert},'{PPay}', '{LPay}','{Total}');"""
        progress_id = self._db.insert(insert_sql.format(**args))
        if self.args.get('progress_list', []):
            update_progress_pic(progress_id, self.args.get('Progress_list'), self._db)
        for i in ('RealName', 'Attend', 'Wage', 'Rights', 'Lwages', 'LAB', 'PAB',
                  'Arrears', 'LPayCert', 'Contract'):
            temp = i + '_list'
            if args.get(i):
                if args.get(temp, []):
                    update_progress_pic(progress_id, args.get(temp), self._db)
        update_sql = r"""update tb_project set Total='{}', TotalPay='{}', Issue='{}' where id={};""".format(
            str(float(result[0]['Total']) + float(args['Total'])),
            str(float(result[0]['TotalPay']) + float(args['PPay'])),
            str(float(result[0]['Issue']) + float(args['LPay'])),
            args['ProjectID']
        )
        self._db.update(update_sql)

        return jsonify(status_code.SUCCESS)


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
        query_sql = r"""select id, name, Phone from tb_company"""
        result = self._db.query(query_sql)
        company_info = []
        for item in result:
            temp = {
                'id': item['id'],
                'name': item['name'],
                'persons': loads(item['Phone'])
            }
            company_info.append(temp)
        success = deepcopy(status_code.SUCCESS)
        success['companyinfo'] = company_info
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
        query_sql = r"""select * from tb_pic_group where CID={}, ptype={}""".format(self.args.get('ID'), 1)
        reslut = self._db.query(query_sql)
        group_list = {
            'project': [],  # 项目分组
            'progress': [],  # 进度分组
            'checkin': [],  # 签到合同分组
            'realname': [],  # 实名制分组
            'attendance': [],  # 考勤分组
            'payroll_account': [],  # 工资专户分组
            'rights_protection': [],  # 维权公示牌
            'salary': [],  # 工资公示牌
            'labor': [],  # 劳务专员
            'project_manager': [],  # 项目经理
            'arrears': [],  # 欠薪预案
            'pay': [],  # 工资支付分组

        }
        for item in reslut:
            temp_type = int(item['type'])
            if temp_type == 0:
                group_list['project'].append(item)
            elif temp_type == 1:
                group_list['progress'].append(item)
            elif temp_type == 2:
                group_list['checkin'].append(item)
            elif temp_type == 3:
                group_list['realname'].append(item)
            elif temp_type == 4:
                group_list['attendance'].append(item)
            elif temp_type == 5:
                group_list['payroll_account'].append(item)
            elif temp_type == 6:
                group_list['rights_protection'].append(item)
            elif temp_type == 7:
                group_list['salary'].append(item)
            elif temp_type == 8:
                group_list['labor'].append(item)
            elif temp_type == 9:
                group_list['project_manager'].append(item)
            elif temp_type == 10:
                group_list['arrears'].append(item)
            else:
                group_list['pay'].append(item)
        success = deepcopy(status_code.SUCCESS)
        success['group']: group_list
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

    def views(self):
        if self.args_is_null('ID', 'IsCreate', 'ProgressID', ):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select id,gurl,ptype,type,name,cid from tb_pic_group where id={}""".format(self.args.get('ID'))
        result = self._db.query(query_sql)
        if not result:
            return jsonify(status_code.DIR_NOT_EXISTS)
        temp_img_dir = result[0]['gurl'][1:]
        image_file = request.files.get('file', None)
        if image_file is None:
            return jsonify(status_code.FILE_NOT_EXISTS)
        iamge_url = save_image(image_file, temp_img_dir)
        success = deepcopy(status_code.SUCCESS)
        if self.args.get('IsCreate'):
            insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type) 
                                value ({},'{}', '{}', {},{})""".format(result[0]['id'], iamge_url,
                                                                       image_file.filename[:-4],
                                                                       result[0]['ptype'],
                                                                       result[0]['type'])
            id = self._db.insert(insert_sql)

            success['id'] = id
            success['name'] = image_file.filename[:-4]
            success['url'] = iamge_url
        else:
            insert_sql = r"""insert into tb_pics(GroupID, purl, name, Ptype, type,progressid) 
                                            value ({},'{}', '{}', {},{})""".format(result[0]['id'], iamge_url,
                                                                                   image_file.filename[:-4],
                                                                                   result[0]['ptype'],
                                                                                   result[0]['type'],
                                                                                   self.args.get('ProgressID'))
            self._db.insert(insert_sql)
        return jsonify(success)


class ProjectMainQuery(BaseView):

    def __init__(self):
        super(ProjectMainQuery, self).__init__()

    def administrator(self):
        self.views()

    def admin(self):
        self.views()

    def views(self):
        args = self.args
        query_sql_base = r"""select t1.*,t2.Name as CompanyName, count(t3.id) as Persons from tb_project as t1
                            left join tb_company as t2 on t2.id = t1.cons
                            left join tb_laborinfo as t3 on t3.ProjectID = t1.id """
        where_sql_list = []
        if args.get('ProjectName', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t1.Name,'')) LIKE '%{}%' """.format(args.get('ProjectName')))
        if args.get('CompanyName', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(t2.Name,'')) LIKE '%{}%' """.format(args.get('CompanyName')))
        if args.get('DID', 0):
            where_sql_list.append(r""" t1.DID={} """.format(args.get('DID')))
        if args.get('CID', 0):
            where_sql_list.append(r""" t1.CID={} """.format(args.get('CID')))
        if args.get('PID', 0):
            where_sql_list.append(r""" t1.PID={} """.format(args.get('PID')))
        if args.get('Status', 0):
            where_sql_list.append(r""" t1.Status={} """.format(args.get('Status')))
        temp = ' where '
        for index, i in enumerate(where_sql_list):
            temp += i
            if index < len(where_sql_list) - 1:
                temp += 'and'
        page = int(args.get('Page', 1))
        psize = int(args.get('PageSize', 10))
        limit_sql = r""" limit {},{};""".format(page * psize, psize)
        query_sql = query_sql_base + " " + temp + limit_sql
        result = self._db.query(query_sql)
        projects = []
        for item in result:
            # item['BadRecord'] = loads(item['BadRecord'])
            for i in ('ConsManager', 'OwnerManager', 'LaborManager', 'Supervisor'):
                item[i] = loads(item[i])
            projects.append(item)
        success = deepcopy(status_code.SUCCESS)
        success['project'] = projects
        return jsonify(status_code.SUCCESS)
