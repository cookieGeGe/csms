from json import loads

from utils.sqlutils import OPMysql


class DealUser():

    def __init__(self):
        self.db = OPMysql()
        self.all_persons = None

    def get_all_Person(self):
        query_sql = r"""select id, person,remark from tb_progress"""
        result = self.db.query(query_sql)
        for item in result:
            item['person'] = loads(item['person'])
        self.all_persons = result
        print(self.all_persons)
        self.deal()

    def deal_person(self, person):
        new_remark = []
        if person['person']:
            for oneperson in person['person']:
                if oneperson['name'] == '' or oneperson['name'] is None:
                    continue
                new_person = r"""姓名：{name},电话:{phone},工种:{class},进场时间：{time},工资情况:{wage}""".format(**oneperson)
                new_remark.append(new_person)
        if person['remark'] != '' and person['remark'] != None:
            new_remark.append(person['remark'])
        return ';'.join(new_remark)

    def update_data(self, id, msg):
        update_sql = r"""
            update tb_progress set remark='{}' where id={};
        """.format(msg, id)
        self.db.update(update_sql)

    def deal(self):
        for item in self.all_persons:
            new_person = self.deal_person(item)
            self.update_data(item['id'], new_person)
            print('id:{} success!'.format(item['id']))


if __name__ == '__main__':
    user = DealUser()
    user.get_all_Person()
