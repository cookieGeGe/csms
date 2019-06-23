import time

from copy import deepcopy

from flask import jsonify, request

from utils import status_code
from utils.sqlutils import coon_mysql


@coon_mysql
def get_province(db, ID=0):
    # start_time = time.time()
    select_sql = r"""select ID,Name from tb_area where FatherID={};""".format(ID)
    result = db.query(select_sql)
    success = deepcopy(status_code.SUCCESS)
    success['province_list'] = result
    # print(time.time() - start_time)
    return jsonify(success)


@coon_mysql
def get_city(db, ID):
    select_sql = r"""select ID,Name from tb_area where FatherID={};""".format(ID)
    result = db.query(select_sql)
    success = deepcopy(status_code.SUCCESS)
    success['city_list'] = result
    return jsonify(success)


@coon_mysql
def get_district(db, ID):
    select_sql = r"""select ID,Name from tb_area where FatherID={};""".format(ID)
    result = db.query(select_sql)
    success = deepcopy(status_code.SUCCESS)
    success['distict_list'] = result
    return jsonify(success)
