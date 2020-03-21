from proxypool2.utils import get_page
from pyquery import PyQuery as pq


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__all_Crawl__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__all_Crawl__'].append(k)
                count += 1
        attrs['__all_Crawl_count__'] = count
        return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):

    def get_proxies(self, callback):
        proxies = []
        for proxy in eval("self.{}()".format(callback)):
            proxies.append(proxy)
            print(proxy)
        return proxies

    def crawl_66(self, page_count=2):
        """
        获取66代理网站代理
        :param page_count: 爬取页面数量
        :return: 代理
        """
        start_url = 'http://www.66ip.cn/{}.html'
        urls = [start_url.format(page) for page in range(1, page_count+1)]
        for url in urls:
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth_child(1)').text()
                    port = tr.find('td:nth_child(2)').text()
                    yield ':'.join([ip, port])


if __name__ == '__main__':
    crawl = Crawler()
    print(crawl.__all_Crawl_count__)
    for i in range(crawl.__all_Crawl_count__):
       call = crawl.__all_Crawl__[i]
       proxy = crawl.get_proxies(call)

