# _*_ coding:utf-8 _*_
import requests
import re


class NeiHan(object):
    def page(self, page=1):
        url = "https://www.neihan8.com/article/list_5_" + str(page) + ".html"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        content = response.content.decode("GBK")
        p = re.compile(r'<div class="f18 mb20">.+?</div>', re.S)
        duanzi_list = p.findall(content)
        with open("段子.txt", "a", encoding="utf-8") as f:
            for item in duanzi_list:
                item = item.replace('<div class="f18 mb20">', ''). \
                    replace("</div>", "").replace("<br />", ""). \
                    replace("<p>", "").replace("</p>", ""). \
                    replace("&ldquo;", "“").replace("&rdquo;", "”").replace("&hellip;", "...")
                print("-" * 200)
                print(item)
                f.write(item)

        return content


if __name__ == '__main__':
    start = int(input('起始页:'))
    end = int(input('结束页:'))
    # map(NeiHan().page, range(start, end))

    for i in range(start, end):
        print(i)
        NeiHan().page(i)
