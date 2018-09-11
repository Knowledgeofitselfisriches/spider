# -*- coding: utf-8 -*-
import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['tu.jiachong.net']
    start_urls = ['http://tu.jiachong.net/']

    def parse(self, response):
        pass
