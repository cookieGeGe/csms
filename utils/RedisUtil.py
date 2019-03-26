import redis

from APP.settings import redisInfo


class OPRedis(object):
    __pool = None
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(OPRedis, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.pool = OPRedis.getRedisCoon()

        self.chan_sub = 'change_dev'
        self.chan_pub = 'change_dev'

    @staticmethod
    def getRedisCoon():
        if OPRedis.__pool is None:
            __pool = redis.ConnectionPool(host=redisInfo['host'], password=redisInfo['password'],
                                          port=redisInfo['port'], db=redisInfo['db'])
            # print(__pool)
        return __pool

    """
    string类型 {'key':'value'} redis操作
    """

    def getpool(self):
        if not self.pool:
            raise Exception('Redis连接池未初始化')
        return self.pool

    def _get_coon(self):
        return redis.Redis(connection_pool=self.pool)

    def update_expire(self, name, time):
        coon = self._get_coon()
        res = coon.expire(name, time)
        return res

    def setredis(self, key, value, time=None):
        coon = self._get_coon()
        # 非空即真非0即真
        if time:
            res = coon.setex(key, time, value)
        else:
            res = coon.set(key, value)
        return res

    def getRedis(self, key):
        coon = self._get_coon()
        res = coon.get(key)
        return res

    def delRedis(self, key):
        coon = self._get_coon()
        res = coon.delete(key)
        return res

    """
    hash类型，{'name':{'key':'value'}} redis操作
    """

    def setHashRedis(self, name, key, value):
        coon = self._get_coon()
        res = coon.hset(name, key, value)
        return res

    def getHashRedis(self, name, key=None):
        coon = self._get_coon()
        # 判断key是否我为空，不为空，获取指定name内的某个key的value; 为空则获取name对应的所有value
        if key:
            res = coon.hget(name, key)
        else:
            res = coon.hgetall(name)
        return res

    def delHashRedis(self, name, key=None):
        coon = self._get_coon()
        if key:
            res = coon.hdel(name, key)
        else:
            res = coon.delete(name)
        return res

    def getkeys(self):
        coon = self._get_coon()
        res = coon.keys()
        return res

    def rpushredis(self, key, *args):
        coon = self._get_coon()
        res = coon.rpush(key, *args)
        return res

    # 发送消息
    def public(self, channel, msg):
        coon = self._get_coon()
        coon.publish(channel, msg)
        return True

    # 订阅
    def subscribe(self, channel):
        coon = self._get_coon()
        # 打开收音机
        pub = coon.pubsub()
        # 调频道
        pub.subscribe(channel)
        # 准备接收
        pub.parse_response()
        return pub


RedisCon = OPRedis()
