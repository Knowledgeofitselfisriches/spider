# -*- coding: utf-8 -*-
import os
import re

import scrapy
from scrapy import Request

from myspider.items import AtguiguItem
from myspider.settings import IMAGES_STORE


class AtguiguSpider(scrapy.Spider):
    name = 'Atguigu'
    allowed_domains = ['www.atguigu.com']
    # start_urls = ['http://www.atguigu.com/teacher.shtml']
    url = 'http://www.atguigu.com/teacher.shtml'

    def start_requests(self):
        yield Request(self.url, callback=self.parse)

    def parse(self, response):
        for teacher in response.css('.teacher-con li'):
            name = teacher.css('.t-info h5 b:first-child').extract_first()

            position = teacher.css('.t-info h5 .b2').extract_first()

            info = teacher.css('.t-info .memo-i').extract_first()

            futures = teacher.css('.t-info a').extract_first()

            style = teacher.css('.t-info p:last-child').extract_first()
            imageurl = teacher.css('.t-img img').extract_first()
            # <img src="teacher/new/weiyunhui.jpg" alt="" hspace="8">
            pattern = re.compile('<img src="teacher/new/(\w+?).jpg" alt="" hspace="8">')
            nickname = pattern.search(imageurl).group(1)
            path = os.path.join(IMAGES_STORE, f'full/{nickname}.jpg')

            item = AtguiguItem(name=name, position=position, info=info, futures=futures, style=style,
                               imageurl=imageurl, path=path)
            yield item
