# -*- coding: utf-8 -*-
import scrapy


class RenrensessionSpider(scrapy.Spider):
    name = 'renrensession'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        pass
