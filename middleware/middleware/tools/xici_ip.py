# _*_ coding:utf-8 _*_

import requests
from fake_useragent import UserAgent
from scrapy import Selector

url = 'http://www.xicidaili.com/nn/1'

headers = {
    'User-Agent': UserAgent.random
}

response = requests.get(url, headers=headers)

selector = Selector(text=response.text)

for item in selector.xpath('//tables'):
    pass