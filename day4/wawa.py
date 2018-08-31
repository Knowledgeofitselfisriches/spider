# _*_ coding:utf-8 _*_
import os

import requests
from bs4 import BeautifulSoup
import re


def download_image(image_url):
    print('正在下载的图片：', image_url)
    response = requests.get(image_url)
    dirs, file = os.path.split(image_url)
    if response.status_code == 200:
        with open(file, 'wb') as fw:
            for block in response.iter_content(1024):
                if not block:
                    break
                fw.write(block)


def get_image_url():
    url = 'http://acg.gamersky.com/pic/201808/1087500_8.shtml'

    resp = requests.get(url)

    content = resp.content

    soup = BeautifulSoup(content, 'lxml')

    for h3 in soup.find_all(href=re.compile(r'.jpg$')):
        img_ul = h3.attrs['href']
        download_image(img_ul)


if __name__ == '__main__':
    get_image_url()
