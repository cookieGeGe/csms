from json import loads

from flask import jsonify

from utils import status_code
from utils.BaseView import BaseView


class Permission(BaseView):

    def __init__(self):
        super(Permission, self).__init__()
        self.api_permission = 'permission_edit'

    def admin(self):
        return self.views()

    def administrator(self):
        return self.views()

    def del_permission(self, permissions):
        """
        删除用户权限
        :param permissions:需要删除的用户权限ID列表
        :return: 当权限列表为空的时候返回，不为空的时候没有返回
        """
        if not permissions:
            return
        temp = ''
        for index, temp_id in enumerate(permissions):
            temp += str(temp_id)
            if index < len(permissions) - 1:
                temp += ','
        deal_sql = r"""delete from tb_user_per where id in ({});""".format(temp)
        self._db.delete(deal_sql)

    def add_permission(self, uid, permissions):
        """
        添加用户权限
        :param uid: 添加权限用户ID
        :param permissions: 需要添加的权限列表
        :return:当权限列表为空的时候返回，不为空的时候没有返回
        """
        if not permissions:
            return
        insert_sql = r"""insert into tb_user_per(uid,pid) values {}"""
        temp = ''
        for index, temp_id in enumerate(permissions):
            temp += '({},{})'.format(uid, temp_id)
            if index < len(permissions) - 1:
                temp += ','
        self._db.insert(insert_sql.format(temp))

    def get_all_per(self):
        query = r"""select * from tb_permission;"""
        result = self._db.query(query)
        name_to_id = {}
        for item in result:
            name_to_id[item['Permission']] = item['ID']
        return name_to_id

    def get_new_permission_list(self, args):
        all_per_id = self.get_all_per()
        all_per = []
        for key in args.keys():
            if int(args.get(key, 0)) == 1:
                all_per.append(all_per_id[key])
        return all_per

    def views(self):
        args = self.args
        per_list = self.get_new_permission_list(loads(args.get('Permission')))
        query_per_sql = r"""select * from tb_user_per where uid = {};""".format(args.get('ID'))
        result = self._db.query(query_per_sql)
        # cur_per_list = [item['ID'] for item in result]
        del_per = []
        for item in result:
            if item['PID'] not in per_list:
                del_per.append(item['ID'])
        current_per = [item['PID'] for item in result]
        add_per = list(set(per_list) - set(current_per))
        self.del_permission(del_per)
        self.add_permission(int(args['ID']), add_per)
        return jsonify(status_code.SUCCESS)
