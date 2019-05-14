from json import loads

import random


def create_random_str(n):
    s = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    random_str = ''
    for i in range(n):
        random_str += random.choice(s)
    return random_str


def update_pic_and_group(tbname, cid, id_list, db, field='id'):
    if isinstance(id_list, str):
        id_list = loads(id_list)
    if id_list:
        update_pic = r"""update {} set cid = {} where {} in ({})""".format(tbname, cid, field, ','.join(
            map(lambda item: str(item), id_list)))
        db.update(update_pic)


def update_progress_pic(progressid, id_list, db):
    if id_list:
        update_progress = r"""update tb_pics set progressid = {} where id in ({})""".format(progressid,
                                                                                            ','.join(map(
                                                                                                lambda item: str(item),
                                                                                                id_list)))
        db.update(update_progress)
