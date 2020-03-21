import time
from multiprocessing import Process
from proxypool2.setting import *
from proxypool2.tester import Tester  # 测试模块
from proxypool2.getter import Getter  # 获取器类
from proxypool2.api import app  # 接口模块

class Scheduler():
    def schedule_tester(self, cycle=TESTER_CYCLE):
        """
        定时测试代理, 调度测试模块
        :param cycle:
        :return:
        """
        tester = Tester()
        while True:
            print('测速器开始运行')
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self, cycle=GETTER_CYCLE):
        """
        定时获取代理
        :param cycle:
        :return:
        """
        getter = Getter()
        while True:
            print('开始抓取代理')
            getter.run()
            time.sleep(cycle)

    def schedule_api(self):
        """
        开启API API配置,接口模块
        :return:
        """
        app.run(API_HOST, API_PORT)

    def run(self):
        print('代理池开始运行')

        if TESTER_ENABLED:
            tester_process = Process(target=self.schedule_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()