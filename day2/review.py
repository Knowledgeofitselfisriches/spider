# _*_ coding:utf-8 _*_
import os
import random

import requests

from proxy_list import PROXIES_LIST
from user_Agent import USER_AGENT

url = 'http://www.baidu.com/s?'


def request_kw():
    value = input('关键词:')
    kw = {'wd': value}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    resp = requests.get(url, params=kw, headers=headers)
    with open(value + '.html', 'wb') as f:
        f.write(resp.content)


def proxy():
    url = 'http://www.meizitu.com/'
    proxies = {
        "http": "http://trygf521:a4c4avg9@118.89.60.145:16818/",
    }
    resp = requests.get(url, proxies=proxies)
    print('ok')


def jd():
    url = 'https://home.jd.com/'
    headers = {
        "Host": "home.jd.com",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Accept": "*/*",
        "Referer": "https://home.jd.com/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": "pinId=MmKX_0k8QLtVr4FtOTKNFg; __jdc=122270672; shshshfpa=46c98554-fd47-b653-03c4-4f7d67049263-1532015526; shshshfpb=070c500866d829b3343203786b0b74f0183bd130eacacc00d5afd99282; ipLoc-djd=1-72-2799-0; PCSYCityID=1; mt_xid=V2_52007VwMWUVhaUV4aSx9dB2IKF1NdW1RcFkwpDFBjAxdTXFpOCUobHEAAMARBTg1ZU1sDSx5bAmMBQlRdCgEIL0oYXAx7AhtOXVBDWhxCGloOYwIiUG1YYlkdTBxfBWcDFWJeUFI%3D; shshshfp=ae9fa2f6d897ac962e61ef2f3614aa17; unpl=V2_ZzNtbRcCE0Z1XUFUKx5dUWIFRgpLVhEQdQBDUnlKVQMzVkAPclRCFXwUR11nGloUZAAZWEBcRxNFCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJBBpUQ1NLEXUIRVNLKV8FVwMTbUJTQBB3C0JReR9dB2IKF1xCVEUTfA12ZHwpbDVhBxNbQFdzFEUJdhYvRV4DZQASEEJTQBB3C0JReR9dB2IKF1xCVEUTfA12VUsa; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|69805951126_0_ddab1d61a60e47ef80c419473b87edcc|1535381036864; pin=%E7%AC%A6%E5%8F%B7%E5%B8%B8%E9%87%8F; unick=%E7%AC%A6%E5%8F%B7%E5%B8%B8%E9%87%8F; _tp=rWzXdtODu1oSXbzRHnnt45DhoX0bNVHRjD8PYRu7OYP7rmlNs%2BrzmmBwrxouTVcr; _pst=%E7%AC%A6%E5%8F%B7%E5%B8%B8%E9%87%8F; user-key=39fdb291-3338-4ff6-bcab-abcd23488a1b; cn=11; __jdu=1524325437034840127784; TrackID=1I3J81HGleTIO-lfR5mokWk33Nhjaz7dnQwK0Buayufn2IdbrY48aWvLQbuA81YsMjghs9-EVkgOfHMPsoLqJNmhKNIJNkb7RtO0s0cFqSJo; ceshi3.com=000; __jda=122270672.1524325437034840127784.1524325437.1535425680.1535503036.40; thor=DFBF05E43E66FE32CD48900DCD568533AC32F9C4C75826125F6B888CF07DF25822FFDD5B7394B98333F4E65407636CF3DFDB5BD39CED6FB4D61CAB024B1F09C8A3E3FD82A74F844B1846C60CFBA61D05162AF550849DAABB8A431D3A28FF76CDADE3D9F957038556E59F420A7751E5CAB5681B9F190C92A513FC402E94DF4D36; shshshsID=afca82265c00e3fba4f3721338cb7015_1_1535503042056; __jdb=122270672.2.1524325437034840127784|40.1535503036",
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    print(response.status_code)
    with open("jd.html", "wb") as f:
        f.write(response.content)


def human():
    session = requests.session()

    url = "http://www.renren.com/PLogin.do"
    data = {
        "email": "18813228601",
        "password": "sentry@docker",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

    session.post(url, data=data, headers=headers)

    reponse = session.get("http://zhibo.renren.com/news/82")

    with open("zhibo.html", "wb") as f:
        f.write(reponse.content)


class FetchTieBa(object):
    PAGES = 3
    ITEMS = 50
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 '
                      'Safari/537.36'
    }

    def fetch_page(self,keyword):
        for i in range(FetchTieBa.PAGES):
            print(f'开始下载第{i}页', '...')
            num = i * FetchTieBa.ITEMS
            FetchTieBa.headers['User-Agent'] = random.choice(USER_AGENT)
            proxies = {'http': random.choice(PROXIES_LIST)}
            print(proxies)
            url = f'https://tieba.baidu.com/f?kw={keyword}&ie=utf-8&pn=' + str(num)
            print(url)
            response = requests.get(url, headers=FetchTieBa.headers, proxies=proxies, verify=False)

            if response.status_code == 200:
                self.download(i, response.content)
                print(f'第{i}页完成！', 'ok!')


    def start(self):
        keyword = input('请输入贴吧名字:')
        self.fetch_page(keyword)

    def download(self, name, content):
        with open(f'{name}.html', 'wb') as fw:
            fw.write(content)

    def __call__(self, *args, **kwargs):
        self.start()

def image():
    url = 'https://i.pximg.net/img-original/img/2018/08/27/20/51/55/70415155_p0.jpg'
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=70415155",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    (dirtory, file) = os.path.split(url)
    print(response.status_code)
    if response.status_code == 200:
        with open(file, 'wb') as f:
            for block in response.iter_content(4096):
                if not block:
                    break
                f.write(block)


if __name__ == '__main__':
    # request_kw()
    # human()
    # FetchTieBa()()
    image()