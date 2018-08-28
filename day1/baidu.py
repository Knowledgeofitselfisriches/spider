# _*_ coding:utf-8 _*_
url = 'http://www.baidu.com'


def request1():
    import requests
    response = requests.get('http://www.baidu.com')
    print(response)
    with open("baidu.html", "wb") as f:
        f.write(response.content)


# urllib
def request2():
    # urllib2 python2 的
    import urllib.request
    response = urllib.request.urlopen(url)

    print(response.read().decode('utf-8'))


def urllib3_request():
    import urllib3

    http = urllib3.PoolManager()
    response = http.request('GET', 'http://www.atguigu.com')
    print(response.status)
    print(response.data.decode('utf-8'))


# get 请求
def requests_org():

    import requests
    url = 'http://www.meizitu.com/'
    resp = requests.request('GET', url)
    resp = requests.get(url)

    content = resp.content

    print(content.decode('gb2312'))


# 加headers 和 关键词
def add_headers():
    import requests

    value = input('关键词:')
    kw = {'wd': value}

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/68.0.3440.106 Safari/537.36"
    }
    response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)
    with open(value+'.html', 'wb') as f:
        f.write(response.content)
    print(response.text)
    print(response.url)
    print(response.encoding)
    print(response.status_code)


import requests

# post 请求
def method_post():

    url = 'http://httpbin.org/post'
    data = {
        'name': 'xiaoba',
        'age': '18'
    }
    resp = requests.post(url, data=data)
    content = resp.content
    print(content.decode('utf-8'))


def request_ajax():
    pass


def request_proxy():
    url = 'http://www.baidu.com'

    proxies = {
        'http':'http://1.197.178.215:39087',
        "https": "https://114.223.221.128:808",
    }
    resp = requests.get(url, proxies)
    print(resp.content)


def private_proxy():
    import requests
    url = 'http://www.meizitu.com/'
    proxies = {
        "https": "https://trygf521:a4c4avg9@118.89.60.145:16818/",
    }
    resp = requests.get(url, proxies=proxies)
    print(resp.content.decode('gb2312'))


def fetch_page():
    import requests
    keyword = input('请输入贴吧名字:')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 '
                      'Safari/537.36'
    }
    PAGES = 3
    ITEMS = 50

    for i in range(PAGES):
        print(f'开始下载第{i}页', '...')
        num = i * ITEMS
        url = f'https://tieba.baidu.com/f?kw={keyword}&ie=utf-8&pn=' + str(num)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(keyword+f'{i}.html', 'wb') as fw:
                fw.write(response.content)

            print(f'第{i}页完成！', 'ok!')


if __name__ == '__main__':
    # request2()
    # urllib3_request()
    # requests_org()
    # add_headers()
    # method_post()
    # request_proxy()
    # private_proxy()
    fetch_page()