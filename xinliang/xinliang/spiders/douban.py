# -*- coding: utf-8 -*-
import scrapy

from xinliang.items import DouBanItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    offset = 0
    url = "https://movie.douban.com/top250?start={}&filter="
    start_urls = [url.format(offset)]
    custom_settings = {
        'COOKIES_ENABLED' : True
    }
    cookie = {
        'll': '"108288"',
        'bid': 'KeVcu7zQ0nE',
        'ps': 'y',
        '_ga': 'GA1.2.1639487160.1535765457',
        '__yadk_uid': 'VcGTqCCB7pjrZCKIJfqP5Ho5oMb1wCNa',
        'push_noty_num': '0',
        'push_doumail_num': '0',
        '__utmv': '30149280.18394',
        '__utma': '30149280.1639487160.1535765457.1536134862.1536288790.8',
        '__utmc': '30149280',
        '__utmz=30149280.1536288790.8.7.utmcsr=baidu|utmccn=(organic)|utmcmd': 'organic',

        'ap_v': '0,6.0',
        '_vwo_uuid_v2': 'D8C668519F369021AEDFA97A8E1C011E4|472f9d52e08099bc50d135973a3b3a7a',
        '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1536288881%2C%22https%3A%2F%2Fmovie.douban.com%2F%22%5D',
        '_pk_ses.100001.8cb4': '*',
        'SL_GWPT_Show_Hide_tmp': '1',
        'SL_wptGlobTipTmp': '1',
        'ct': 'y',
        '_gid': 'GA1.2.1417511983.1536290429',
        'dbcl2': '"183944973:qnj9cUOBgfY"',
        'ck': 'm55y',
        'douban-profile-remind': '1',
        '_pk_id.100001.8cb4': 'ce0782a175164389.1535765454.5.1536292066.1535938368.',
        '__utmt': '1',
        '__utmb': '30149280.16.10.1536288790',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url, cookies=self.cookie, callback=self.parse)
        if self.offset <= 225:
            self.offset += 25
        yield scrapy.Request(self.url.format(self.offset), callback=self.parse)

    def parse(self, response):
        print(response.url)
        for node in response.xpath('//div[@class="item"]'):
            name = node.xpath('.//span[@class="title"][1]/text()').extract_first()
            image = node.xpath('.//div[@class="pic"]/a/img/@src').extract_first()
            info = node.xpath('.//div[@class="bd"]/p[1]/text()').extract_first()
            if info:
                info = ''.join(info)
            star = node.xpath('.//div[@class="star"]/span/text()').extract_first()
            desc = node.xpath('.//span[@class="inq"]/text()')
            if desc:
                desc = desc.extract_first()

            item = DouBanItem(name=name, image=image, info=info, star=star, desc=desc)
            yield item

