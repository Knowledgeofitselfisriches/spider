# _*_ coding:utf-8 _*_
import os

import requests
from lxml import etree


class TieBaSpider(object):

    def download_index(self, url, params):
        resp = requests.get(url, params=params, allow_redirects=False)
        print(resp.url)
        if resp.status_code == 200:
            return resp.content

    def get_content(self, url, kw, params, start, end):
        for n in range(start, end + 1):
            pn = (n - 1) * 50
            full_url = url + "&pn=" + str(pn)
            content = self.download_index(full_url, params)
            print(content)
            self.save_tb_urls(content, n, kw)

    def save_tb_urls(self, content, n, kw):
        print('正在获取第', str(n), '的连接')
        html = etree.HTML(content)
        tiezi_urls = html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
        for tiezi_url in tiezi_urls:
            self.get_image_urls(tiezi_url)

    def get_image_urls(self, tiezi_url):
        tiezi_url = 'https://tieba.baidu.com' + tiezi_url
        response = requests.get(tiezi_url)
        html = etree.HTML(response.content)
        image_urls = html.xpath('//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src')

        for image_url in image_urls:
            self.download_image(image_url)

    def download_image(self, image_url):
        print('正在下载的图片：', image_url)
        response = requests.get(image_url)
        dirs, file = os.path.split(image_url)
        if response.status_code == 200:
            with open(file, 'wb') as fw:
                for block in response.iter_content(1024):
                    if not block:
                        break
                    fw.write(block)

    def main(self):
        url = "https://tieba.baidu.com/f?ie=utf-8"
        kw = input("请输入您要爬取贴吧的名称：")
        params = {"kw": kw}
        start = int(input("请输入您要爬取起始页（从1开始）:"))
        end = int(input("请输入爬取的截止页："))
        self.get_content(url, kw, params, start, end)


class Spider52(object):
    def __init__(self):
        self.file = open('title.txt', 'ab')

    def get_page(self, end ):
        for i in range(end):
            url = f'https://www.52pojie.cn/forum-21-{i}.html'
            resp = requests.get(url)
            content = resp.text
            self.get_href(content)
            # self.get_title(content)

    def get_href(self, content):
        html = etree.HTML(content)
        href = html.xpath('')
    # def get_title(self, content):

if __name__ == '__main__':
    # TieBaSpider().main()
    Spider52().get_page(1)
