# -*- coding: utf-8 -*-
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from hotline.items import HotlineItem


class DongguanSpider(CrawlSpider):
    name = 'Dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=30']

    rules = (
        Rule(LinkExtractor(allow=r'question/\d+/\d+\.shtml'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'type=\d+&page=\d+')),
    )

    def parse_item(self, response):
        url = response.url

        title_number = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract_first()
        # [\u4e00-\u9fa5] 提问：虎门镇龙眼社区发廊，通过微信群联系，上门联系，抬高发廊理发价格  编号:195555
        print(title_number)
        title_number = title_number.split("：")[1]

        title = title_number.split('\xa0\xa0')[0]
        number = title_number.split(":")[1]
        content = response.xpath("//div[@class='c1 text14_2']//text()").get()
        yield HotlineItem(url=url, title=title, number=number, content=content)
