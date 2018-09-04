# -*- coding: utf-8 -*-
import scrapy

from txspider.items import TXItem


class TxSpider(scrapy.Spider):
    name = 'TX'
    offset = 0
    allowed_domains = ['hr.tencent.com']
    start_urls = [f'https://hr.tencent.com/position.php?start={str(offset)}#a']

    def parse(self, response):
        print(response.url)
        total = response.xpath('//span[@class="lightblue total"]/text()')
        for item_data in response.xpath('//tr[@class="even"]|//tr[@class="odd"]'):

            name = item_data.xpath('./td[1]/a/text()').get()
            job = item_data.xpath('./td[2]/text()').get()
            nums = item_data.xpath('./td[3]/text()').get()
            address = item_data.xpath('./td[4]/text()').get()
            publish = item_data.xpath('./td[5]/text()').get()
            link = item_data.xpath('./td[1]/a/@href').get()

            item = TXItem(name=name, job=job, nums=nums, address=address, publish=publish, link=link)

            yield item
            if self.offset < total:
                self.offset += 10
            next_url = f'https://hr.tencent.com/position.php?start={str(self.offset)}#a'
            print('--------------------', next_url)
            request = scrapy.Request(next_url, callback=self.parse)
            yield request


