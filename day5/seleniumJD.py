# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common import keys
import time
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(chrome_options=options)
url = 'https://www.baidu.com/'
driver.get(url)

driver.find_element_by
# gl_list = driver.find_elements_by_class_name('gl-item')
# print(len(gl_list))
driver.quit()

