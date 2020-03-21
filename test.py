import requests
from selenium import webdriver

url = 'https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/solution/python-chao-ji-kuai-zui-sha-gua-xie-fa-ming-ming-b/'
rsp = requests.get(url)
browser = webdriver.Chrome()

browser.get(url)
browser.close()
