from utils.sqlutils import OPMysql


def dict_deal(dict_data):
    temp = {}
    for key, value in dict_data.items():
        if isinstance(value, dict):
            temp[key.lower()] = dict_deal(value)
        elif isinstance(value, list):
            temp[key.lower()] = deal_list(value)
        else:
            temp[key.lower()] = value
    return temp


def deal_list(data_list):
    temp = []
    for i, item in enumerate(data_list):
        if isinstance(item, dict):
            item = dict_deal(item)
        elif isinstance(item, list):
            item = deal_list(item)
        else:
            item = item
        temp.append(item)
    return temp


def main():
    db = OPMysql()
    query_sql = db.query("""
    select b.id as id from tb_attendance as b group by b.year,b.month,b.day,b.laborid having count(laborid)>0
    """)
    ids_list = [str(item['id']) for item in query_sql]
    print(len(ids_list), ids_list)

    delete_sql = """
    select id from tb_attendance where projectid = 116 and id not in ({})
    """.format(','.join(ids_list))
    print(delete_sql)


if __name__ == '__main__':
    main()
