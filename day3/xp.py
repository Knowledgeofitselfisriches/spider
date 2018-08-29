# _*_ coding:utf-8 _*_
import random

import requests
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>
'''
def test_xpath():
    html = etree.parse("./other.html")
    # etree.tostring(html)
    # html = etree.HTML(html)
    result = html.xpath('//li[last()]/a/@href')

    print(result)


class FetchTieBa(object):
    PAGES = 1
    ITEMS = 50
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 '
                      'Safari/537.36'
    }

    def fetch_page(self, keyword):
        for i in range(FetchTieBa.PAGES):
            print(f'开始下载第{i}页', '...')
            num = i * FetchTieBa.ITEMS
            url = f'https://tieba.baidu.com/f?kw={keyword}&ie=utf-8&pn=' + str(num)
            print(url)
            response = requests.get(url )

            if response.status_code == 200:
                # self.download(i, response.content)
                print(response.text)
                html = etree.HTML(response.text)
                result = html.xpath('//div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit"]/a[@title]/text()')

                print(result)


    def start(self):
        keyword = input('请输入贴吧名字:')
        self.fetch_page(keyword)

    def download(self, name, content):
        with open(f'{name}.html', 'wb') as fw:
            fw.write(content)

    def __call__(self, *args, **kwargs):
        self.start()


if __name__ == "__main__":
    test_xpath()