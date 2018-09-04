# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TXItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    job = scrapy.Field()
    nums = scrapy.Field()
    address = scrapy.Field()
    publish = scrapy.Field()
    link = scrapy.Field()


class LeTVItem(scrapy.Item):

    nick = scrapy.Field()
    image = scrapy.Field()
    liveUrl = scrapy.Field()
    path = scrapy.Field()
