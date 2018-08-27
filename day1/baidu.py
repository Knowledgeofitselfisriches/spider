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
    with open(value.join('.html'), 'wb') as f:
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
        "https": '183.62.22.220:3128',
    }
    resp = requests.get(url, proxies)
    print(resp.content)


if __name__ == '__main__':
    # request2()
    # urllib3_request()
    # requests_org()
    # add_headers()
    # method_post()
    request_proxy()