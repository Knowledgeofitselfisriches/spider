# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common import keys
import time

from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)
url = 'https://www.pixiv.net/member_illust.php?id=480448&type=all&p=2'
driver.get(url)
print(driver.page_source)
print('acess')
a_list = driver.find_elements_by_class_name('work  _work ')[0].get_attribute().text
print(len(a_list))
# driver.find_element(By.CLASS_NAME, 'work  _work ')
driver.quit()