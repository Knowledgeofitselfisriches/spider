# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

import requests

from meizitu.settings import IMAGES_STORE


class MeizituPipeline(object):
    def open_spider(self, spider):
        self.file = open('meizitu.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        image_paths = []
        if not os.path.exists(IMAGES_STORE):
            os.makedirs(IMAGES_STORE)
        for image_url in item['image_urls']:
            file_name = image_url[7:].replace('/', '_')
            image_path = IMAGES_STORE + file_name

            if os.path.exists(image_path):
                image_paths.append(image_path)
                continue
            self.save(image_url, image_path)
            image_paths.append(image_path)
        item['image_paths'] = image_paths

        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def save(self, image_url, image_path):
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                for block in response.iter_content(4096):
                    if not block:
                        break
                    f.write(block)

