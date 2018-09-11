# -*- coding: utf-8 -*-
import scrapy


class LogindemoSpider(scrapy.Spider):
    name = 'logindemo'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/post']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(
                url = url,
                formdata={'name':'cwq', 'password': '123456'},
                callback=self.parse
            )

    def parse(self, response):
        pass
