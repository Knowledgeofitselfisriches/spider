import re
import requests
from bs4 import BeautifulSoup


def get_product_id_list():
    url = 'https://list.tmall.com/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton&smToken=7784c0cb3f664586b60eb140eddbc544&smSign=XnBIrCJRsPQoAsWokYTxGg%3D%3D'


    response = requests.get(url)

    content = response.content

    link_list = []

    id_list = []
    soup = BeautifulSoup(content, "lxml")

    tags = soup.find_all(href=re.compile(r'//detail.tmall.com/item.htm'))
    for tag in tags:
        # print(type(tag))
        print(tag["href"])
        link_list.append(tag["href"])

    # 去除重复
    link_list = list(set(link_list))

    for link in link_list:


        link = link.split("&")[0]

        id = link.replace("//detail.tmall.com/item.htm?id=", "")

        id_list.append(id)

    return id_list


print(get_product_id_list())
