# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/']

    custom_settings = {
        "COOKIES_ENABLED": True
    }

    def parse(self, response):
        print('请求的首页:', response.url)
        yield scrapy.FormRequest.from_response(
            response,
            formdata={"email": "18813228601", "password": "sentry@docker"},
            callback=self.home
        )

    def home(self, response):
        print("主页：", response.url)

        with open("Home.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        url = "http://www.renren.com/881820831/profile"
        yield scrapy.Request(url, callback=self.home_of_zhengshuang)

    def home_of_zhengshuang(self, response):
        print("请求的郑爽呢：", response.url)

        with open("郑爽Home.html", "w", encoding="utf-8") as f:
            f.write(response.text)
