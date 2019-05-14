from flask import jsonify

from utils import status_code
from utils.BaseView import BaseView


class Permission(BaseView):

    def __init__(self):
        super(Permission, self).__init__()

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
        deal_sql = r"""delete from tb_user_per where pid in ({})""".format(temp)
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

    def views(self):
        args = self.args
        per_list = args['Permission_list']
        query_per_sql = r"""select * from tb_user_per where uid = {};""".format(args['UID'])
        result = self._db.query(query_per_sql)
        cur_per_list = [item['ID'] for item in result]
        add_per = list(set(per_list) - set(cur_per_list))
        del_per = list(set(cur_per_list) - set(per_list))
        self.del_permission(del_per)
        self.add_permission(int(args['UID']), add_per)
        return jsonify(status_code.SUCCESS)
