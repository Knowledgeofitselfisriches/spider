# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    subject_title = scrapy.Field()
    subject_url = scrapy.Field()

    sub_title = scrapy.Field()
    sub_url = scrapy.Field()
    tiezi_url = scrapy.Field()
    tiezi_path = scrapy.Field()

    tiezi_title = scrapy.Field()
    tiezi_content = scrapy.Field()

class DouBanItem(scrapy.Item):
    name = scrapy.Field()
    image = scrapy.Field()
    info = scrapy.Field()
    star = scrapy.Field()
    desc = scrapy.Field()
