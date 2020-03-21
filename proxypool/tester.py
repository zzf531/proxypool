import asyncio
import aiohttp
import time
import sys
try:
    from aiohttp import ClientError
except:
    from aiohttp import ClientProxyConnectionError as ProxyConnectionError
from proxypool.db import RedisClient
from proxypool.setting import *


class Tester:
    def __init__(self):
        self.redis = RedisClient()

    async def test_single_proxy(self, proxy):
        """
        测试单个代理
        :param proxy:
        :return:
        """
        conn = aiohttp.TCPConnector(ssl=False)
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                if isinstance(proxy, bytes):  # 判断是不是bytes类型
                    proxy = proxy.decode('utf-8')
                real_proxy = 'http://' + proxy
                print('正在测试')
                async with session.get(TEST_URL, proxy=real_proxy, timeout=15, allow_redirects=False) as response:
                    if response.status in VALID_STATUS_CODES:  # 状态码是否为200,302
                        self.redis.max(proxy)  # 代理可用就改变代理的分数为100
                        print('代理可用', proxy)
                    else:
                        self.redis.decrease(proxy)  # 代理减分
                        print('请求响应码不合理', response.status, 'IP', proxy)
            except (ClientError, aiohttp.client_exceptions.ClientConnectorError, asyncio.TimeoutError, AttributeError):
                self.redis.decrease(proxy)
                print('代理请求失败______________', proxy)

    def run(self):
        """
        检测主函数
        :return:
        """
        print('检测器开始运行')
        try:
            count = self.redis.count()  # 获取proxies数量
            print('当前剩余', count, '个代理')
            for i in range(0, count, BATCH_TEST_SIZE):  # 最大批测试量BATCH_TEST_SIZE = 10
                start = i
                stop = min(i + BATCH_TEST_SIZE, count)
                print('正在测试第', start + 1, '-', stop, '个代理')
                test_proxies = self.redis.batch(start, stop)  # 批量获取
                loop = asyncio.get_event_loop()
                tasks = [self.test_single_proxy(proxy) for proxy in test_proxies]
                loop.run_until_complete(asyncio.wait(tasks))
                sys.stdout.flush()
                time.sleep(5)
        except Exception as e:
            print('测试器发生错误', e.args)


tester = Tester()
tester.run()
