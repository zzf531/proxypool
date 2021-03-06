from pyquery import PyQuery as pq
import requests
from bs4 import BeautifulSoup
base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}

def get_page(url, options={}):
    """
    抓取代理
    :param url:
    :param options:
    :return: 网页文字
    """
    headers = dict(base_headers, **options)
    print('正在抓取的url', url)
    try:
        response = requests.get(url, headers=base_headers)
        if response.status_code == 200:
            print('抓取成功', url, response.status_code)
            return response.text
    except ConnectionError:
        print('抓取失败', url)
        return None



url = 'http://www.66ip.cn/3.html'
html = get_page(url)
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
if html:
    doc = pq(html)
    trs = doc('.containerbox table tr:gt(1)').items()
    for tr in trs:
        ip = tr.find('td:nth-child(1)').text()
        port = tr.find('td:nth-child(2)').text()
        print(':'.join([ip, port]))
