# _*_ coding:utf-8 _*_

from selenium import webdriver
import time

driver = webdriver.Chrome()
# 如果没有在环境变量指定PhantomJS位置
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择
driver.get("https://www.baidu.com/")
# 打印页面标题 "百度一下，你就知道
print(driver.title)
# 生成当前页面快照并保存
driver.save_screenshot("baidu.png")

#往输id为kw入框输入女优
driver.find_element_by_id("kw").send_keys("女优")
#找到百度一些按钮，点击
driver.find_element_by_id("su").click()

time.sleep(2)

# # #保存图片
driver.save_screenshot("女优.png")

# 关闭浏览器
driver.quit()
