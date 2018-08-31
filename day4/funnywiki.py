# _*_ coding:utf-8 _*_
import requests
from lxml import etree
import json


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

if __name__ == '__main__':
    get_page()