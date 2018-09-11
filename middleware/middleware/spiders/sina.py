# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SinaSpider(CrawlSpider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    # start_urls = ['http://sina.com.cn/']

    # start_urls = ['http://118.190.202.67:8000/test/']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        print('=====================', response.url)
        print('=====================', response.text)