import re
import redis
from proxypool2.setting import *
from random import choice
from proxypool.error import PoolEmptyError


class RedisClient:
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        """
        数据库链接
        :param host: 地址
        :param port: 端口
        :param password: 密码
        """
        self.db = redis.StrictRedis(host=host, port=port, password=password)

    def add(self, proxy, score=INITIAL_SCORE):
        """
        添加代理,设置最高分,最高分就是键名
        :param proxy: 存储到redis,有序集合的值,值不能重复
        :param score: 存储到redis,有序集合的键,键可以重复
        :return: 添加结构
        先判断代理是否符合规范,在判断数据库里是否有这条数据
        如果没有,就zadd到数据库
        """
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):
            print('代理不符合规范,丢弃', proxy)
            return
        if not self.db.zscore(REDIS_KEY,proxy):
            print('我正在添加代理', proxy)
            return self.db.zadd(REDIS_KEY, {proxy: score})

    def count(self):
        """
        获取数量
        :return: 数量
        """
        return self.db.zcard(REDIS_KEY)

    def max(self, proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结构
        """
        return self.db.zadd(REDIS_KEY, {proxy, MAX_SCORE})


    def decrease(self, proxy):
        """
        代理值减一分,小于最小值,直接删除
        :param proxy: 代理
        :return: 修改后代理的分数
        """
        score = self.db.zscore(REDIS_KEY, proxy)
        if score and score > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减一分')
            return self.db.zincrby(REDIS_KEY, -1, proxy)
        else:
            print('代理', proxy, '当前分数', score, '移除')
            return self.db.zrem(REDIS_KEY, proxy)

    def batch(self, start, stop):
        """
        批量获取
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        return self.db.zrevrange(REDIS_KEY, start, stop - 1)

    def random(self):
        """
        随机获取有效代理,首先尝试获取最高分代理
        如果不存在,按照排名获取,否则异常
        :return: 随机代理
        """
        result = self.db.zrangebyscore(REDIS_KEY, MAX_SCORE, MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            result = self.db.zrevrange(REDIS_KEY, 0, 100)
            if len(result):
                return choice(result)
            else:
                raise PoolEmptyError
