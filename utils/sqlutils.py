import functools

from APP.functions import db


class MysqlDB():

    def __init__(self):
        self._db = db
        self._session = self._db.session

    def close(self):
        self._session.close()

    def query(self, sql):
        db_exe = self._session.execute(sql)
        data_list = list(map(lambda x: dict(zip(db_exe.keys(), x)), db_exe.fetchall()))
        return data_list

    def delete(self, sql):
        self._session.execute(sql)
        self._session.commit()

    def update(self, sql):
        self._session.execute(sql)
        self._session.commit()

    def insert(self, sql):
        db_exe = self._session.execute(sql)
        self._session.commit()
        return db_exe.lastrowid

    def execute(self, sql):
        sql_list = sql.split(';')
        for one_sql in sql_list:
            if one_sql != '':
                self._session.execute(one_sql+';')
        self._session.commit()


def coon_mysql(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        one_coon = MysqlDB()
        result = fn(one_coon, *args, **kwargs)
        one_coon.close()
        return result

    return wrapper
