# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymongo


class XinliangPipeline(object):
    def open_spider(self, spider):
        self.file = open('NEWS_SINA.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        item_dict = dict(item)

        dict_str = json.dumps(item_dict, ensure_ascii=False) + "\n"
        self.file.write(dict_str)
        return item

    def close_spider(self, spider):
        self.file.close()

class NewsTextPipeline(object):

    def process_item(self, item, spider):
        tiezi_content = item['tiezi_content']
        tiezi_url = item['tiezi_url']
        tiezi_path = item['tiezi_path']
        name = tiezi_url[7:tiezi_url.rfind('.')].replace('.', '_').replace('/', '_')
        file_name = tiezi_path + '/' + name + '.txt'
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(tiezi_content)
        return item

class DouBanPipeline(object):
    def open_spider(self, spider):
        self.file = open('movie_top_250.json', 'w', encoding='utf-8')
        db = pymongo.MongoClient(host='127.0.0.1', port=27017)
        douban = db['douban']
        self.sheet_name = douban['movie']
    def process_item(self, item, spider):
        item_dict = dict(item)

        dict_str = json.dumps(item_dict, ensure_ascii=False) + "\n"
        self.file.write(dict_str)
        self.sheet_name.insert(item_dict)
        return item

    def close_spider(self, spider):
        self.file.close()
