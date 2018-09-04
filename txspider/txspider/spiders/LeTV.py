# -*- coding: utf-8 -*-
import os
import shutil

import scrapy
import json

from scrapy import Request

from txspider.items import LeTVItem
from txspider.settings import IMAGES_STORE


class LeTvSpider(scrapy.Spider):
    name = 'LeTV'
    allowed_domains = ['letv.com']
    page = 1
    # start_url = f'http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=8.1&channelId=2168&pages={str(page)}&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN'
    # start_urls = [start_url]

    url = 'http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=8.1&channelId=2168&pages={}&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN'

    if os.path.exists(IMAGES_STORE):
        shutil.rmtree(IMAGES_STORE)

    def start_requests(self):
        for i in range(1, 4):
            yield Request(self.url.format(i), callback=self.parse)

    # def parse(self, response):
    #     print("-------------------------------", response.url)
    #     data = json.loads(response.text, encoding='utf-8')
    #     for info in data["body"]["result"]:
    #
    #         nick = info['nick']
    #         image = info['screenshot']
    #         liveUrl = info['liveUrl']
    #
    #         item = LeTVItem(nick=nick, image=image, liveUrl=liveUrl)
    #         print(item)
    #         yield item
    #         if self.page < 100:
    #             self.page += 1
    #         new_url = self.start_url
    #         print(new_url)
    #         request = scrapy.Request(new_url, callback=self.parse)
    #         yield request

    def parse(self, response):
        datas = json.loads(response.body, encoding='utf-8')['body']['result']
        for data in datas:
            nick = data.get('nick')
            image = data.get('screenshot')
            liveUrl = data.get('liveUrl')
            path = os.path.join(IMAGES_STORE, 'full', nick + '.jpg')
            yield LeTVItem(nick=nick, image=image, liveUrl=liveUrl, path=path)
