import re
import requests
from bs4 import BeautifulSoup


# 得到产品所以的id
def get_product_id_list():
    url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC&pvid=65675957a19e481fb80a38e9b21af0bb'

    response = requests.get(url)

    content = response.content

    link_list = []
    id_list = []
    soup = BeautifulSoup(content, "lxml")
    # 找到所有包含
    tags = soup.select('.gl-i-wrap .p-img a')
    for tag in tags:
        if tag['href'].startswith('//'):
            link_list.append(tag["href"])

    # 去除重复
    link_list = list(set(link_list))
    print(link_list)

    for link in link_list:

        link = link.split(".html")[0]

        id = link.replace("//item.jd.com/", "")

        id_list.append(id)

    return id_list


print(get_product_id_list())
