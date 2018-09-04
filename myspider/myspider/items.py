# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AtguiguItem(scrapy.Item):
    # 姓名：name
    name = scrapy.Field()
    # 职位：position
    position = scrapy.Field()
    # 简介：info
    info = scrapy.Field()
    # 特点：point
    futures = scrapy.Field()
    # 讲课风格：style
    style = scrapy.Field()
    # 图片：image
    image = scrapy.Field()

class QiuShiItem(scrapy.Item):
    # 姓名：name
    name = scrapy.Field()
    # 段子：position
    content = scrapy.Field()
