import json
from proxypool.utils import get_page
from pyquery import PyQuery as pq


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            # print('成功过去代理', proxy)
            proxies.append(proxy)
        return proxies

    def crawl_daili66(self, page_count=2):
        """
        获取代理66
        :param page_count: 网站的页码
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('正在爬取得链接', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])


crawl = Crawler()
print(crawl.__CrawlFuncCount__)
# for i in range(crawl.__CrawlFuncCount__):
#     callback = crawl.__CrawlFunc__[i]
#     print('类名', callback)
#     a = crawl.get_proxies(callback)
#
#     print(a)
#     print('__')