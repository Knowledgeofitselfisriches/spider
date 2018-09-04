# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your h to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

import scrapy
from scrapy.pipelines.images import ImagesPipeline

from txspider.settings import IMAGES_STORE


class TxspiderPipeline(object):
    # 开始时执行
    def open_spider(self, spider):
        self.file = open('position.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item_dict = dict(item)

        dict_str = json.dumps(item_dict, ensure_ascii=False) + "\n"
        self.file.write(dict_str)

        return item

    # 结束时执行
    def close_spider(self, spider):
        self.file.close()


class LeTVPipeline(object):
    def open_spider(self, spider):
        self.file = open('letv.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item_dict = dict(item)

        dict_str = json.dumps(item_dict, ensure_ascii=False) + "\n"
        self.file.write(dict_str)

        return item

    # 结束时执行
    def close_spider(self, spider):
        self.file.close()


class LeTVImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        image = item['image']
        yield scrapy.Request(image)

    def item_completed(self, results, item, info):
        image_name = [x['path'] for ok, x in results if ok][0]
        origin = IMAGES_STORE + '/' + image_name
        modify = IMAGES_STORE + '/' + item['nick'] + '.jpg'
        os.rename(origin, modify)
        item['path'] = modify
        return item
