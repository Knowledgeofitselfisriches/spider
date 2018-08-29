# _*_ coding:utf-8 _*_
import random
import requests
import os
from user_Agent import USER_AGENT
from proxy_list import PROXIES_LIST


# 随机代理 注意代理不能返回公网/注意公网ip被封
def multi_user_agent():
    url = 'http://47.93.10.182:8000'
    user_agent = random.choice(USER_AGENT)
    proxies = {'http': random.choice(PROXIES_LIST)}
    print(proxies)
    headers = {
        'user_agent': user_agent
    }
    resp = requests.get(url, headers=headers, proxies=proxies)
    print(resp.content.decode('utf-8'))


# cookie 请求
def request_cookie():
    url = 'http://www.baidu.com'
    resp = requests.get(url)
    print(resp.cookies)
    cookies = requests.utils.dict_from_cookiejar(resp.cookies)
    print(cookies)


def request_session():
    session = requests.session()

    url = "http://www.renren.com/PLogin.do"
    # url = "http://www.renren.com/SysHome.do"
    data = {
        "email": "18813228601",
        "password": "sentry@docker",
    }

    # 模拟谷歌浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

    # post请求成功，进入主页，返回主页数据
    response = session.post(url, data=data, headers=headers)

    with open("session.html", "wb") as f:
        f.write(response.content)

    # get请求--cookie

    reponse = session.get("http://www.renren.com/881820831/profile")

    with open("郑爽.html", "wb") as f:
        f.write(reponse.content)


def request_jd():
    url = 'https://home.jd.com/'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '__jdu=1524325437034840127784; pinId=MmKX_0k8QLtVr4FtOTKNFg; __jdc=122270672; shshshfpa=46c98554-fd47-b653-03c4-4f7d67049263-1532015526; shshshfpb=070c500866d829b3343203786b0b74f0183bd130eacacc00d5afd99282; ipLoc-djd=1-72-2799-0; PCSYCityID=1; mt_xid=V2_52007VwMWUVhaUV4aSx9dB2IKF1NdW1RcFkwpDFBjAxdTXFpOCUobHEAAMARBTg1ZU1sDSx5bAmMBQlRdCgEIL0oYXAx7AhtOXVBDWhxCGloOYwIiUG1YYlkdTBxfBWcDFWJeUFI%3D; shshshfp=ae9fa2f6d897ac962e61ef2f3614aa17; unpl=V2_ZzNtbRcCE0Z1XUFUKx5dUWIFRgpLVhEQdQBDUnlKVQMzVkAPclRCFXwUR11nGloUZAAZWEBcRxNFCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJBBpUQ1NLEXUIRVNLKV8FVwMTbUJTQBB3C0JReR9dB2IKF1xCVEUTfA12ZHwpbDVhBxNbQFdzFEUJdhYvRV4DZQASEEJTQBB3C0JReR9dB2IKF1xCVEUTfA12VUsa; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|69805951126_0_ddab1d61a60e47ef80c419473b87edcc|1535381036864; pin=%E7%AC%A6%E5%8F%B7%E5%B8%B8%E9%87%8F; unick=%E7%AC%A6%E5%8F%B7%E5%B8%B8%E9%87%8F; _tp=rWzXdtODu1oSXbzRHnnt45DhoX0bNVHRjD8PYRu7OYP7rmlNs%2BrzmmBwrxouTVcr; _pst=%E7%AC%A6%E5%8F%B7%E5%B8%B8%E9%87%8F; __jda=122270672.1524325437034840127784.1524325437.1535381037.1535425680.39; user-key=39fdb291-3338-4ff6-bcab-abcd23488a1b; cn=11; TrackID=1VTcmuYQHjhegqLx0pNack9gHh2wS5EIrPTdXRs8U7m6w6SCZdbwxfztKkwINMha5gcuuutdz2yWX2GVwZRnxQuwynaPOQCUahcIp32h2N0E; thor=FCA4929382E58BB53D0D5E852B489266BB17FCF304AE2E5CA3675985E79F375B7B6B294D84F999BCB21BBF7B1B0A372009659BEDB1DFE2325DBD7BB7945CE0AC65CF995DE62A92C157CDC260D7AA5FCF1EBEB6CA5C34067587AE6D49633C40D05965DA03D6BD207B07F84DF8D2B833897EC5904033AB2D5816D8537B3BC2B965; ceshi3.com=000; shshshsID=86364b9659b79cf04960208883802dcc_3_1535426238319; __jdb=122270672.6.1524325437034840127784|39.1535425680; 3AB9D23F7A4B3C9B=BDMV2KZ56SDYS6BQ5M5V3L6WCQJX7L2M6MLNULVRIG5FSBRZM3SK3SXR5G4JYHGVTG6N2RPWBQHZE6RDIEROGJT2PY',
        'Host': 'home.jd.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    with open("jd.html", "wb") as f:
        f.write(response.content)


# 跳过ssl 认证 verify=False
def request_ignore_ca():
    url = ' https://www.12306.cn/mormhweb/'
    headers = {
        'User-Agent': random.choice(USER_AGENT)
    }
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)


def request_image():
    url = 'https://i.pximg.net/img-original/img/2018/08/27/20/51/55/70415155_p0.jpg'
    headers = {
        # "authority": "i.pximg.net",
        # "method": "GET",
        # "path": "/img-original/img/2018/08/27/20/51/55/70415155_p0.jpg",
        # "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=70415155",
        # "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    }
    response = requests.get(url, headers=headers)
    (dirtory, file) = os.path.split(url)
    print(response.status_code)
    if response.status_code == 200:
        with open(file, 'wb') as f:
            for block in response.iter_content(2048):
                if not block:
                    break
                f.write(block)


import requests


class FetchTieBa(object):
    PAGES = 3
    ITEMS = 50
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 '
                      'Safari/537.36'
    }

    def fetch_page(self, keyword):
        for i in range(FetchTieBa.PAGES):
            print(f'开始下载第{i}页', '...')
            num = i * FetchTieBa.ITEMS
            FetchTieBa.headers['User-Agent'] = random.choice(USER_AGENT)
            proxies = {'http': random.choice(PROXIES_LIST)}
            print(type(proxies))
            url = f'https://tieba.baidu.com/f?kw={keyword}&ie=utf-8&pn=' + str(num)
            response = requests.get(url, headers=FetchTieBa.headers, proxies=proxies)
            print(response.status_code)
            if response.status_code == 200:
                self.download(keyword + str(i), response.content)
                print(f'第{i}页完成！', 'ok!')

    def start(self):
        keyword = input('请输入贴吧名字:')
        self.fetch_page(keyword)

    def download(self, name, content):
        with open(f'{name}.html', 'wb') as fw:
            fw.write(content)

    def __call__(self, *args, **kwargs):
        self.start()


class Spider(object):
    #  获取文本
    def loading(self, i):
        url = f'https://tieba.baidu.com/f?kw=搞笑吧&ie=utf-8&pn=' + str(i*50)
        # 封装请求对象
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
        response = requests.get(url, headers=headers)

        return response.text

    def main(self):
        i = input('取第几页：')
        content = self.loading(i)
        print(content)


if __name__ == '__main__':
    # request_kw()
    # multi_user_agent()
    # request_cookie()
    # request_image()
    # FetchTieBa()()
    Spider().main()