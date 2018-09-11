# _*_ coding:utf-8 _*_
from selenium import webdriver
import requests
import re

options = webdriver.ChromeOptions()
options.headless = True


driver = webdriver.Chrome(chrome_options=options)
def get_index(url):
    driver.get(url)
    index = driver.page_source
    print(index)
    return index

def main():
    id = 480448
    url = 'https://www.pixiv.net/member.php?id={}'
    get_index(url.format(id))

if __name__ == '__main__':
    main()