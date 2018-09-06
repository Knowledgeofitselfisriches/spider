# -*- coding: utf-8 -*-
import scrapy
from hotline.items import HotlineItem


class Dongguan2Spider(scrapy.Spider):
    name = 'Dongguan2'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page={}'

    def start_requests(self):
        for i in range(0, 120, 30):
            yield scrapy.Request(self.url.format(i), callback=self.parse)

    def parse(self, response):

        artical_urls = response.xpath('//a[@class="news14"]/@href').extract()
        for artical in artical_urls:
            yield scrapy.Request(artical, callback=self.get_detail)

    def get_detail(self, response):

        url = response.url
        title_number = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()
        title_number = title_number.split("：")[1]
        title = title_number.split('\xa0\xa0')[0]
        number = title_number.split(":")[1]
        content = response.xpath("//div[@class='c1 text14_2']//text()").get()

        yield HotlineItem(url=url, title=title, number=number, content=content)
