import os
import time

import random
import re
from flask import jsonify

from APP.settings import BASE_DIR, upload_dir
from utils import status_code
from utils.ImageCompress import CompressImage


def save_image(image_file, base='static/media/ava'):
    if not re.match('^image/.*$', image_file.mimetype):
        return jsonify(status_code.USER_UPLOAD_IMG_TYPE_ERROR)
    img_name = image_file.filename
    ticket = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    temp = ''
    for i in range(10):
        temp += random.choice(ticket)
    new_base = os.path.join(*base.split(r'/'))
    new_name = str(int(time.time())) + '_' + temp + '.' + img_name.split('.')[-1]
    save_name = os.path.join(new_base, new_name)
    url = os.path.join(BASE_DIR, save_name)
    image_file.save(url)
    try:
        compress = CompressImage(url)
        compress.default_compress_image()
    except Exception as e:
        print(e)
        pass
    img_url = '/' + base + '/' + new_name
    return img_url


def save_other_file(image_file, base='static/media/otherfile'):
    img_name = image_file.filename
    ticket = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    temp = ''
    for i in range(10):
        temp += random.choice(ticket)
    new_base = os.path.join(*base.split(r'/'))
    new_name = str(int(time.time())) + '_' + temp + '.' + img_name.split('.')[-1]
    save_name = os.path.join(new_base, new_name)
    url = os.path.join(BASE_DIR, save_name)
    image_file.save(url)
    img_url = '/' + base + '/' + new_name
    return img_name, img_url


def get_all_area_id(db, area_list):
    temp_id = []
    for item in area_list:
        if item['HasChild']:
            temp_sql = r"""select * from tb_area where FatherID={}""".format(item['ID'])
            temp_id.append(item['ID'])
            child_list = db.query(temp_sql)
            temp_id += get_all_area_id(db, child_list)
        else:
            temp_id.append(item['ID'])
    return temp_id
