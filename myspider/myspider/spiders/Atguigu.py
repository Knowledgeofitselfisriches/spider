# -*- coding: utf-8 -*-
import scrapy

from myspider.items import AtguiguItem


class AtguiguSpider(scrapy.Spider):
    name = 'Atguigu'
    allowed_domains = ['www.atguigu.com']
    start_urls = ['http://www.atguigu.com/teacher.shtml']

    def parse(self, response):
        for teacher in response.css('.teacher-con li'):
            name = teacher.css('.t-info h5 b:first-child').extract_first()

            position = teacher.css('.t-info h5 .b2').extract_first()

            info = teacher.css('.t-info .memo-i').extract_first()

            futures = teacher.css('.t-info a').extract_first()

            style = teacher.css('.t-info p:last-child').extract_first()
            image = teacher.css('.t-img img').extract_first()

            item = AtguiguItem()

            item['name'] = name
            item['position'] = position
            item['info'] = info
            item['futures'] = futures
            item['style'] = style
            item['image'] = image
            print(item)
            yield item
