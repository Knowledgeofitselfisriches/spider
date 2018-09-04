# _*_ coding:utf-8 _*_
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 目标：得到直播主题和观看人数，并且统计直播人数（直播主题），统计有多少页
# 使用到的技术selenium+无界面的浏览器 ，解析数据bs4

# 统计有多少主播
nums = 0
# 统计有多少页
page_nums = 1

# 创建浏览器
driver = webdriver.Chrome()
url = "https://www.douyu.com/directory/all"
# 请求url
driver.get(url)

try:

    while True:

        # 得到页面(第1页)的数据
        content = driver.page_source

        print(content)

        # 解析数据
        soup = BeautifulSoup(content, "lxml")

        # 直播主题
        titles = soup.select('#live-list-contentbox li .play-list-link .mes .mes-tit h3')
        # 观看人数
        numbers = soup.select('#live-list-contentbox li .play-list-link .mes p .dy-num')

        for title, number in zip(titles, numbers):
            title = title.text.strip()
            number = number.text.strip()
            print("直播主题==", title, "观看人数==", number)
            # 统计直播人数
            nums += 1

        # 切换到下一页，如果没有下一页，就退出循环，
        if content.find("shark-pager-disable-next") >= 0:
            # 没有下一页了
            break
        else:
            try:
                time.sleep(0.2)
                # 如果有下一页就点击切换按钮
                driver.find_element_by_class_name("shark-pager-next").click()
                page_nums += 1
            except Exception as e:
                print("出错了==", e)

    print("当前页数===============", page_nums, "当前主播人数======", nums)
    print(len(titles))
    print(len(numbers))
except Exception as  e:
    print(e)
finally:
    driver.quit()
