# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from meizitu.items import MeizituItem


class RuleCrawlSpider(CrawlSpider):
    name = 'rule_crawl'
    allowed_domains = ['www.meizitu.com']
    url = 'http://www.meizitu.com/a/more_{}.html'
    page = 1
    start_urls = [url.format(page)]

    rules = (

        Rule(LinkExtractor(allow=r'/a/\d+\.html'), callback='parse_page', follow=True),
        Rule(LinkExtractor(allow=r'more_\d+\.html')),
    )

    def parse_page(self, response):
        url = response.url

        item = ItemLoader(item=MeizituItem(), response=response)
        item.add_value("url", url)
        item.add_xpath("title", '//h2/a/text()')
        item.add_xpath("image_urls", '//div[@id="picture"]/p/img/@src')
        print(item.load_item())
        # return item.load_item()

