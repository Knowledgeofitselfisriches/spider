# _*_ coding:utf-8 _*_
from pyquery import PyQuery
import requests

html = requests.get('http://www.baidu.com').text
doc = PyQuery(html)
print(doc('meta'))
