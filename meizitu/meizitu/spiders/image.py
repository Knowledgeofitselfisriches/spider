# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from meizitu.items import MeizituItem


class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['www.meizitu.com']
    url = 'http://www.meizitu.com/a/more_{}.html'
    page = 1
    start_urls = [url.format(page)]

    def tiezi_detail(self, response):

        url = response.url

        item = ItemLoader(item=MeizituItem(), response=response)
        item.add_value("url", url)
        item.add_xpath("title", '//h2/a/text()')
        item.add_xpath("image_urls", '//div[@id="picture"]/p/img/@src')

        return item.load_item()

    def parse(self, response):

        for teizi_url in response.xpath('//li[@class="wp-item"]//div[@class="pic"]//a[1]/@href').extract():
            yield scrapy.Request(teizi_url, callback=self.tiezi_detail)

        if self.page < 72:
            self.page += 1
            yield scrapy.Request(self.url.format(self.page), callback=self.parse)
