import os
import time

import random
import re
from flask import jsonify

from APP.settings import BASE_DIR, upload_dir
from utils import status_code


def save_image(image_file, base='static/media/ava'):
    if not re.match('^image/.*$', image_file.mimetype):
        return jsonify(status_code.USER_UPLOAD_IMG_TYPE_ERROR)
    img_name = image_file.filename
    ticket = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    temp = ''
    for i in range(10):
        temp += random.choice(ticket)
    save_name = os.path.join(base, str(int(time.time())), temp, img_name)
    save_name = base + '/' + str(int(time.time())) + '_' + temp + '_' + img_name
    url = os.path.join(BASE_DIR, save_name)
    image_file.save(url)
    img_url = os.path.join('/static/media', save_name)
    return img_url


def get_all_area_id(db, area_list):
    temp_id = []
    for item in area_list:
        if item['HasChild']:
            temp_sql = r"""select * from tb_area where FatherID={}""".format(item['ID'])
            child_list = db.query(temp_sql)
            temp_id.append(get_all_area_id(db, child_list))
        else:
            temp_id.append(item['ID'])
    return temp_id
