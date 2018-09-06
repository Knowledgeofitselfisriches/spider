# _*_ coding:utf-8 _*_
# 今日头条 ajax 动态加载 图片隐藏于js中 利用正则解析
import json
import os
import re
from hashlib import md5
from multiprocessing.pool import Pool
from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup
from requests import RequestException


def get_index(offset, keyword):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',

    }
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    # url = 'http://www.toutiao.com/search_content/?' + urlencode(data)  # 转为请求参数
    url = 'http://www.toutiao.com/search_content/'  # 转为请求参数
    response = requests.get(url, headers=headers, params=data, verify=False)
    print('index', 'ok')
    if response.status_code == 200:
        return response.text  # json


def parse_json(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_detail(url):
    if url is None:
        return None
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    response = requests.get(url, headers=headers, verify=False)
    return response.text


def parse_detail(detail_page):
    soup = BeautifulSoup(detail_page, 'lxml')
    title = soup.select('title')[0].get_text()
    images_pattern = re.compile('gallery: JSON.parse\\((.*?)\\)', re.S)
    images = re.search(images_pattern, detail_page)
    if images:
        images = json.loads(images.group(1))  # json.loads 不能转换单引号数据类型,json对象。
        image_url = re.findall('\\"(http.*?)\\"', images)
        image_url1 = []
        for i in image_url:
            image_url1.append(i.replace('\\', ''))
        data = {
            'title': title,
            'image_url': image_url1
        }
        return data  # 每一个详情页的数据


def download_image(image_url):
    response = requests.get(image_url)

    print('正在下载图片', image_url)
    if response.status_code == 200:
        save_image(response.content)


# 防止重复
def save_image(content):
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)


def main(offset):
    html = get_index(offset, '街拍')
    for url in parse_json(html):
        detail_page = get_detail(url)
        if html:
            image_urls = parse_detail(detail_page).get('image_url')
            if image_urls:
                for url in image_urls:
                    download_image(url)


if __name__ == '__main__':
    groups = [x*20 for x in range(1, 21)]

    pool = Pool()
    pool.map(main, groups)
