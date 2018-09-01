# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common import keys
import time

options = webdriver.FirefoxOptions()
# options.headless = True
# driver = webdriver.Firefox(firefox_options=options)
driver = webdriver.Firefox()

url = 'https://www.baidu.com/'
driver.get(url)
# print(driver.current_url)
# print(driver.page_source)
# print(driver.title)
# 生成当前页面快照并保存
# driver.save_screenshot("baidu.png")

#往输id为kw入框输入关键词
time.sleep(3)
driver.find_element_by_id("kw").send_keys("女友")
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(3)
driver.find_element_by_id("kw").send_keys(keys.Keys.CONTROL, 'a')
time.sleep(3)
driver.find_element_by_id("kw").send_keys(keys.Keys.CONTROL, 'x')
time.sleep(3)
driver.find_element_by_id("kw").send_keys('笔记本')
time.sleep(3)
driver.find_element_by_id("su").click()

# driver.get_cookies()


driver.quit()






