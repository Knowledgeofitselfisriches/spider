# _*_ coding:utf-8 _*_
import re

import requests
import os


class Spider(object):
    def load_page(self, page):
        """
        :param page: 请求的页数
        :return: 返回网页的数据
        """
        url = "https://cuiqingcai.com/page/" + str(page)

        headers = {
            "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
            # "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Cookie": "UM_distinctid=165619fe87c5ee-03a608aae53197-9393265-100200-165619fe87e1a9;"
                      " Hm_lvt_3ef185224776ec2561c9f7066ead4f24=1534941194,1534941873;"
                      " Hm_lpvt_3ef185224776ec2561c9f7066ead4f24=1535453184",
            "Host": "qiniu.cuiqingcai.com",
            "Pragma": "no-cache",
            "Referer": "https://cuiqingcai.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/68.0.3440.106 Safari/537.36",
        }
        response = requests.get(url, headers=headers, verify=False)

        return response.text

    def filter_title(self, text):
        # <a target="_blank" href="https://cuiqingcai.com/5491.html" title=""> </a>
        pattern = re.compile(r'<a target="_blank" href="(.*?)">', re.S)
        items = pattern.findall(text)
        for item in items[0][0]:
            for i in items:
                print(i)
                # https://cuiqingcai.com/5052.html" title="Python3网络爬虫开发实战教程
                j = i.replace('" title="', '')
                print(i)


if __name__ == "__main__":
    spd = Spider()
    content = spd.load_page(1)
    spd.filter_title(content)