# -*- coding: utf-8 -*-
import os

import scrapy

from xinliang.items import SinaItem


class SinaGuideSpider(scrapy.Spider):
    name = 'sina_guide'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        # 内容聚合的新闻总分类
        subject_titles = response.xpath(
            '//div[@id="tab01"]/div[@class="clearfix"]/h3[@class="tit02"]/a/text()').extract()
        subject_urls = response.xpath('//div[@id="tab01"]/div[@class="clearfix"]/h3[@class="tit02"]/a/@href').extract()
        # 子新闻资讯入口
        sub_titles = response.xpath('//div[@id="tab01"]//ul[@class="list01"]/li/a/text()').extract()
        sub_urls = response.xpath('//div[@id="tab01"]//ul[@class="list01"]/li/a/@href').extract()
        for index, subject_url in enumerate(subject_urls):
            subject_title = subject_titles[index]

            for sub_index, sub_url in enumerate(sub_urls):
                sub_title = sub_titles[sub_index]

                if sub_url.startswith(subject_url):
                    path = './datas/' + subject_title + '/' + sub_title
                    if not os.path.exists(path):
                        os.makedirs(path)

                    item = SinaItem(subject_title=subject_title, subject_url=subject_url,
                                    sub_title=sub_title, sub_url=sub_url, tiezi_path=path)
                    yield scrapy.Request(sub_url, callback=self.second_detail, meta={'item': item})

    def second_detail(self, response):
        item = response.meta['item']
        urls = response.xpath('//a/@href').extract()
        subject_url = item['subject_url']

        for url in urls:
            if url.startswith(subject_url) and url.endswith('.shtml'):
                yield scrapy.Request(url, callback=self.tiezi_detail, meta={'item': item})

    def tiezi_detail(self, response):
        item = response.meta['item']
        tiezi_title = response.xpath("//h1[@id='artibodyTitle']/text()|//h1[@class='main-title']/text()").extract()
        tiezi_content = response.xpath("//div[@id='artibody']//p//text()|//div[@class='article']//p//text()").extract()
        tiezi_content = "".join(tiezi_content)

        item['tiezi_url'] = response.url
        item['tiezi_title'] = tiezi_title
        item['tiezi_content'] = tiezi_content

        yield item



