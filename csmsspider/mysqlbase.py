import pymysql
from DBUtils.PooledDB import PooledDB

mysqlInfo = {
    "host": '127.0.0.1',
    "user": 'root',
    "passwd": 'admin123',
    "db": 'csmstest',
    "port": 3306,
    "charset": 'utf8'
}


class OPMysql(object):
    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.pool = OPMysql.getmysqlconn()
        # self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)

    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        if OPMysql.__pool is None:
            __pool = PooledDB(creator=pymysql,
                              mincached=20,
                              maxconnections=40,
                              blocking=True,
                              host=mysqlInfo['host'],
                              user=mysqlInfo['user'],
                              passwd=mysqlInfo['passwd'],
                              db=mysqlInfo['db'],
                              port=mysqlInfo['port'],
                              charset=mysqlInfo['charset'])
            # print(__pool)
        # return __pool.connection()
        return __pool

    def connection(self):
        coon = self.pool.connection()
        cur = coon.cursor(cursor=pymysql.cursors.DictCursor)
        return coon, cur

    # 插入\更新\删除sql
    def op_update(self, sql, *args):
        # print('op_insert', sql)
        coon, cur = self.connection()
        insert_num = cur.execute(sql, *args)
        # print('mysql sucess ', insert_num)
        coon.commit()
        self.closeall(cur, coon)
        return insert_num

    # 查询
    def op_select(self, sql, *args):
        # print('op_select', sql)
        coon, cur = self.connection()
        cur.execute(sql, *args)  # 执行sql
        select_res = cur.fetchall()  # 返回结果为字典
        # print('op_select', select_res)
        self.closeall(cur, coon)
        return select_res

    # 释放资源
    def closeall(self, cur, coon):
        # pass
        cur.close()
        coon.close()


mysql_con = OPMysql()
