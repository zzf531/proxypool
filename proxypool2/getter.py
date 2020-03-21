from proxypool2.crawler import Crawler
from proxypool2.setting import *
from proxypool2.db import RedisClient

class Getter:
    def __init__(self):
        self.redis = RedisClient()
        self.crawler = Crawler()

    def is_over_threshold(self):
        if self.redis.count() >= POOL_UPPER_THRESHOLD:
            return True
        else:
            return False

    def run(self):
        if not self.is_over_threshold():

            for i in range(self.crawler.__all_Crawl_count__):
                call = self.crawler.__all_Crawl__[i]
                proxise = self.crawler.get_proxies(call)
                for proxy in proxise:
                    self.redis.add(proxy)


a = Getter()
a.run()


