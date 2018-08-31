import re
import requests
from bs4 import BeautifulSoup


# 得到产品所以的id
def get_product_id_list():
    url = 'https://list.tmall.com/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton&smToken=7784c0cb3f664586b60eb140eddbc544&smSign=XnBIrCJRsPQoAsWokYTxGg%3D%3D'
    # 存放在这里

    response = requests.get(url)
    # 得到数据,返回的bytes类型
    content = response.content
    # print(content)
    # 链接列表
    link_list = []
    # id列表
    id_list = []
    soup = BeautifulSoup(content, "lxml")
    # 找到所有包含
    tags = soup.find_all(href=re.compile(r'//detail.tmall.com/item.htm'))
    for tag in tags:
        # print(type(tag))
        print(tag["href"])
        link_list.append(tag["href"])

    # 去除重复
    link_list = list(set(link_list))

    for link in link_list:
        # //detail.tmall.com/item.htm?id=542032611813&skuId=3420169286887-
        # 要得到id对应的内容542032611813
        # 根据&去切
        link = link.split("&")[0]
        # 把不要的切掉,替换成空字符串
        id = link.replace("//detail.tmall.com/item.htm?id=", "")
        # 添加到列表里面
        id_list.append(id)

    return id_list


print(get_product_id_list())
