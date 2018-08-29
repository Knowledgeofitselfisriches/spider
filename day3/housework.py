import requests
from lxml import etree
import os


class NeiHan(object):
    def __init__(self):
        self.file = open('段子.txt', 'a', encoding='utf-8')

    def spider_paragraph(self, content):
        html = etree.HTML(content)
        texts = html.xpath('//div[@class="f18 mb20"]/text()')

        for item in texts:
            item = item.replace(' ', '')
            self.file.write(item)

        print('段子爬取成功！')

    def get_content(self, start_page, end_page):
        for i in range(start_page, end_page + 1):
            url = 'https://www.neihan8.com/article/list_5_' + str(i) + '.html'
            response = requests.get(url)
            content = response.content.decode('gbk')

            print('正在获取第', str(i), '页！')
            self.spider_paragraph(content)
        self.close()

    def close(self):
        self.file.close()

    def start(self):
        start = int(input('起始爬取页:'))
        end = int(input('结束爬取页：'))
        self.get_content(start, end)


class TieBa(object):

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


    def get_image_urls(self, tiezi_url):
        tiezi_url = 'https://tieba.baidu.com' + tiezi_url
        response = requests.get(tiezi_url)
        html = etree.HTML(response.content)
        image_urls = html.xpath('//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src')

        for image_url in image_urls:
            self.download_image(image_url)

    def save_tb_urls(self, content, n, kw):
        print('正在获取第', str(n), '的连接')
        html = etree.HTML(content)
        tiezi_urls = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        for tiezi_url in tiezi_urls:
            self. get_image_urls(tiezi_url)

    def download_index(self, full_url, params):
        """获取index.html"""
        response = requests.get(full_url, params=params)
        print(response.url)

        content = response.content
        return content

    def calc_url(self, url, kw, params, start, end):
        """
            拼贴吧每页url
        :param kw:
        :param params:
        :param start:
        :param end:
        :return:
        """
        for n in range(start, end + 1):
            pn = (n - 1) * 50
            full_url = url + "&pn=" + str(pn)
            content = self.download_index(full_url, params)
            self.save_tb_urls(content, n, kw)

    def main(self):
        url = "https://tieba.baidu.com/f?ie=utf-8"
        kw = input("请输入您要爬取贴吧的名称：")
        params = {"kw": kw}
        start = int(input("请输入您要爬取起始页（从1开始）:"))
        end = int(input("请输入爬取的截止页："))
        self.calc_url(url, kw, params, start, end)


if __name__ == '__main__':
    NeiHan().start()
    TieBa().main()

