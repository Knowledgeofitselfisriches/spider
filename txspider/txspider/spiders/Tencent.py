# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from txspider.items import TXItem


class TencentSpider(CrawlSpider):
    name = 'Tencent'
    allowed_domains = ['hr.tencent.com']
    url = 'https://hr.tencent.com/position.php?&start={}#a'
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
    offset = 0
    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )
    count = 1

    def parse_item(self, response):
        total = response.xpath('//span[@class="lightblue total"]/text()').get()
        for item_data in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):

            name = item_data.xpath('./td[1]/a/text()').get()
            job = item_data.xpath('./td[2]/text()').get()
            nums = item_data.xpath('./td[3]/text()').get()
            address = item_data.xpath('./td[4]/text()').get()
            publish = item_data.xpath('./td[5]/text()').get()
            link = item_data.xpath('./td[1]/a/@href').get()

            item = TXItem(name=name, job=job, nums=nums, address=address, publish=publish, link=link)
            TencentSpider.count += 1
            yield item


