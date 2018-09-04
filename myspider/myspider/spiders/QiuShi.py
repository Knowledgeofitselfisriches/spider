# -*- coding: utf-8 -*-
import scrapy

from myspider.items import QiuShiItem


class QiuShiSpider(scrapy.Spider):
    name = 'QiuShi'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/8hr/page/1/']

    def parse(self, response):
        articls = response.xpath('//div[contains(@id, "qiushi_tag")]')
        print(articls)
        for articl in articls:
            name = articl.xpath('./div[@class="author clearfix"]/a/h2/text()').extract_first()
            content = articl.xpath('./a[@class="contentHerf"]/div[@class="content"]/span').extract_first()
            item = QiuShiItem()
            item['name'] = name
            item['content'] = content
            print(item)
            yield item