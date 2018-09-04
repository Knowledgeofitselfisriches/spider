# _*_ coding:utf-8 _*_
from selenium import webdriver
import time
url = 'https://www.douban.com/'

driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_id('form_email').send_keys('283658013@qq.com')

driver.find_element_by_id('form_password').send_keys('283658013@cwq')
try:
    driver.save_screenshot('verifycode.png')
    verify_code = input('请输入验证码')

    driver.find_element_by_id('captcha_field').send_keys(verify_code)
except Exception as e:
    print('false')
    driver.quit()


driver.find_element_by_class_name('bn-submit').click()

time.sleep(2)
content = driver.page_source


driver.quit()