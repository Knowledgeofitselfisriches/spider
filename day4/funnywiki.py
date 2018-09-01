# _*_ coding:utf-8 _*_
import threading

import requests
from lxml import etree
import json
import queue


def get_page():
    url = 'https://www.qiushibaike.com/8hr/page/1/'

    resp = requests.get(url)
    print(resp.text)
    html = etree.HTML(resp.content)
    nodes = html.xpath('//div[contains(@id, "qiushi_tag")]')
    item = {}
    articles = []
    for node in nodes:
        user_image = node.xpath('//div[contains(@id, "qiushi_tag")]/div[@class="author clearfix"]/a/img/@src')
        user_name = node.xpath('//div[contains(@id, "qiushi_tag")]/div[@class="author clearfix"]/a/h2/text()')
        content = node.xpath('//div[contains(@id, "qiushi_tag")]//div[@class="content"]/span/text()')
        like = node.xpath('//div[contains(@id, "qiushi_tag")]//div[@class="stats"]/span/i[@class="number"]/text()')
        comment = node.xpath('//div[contains(@id, "qiushi_tag")]//span[@class="stats-comments"]/a/i[@class="number"]/text()')

        if user_image:
            item['user_image'] = user_image[0]
        if user_name:
            item['user_name'] = user_name[0]
        if content:
            item['content'] = content[0]
        if like:
            item['like'] = like[0]
        if comment:
            item['comment'] = comment[0]
        articles.append(item)
    print(articles)
    with open('qiushi.json', 'w', encoding='utf-8') as f:
        for i in articles:
            jstr = json.dumps(i, ensure_ascii=False) + '\n'
            f.write(jstr)

class WiKiSpider(object):

    def get_content(self):
        url = 'https://www.qiushibaike.com/8hr/page/1/'
        resp = requests.get(url)
        return resp.content

    def extract(self,content):
        html = etree.HTML(content)
        nodes = html.xpath('//div[contains(@id, "qiushi_tag")]')
        return nodes
    def transform(self, node):
        item = {}
        user_image = node.xpath('//div[contains(@id, "qiushi_tag")]/div[@class="author clearfix"]/a/img/@src')
        user_name = node.xpath('//div[contains(@id, "qiushi_tag")]/div[@class="author clearfix"]/a/h2/text()')
        content = node.xpath('//div[contains(@id, "qiushi_tag")]//div[@class="content"]/span/text()')
        like = node.xpath('//div[contains(@id, "qiushi_tag")]//div[@class="stats"]/span/i[@class="number"]/text()')
        comment = node.xpath(
            '//div[contains(@id, "qiushi_tag")]//span[@class="stats-comments"]/a/i[@class="number"]/text()')

        if user_image:
            item['user_image'] = user_image[0]
        if user_name:
            item['user_name'] = user_name[0]
        if content:
            item['content'] = content[0]
        if like:
            item['like'] = like[0]
        if comment:
            item['comment'] = comment[0]

        return item

    def producer(self, queue):
        content = self.get_content()
        nodes = self.extract(content)
        for node in nodes:
            item = self.transform(node)
            if not queue.full():
                queue.put(item, block=False)

    def save(self, queue):
        with open('qiushi.json', 'w', encoding='utf-8') as f:
            if not queue.empty():
                jstr = json.dumps(queue.get_nowait(), ensure_ascii=False) + '\n'
                f.write(jstr)

if __name__ == '__main__':
    queue = queue.Queue(maxsize=10)
    p = threading.Thread(target=WiKiSpider.producer, args=(queue,))
    c1 = threading.Thread(target=WiKiSpider.save, args=(queue,))
    c2 = threading.Thread(target=WiKiSpider.save, args=(queue,))
    p.start()
    c1.start()
    c2.start()
