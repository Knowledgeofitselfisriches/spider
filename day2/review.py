# _*_ coding:utf-8 _*_
import requests

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
        "https": "https://trygf521:a4c4avg9@118.89.60.145:16818/",
    }
    resp = requests.get(url, proxies=proxies)
    with open('index' + '.html', 'wb') as f:
        f.write(resp.content)


if __name__ == '__main__':
    request_kw()
    proxy()