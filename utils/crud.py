from flask import request, jsonify

from utils import BaseView, status_code


class InsertBaseView(BaseView):

    def __init__(self):
        super(InsertBaseView, self).__init__()

    def admin(self):
        pass

    def administrator(self):
        pass

    def guest(self):
        pass


class UpdateBaseView(BaseView):

    def __init__(self):
        super(UpdateBaseView, self).__init__()

    def admin(self):
        pass

    def administrator(self):
        pass

    def guest(self):
        pass


class DeleteBaseView(BaseView):

    def __init__(self):
        super(DeleteBaseView, self).__init__()
        self._tb_name = None

    def admin(self):
        self.administrator()

    def administrator(self):
        return self.views()

    def guest(self):
        self.administrator()

    def views(self):
        args = request.args
        delete_sql = r"""delete from {} where id = {}""".format(self._tb_name, args.get('ID'))
        try:
            self._db.delete(delete_sql)
            return jsonify(status_code.SUCCESS)
        except Exception as e:
            return jsonify(status_code.DB_ERROR)
