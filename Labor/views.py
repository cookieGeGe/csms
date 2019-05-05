from flask import jsonify

from utils import status_code
from utils.BaseView import BaseView


class LaborBase(BaseView):

    def __init__(self):
        super(LaborBase, self).__init__()

    def administrator(self):
        return self.views()

    def admin(self):
        return self.views()

    def views(self):
        return jsonify(status_code.SUCCESS)


class CreateLabor(LaborBase):

    def __init__(self):
        super(CreateLabor, self).__init__()

    def views(self):
        return jsonify(status_code.SUCCESS)


class UpdateLabor(LaborBase):

    def __init__(self):
        super(UpdateLabor, self).__init__()

    def views(self):
        return jsonify(status_code.SUCCESS)


class DeleteLabor(LaborBase):

    def __init__(self):
        super(DeleteLabor, self).__init__()

    def views(self):
        return jsonify(status_code.SUCCESS)


class QueryLabor(LaborBase):

    def __init__(self):
        super(QueryLabor, self).__init__()

    def views(self):
        return jsonify(status_code.SUCCESS)
