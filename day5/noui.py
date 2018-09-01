# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url="http://www.baidu.com"
#浏览器配置
options = webdriver.ChromeOptions()
#配置浏览器没有界面
options.headless=True
#设置参数
driver=webdriver.Chrome(chrome_options=options)
#请求百度网站
driver.get(url)
#得到当前的页面
print(driver.current_url)
time.sleep(2)
#如果能正常保存图片就是正常
driver.save_screenshot("谷歌内置没有界面的浏览器.png")
#得到页面源代码
print(driver.page_source)

driver.quit()
