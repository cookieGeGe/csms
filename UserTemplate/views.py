import datetime

from copy import deepcopy

import os
import time
import uuid

from flask import jsonify, request, make_response
from werkzeug.utils import secure_filename

from APP.settings import BASE_DIR
from Company.ImportCompany import FileImportCompany
from Export.exportcontext import ExportContext
from Labor.ImportLabor import FileImportLabor
from Project.ImportProject import FileImportProject
from utils import status_code
from utils.BaseView import BaseView
from utils.ImportTemp import TempColnames
from Export.exportfile import ExportFile
from utils.pulic_utils import str_to_datetime


class TemplateBase(BaseView):

    def __init__(self):
        super(TemplateBase, self).__init__()

    def admin(self):
        return self.views()

    def administrator(self):
        return self.views()

    def views(self):
        return jsonify(status_code.SUCCESS)


class CreateTemplate(TemplateBase):

    def __init__(self):
        super(CreateTemplate, self).__init__()
        self.api_permission = 'template_edit'

    def save_file(self, template_file):
        file_url = ''
        if template_file != '':
            filename = secure_filename(template_file.filename)
            dir_path = os.path.join(BASE_DIR, 'static', 'template')
            while not os.path.exists(dir_path):
                dir_path = os.path.join(BASE_DIR, 'static', 'template')
                os.makedirs(dir_path)
            # 因为上次的文件可能有重名，因此使用uuid保存文件
            file_name = str(uuid.uuid4()) + '.' + filename.rsplit('.', 1)[1]
            template_file.save(os.path.join(dir_path, file_name))
            file_url = '/static/template/' + file_name
        return file_url

    def views(self):
        args = self.args
        success = deepcopy(status_code.SUCCESS)
        args['Time'] = datetime.datetime.now()
        if int(args.get('ID', 0)) == 0:
            """新建模板"""
            args['Number'] = 'MBBH-' + str(int(time.time() * 1000))
            template_file = request.files.get('File', '')
            args['File'] = self.save_file(template_file)
            insert_sql = r"""insert into tb_template(Name,Time,Description,Number,File,Type) value 
                            ('{Name}', '{Time}', '{Description}', '{Number}', '{File}', {Type});""".format(**args)
            self._db.insert(insert_sql)
        else:
            template_file = request.files.get('File', '')
            args['File'] = self.save_file(template_file)
            if args['File'] == '':
                update_sql = r"""update tb_template set Name='{Name}',
                                Description='{Description}', Type='{Type}' where id={ID};""".format(**args)
            else:
                update_sql = r"""update tb_template set Name={Name},Description={Description}, 
                                    Type={Type}, File='{File}' where id={ID};""".format(**args)
            self._db.update(update_sql)
        return jsonify(success)


class DeleteTemplate(TemplateBase):

    def __init__(self):
        super(DeleteTemplate, self).__init__()
        self.api_permission = 'template_edit'

    def views(self):
        self.args_is_null('ID')
        delete_sql = r""" delete from tb_template where id = {};""".format(int(self.args.get('ID')))
        self._db.delete(delete_sql)
        return jsonify(status_code.SUCCESS)


class QueryTemplate(TemplateBase):

    def __init__(self):
        super(QueryTemplate, self).__init__()
        self.api_permission = 'template_show'

    def views(self):
        args = self.args
        query_sql = r"""select SQL_CALC_FOUND_ROWS * from tb_template"""
        where_sql_list = []
        if args.get('Name', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(Name,'')) LIKE '%{}%' """.format(args.get('Name')))
        if args.get('Number', '') != '':
            where_sql_list.append(r""" CONCAT(IFNULL(Number,'')) LIKE '%{}%' """.format(args.get('Number')))
        if int(args.get('Type', 3)) != 3:
            where_sql_list.append(r""" Type={} """.format(int(args.get('Type'))))
        if args.get('Time', '') != '':
            where_sql_list.append(r""" Time>'{}' """.format(str_to_datetime(args.get('Time'))))
        where_sql = ' '
        for index, item in enumerate(where_sql_list):
            where_sql += ' where '
            where_sql += item
            if index < len(where_sql_list) - 1:
                where_sql += ' and '
        page = int(args.get('Page', 1))
        psize = int(args.get('PageSize', 10))
        limit_sql = r""" limit {},{};""".format((page - 1) * psize, psize)
        result = self._db.query(query_sql + where_sql + limit_sql)
        total = self._db.query("""SELECT FOUND_ROWS() as total_row;""")
        for item in result:
            item['Time'] = item['Time'].strftime("%Y-%m-%d %H:%M:%S")
        success = deepcopy(status_code.SUCCESS)
        success['result'] = result
        success['total'] = total[0]['total_row']
        return jsonify(success)


class QueryOneTemplate(TemplateBase):

    def __init__(self):
        super(QueryOneTemplate, self).__init__()
        self.api_permission = 'template_show'

    def views(self):
        self.args_is_null('ID')
        query_sql = r"""select * from tb_template where id = {}""".format(self.args.get('ID'))
        result = self._db.query(query_sql)
        success = deepcopy(status_code.SUCCESS)
        success['template'] = ''
        if result:
            result[0]['Time'] = result[0]['Time'].strftime("%Y-%m-%d %H:%M:%S")
            success['template'] = result[0]
        return jsonify(success)


class ImportComProLaTemp(TemplateBase):

    def __init__(self):
        super(ImportComProLaTemp, self).__init__()
        self.api_permission = 'template_edit'

    def views(self):
        args = self.args
        files = request.files.get('file', '')
        if files == '':
            return jsonify(status_code.TEMPLATE_ERROR)
        if args.get('Name') == 'Company':
            import_temp = FileImportCompany(files, TempColnames.COMPANY, self._db)
        elif args.get('Name') == 'Project':
            import_temp = FileImportProject(files, TempColnames.PROJECT, self._db)
        else:
            import_temp = FileImportLabor(files, TempColnames.LABOR, self._db)
        import_temp.save()
        result = import_temp.bad_info
        success = deepcopy(status_code.SUCCESS)
        success['data'] = []
        success['msg'] = '导入成功！'
        if result:
            success['msg'] = '导入失败！'
            success['data'] = result
        return jsonify(success)


class ExportFileView(TemplateBase):

    def __init__(self):
        super(ExportFileView, self).__init__()

    def views(self):
        if self.args_is_null('type', 'ft'):
            return jsonify(status_code.CONTENT_IS_NULL)
        factory = ExportFile()
        export = factory.get_export_factory(self.args.get('type')).get_export_obj(self.args.get('ft'))
        export_context = ExportContext(export)
        export_context.query_data()
        export_context.formatter()
        export_context.render()
        value = export_context.get_stream()
        resp = make_response(value)
        resp.headers["Content-Disposition"] = "attachment; filename={}".format(export_context.export_name)
        resp.headers['Content-Type'] = '{}'.format(export_context.content_type)
        return resp
