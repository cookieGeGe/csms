# -*- coding: utf-8 -*-
# @Time : 2019/12/7
# @Author : zhang
# @Site :
# @File : public_view.py
# @Software: PyCharm
from flask import jsonify

from utils import status_code
from utils.BaseView import BaseView


class wechatPublicBase(BaseView):

    def __init__(self):
        super(wechatPublicBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def guest(self):
        return self.views()

    def views(self):
        pass


class wechatPics(wechatPublicBase):

    def __init__(self):
        super(wechatPics, self).__init__()

    def views(self):
        if self.args_is_null('id'):
            return jsonify(status_code.CONTENT_IS_NULL)
        query_sql = r"""select name, purl from tb_pics where groupid={};""".format(self.args.get('id'))
        result = self._db.query(query_sql)
        self.success['group_pics'] = result
        return self.make_response(self.success)
