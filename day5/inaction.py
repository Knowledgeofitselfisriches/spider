# _*_coding: utf-8_*_
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.expected_conditions import presence_of_element_located


browser = webdriver.Chrome()
def actions():
    url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    browser.get(url)
    # 切换到目标元素所在的frame
    browser.switch_to.frame("iframeResult")
    # 确定拖拽目标的起点
    source = browser.find_element_by_id("draggable")
    # 确定拖拽目标的终点
    target = browser.find_element_by_id("droppable")
    # 形成动作链
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    # 执行
    actions.perform()
    '''
    1.先用switch_to_alert()方法切换到alert弹出框上
    2.可以用text方法获取弹出的文本 信息
    3.accept()点击确认按钮l
    
    4.dismiss()相当于点右上角x，取消弹出框
    element = driver.switch_to.active_element
    alert = driver.switch_to.alert
    driver.switch_to.default_content()
    driver.switch_to.frame('frame_name')
    driver.switch_to.frame(1)
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
    driver.switch_to.parent_frame()
    driver.switch_to.window('main')
    '''
    # t = browser.switch_to_alert()
    t = browser.switch_to.alert
    print(t.text)
    t.accept()
    time.sleep(10)
    browser.quit()

def script(browser):
    browser.get("https://www.zhihu.com/explore")
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    browser.execute_script("alert('To Button')")
    time.sleep(10)
    browser.quit()

def get_attr(driver):
    url = "https://www.zhihu.com/explore"
    browser.get(url)
    logo = browser.find_element_by_id("zh-top-link-logo")
    print(logo)
    print(logo.get_attribute("class"))
    browser.quit()

def testcondition():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    # WebDriverWait 库，负责循环等待
    from selenium.webdriver.support.ui import WebDriverWait
    # expected_conditions 类，负责条件出发
    from selenium.webdriver.support import expected_conditions as EC

    # 浏览器
    driver = webdriver.Chrome()
    # 等待时间
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.taobao.com/")
    try:
        # 页面一直循环，直到 id="q" 出现，如果10秒不出现将会报错
        element = wait.until(EC.presence_of_element_located((By.ID, "q")))
        # 输入内容
        element.send_keys("美食")
        # 停留两秒
        time.sleep(2)
    except Exception as e:
        print("出错了:", e)
    finally:
        driver.quit()


if __name__ == '__main__':
    # script(browser)
    # get_attr(browser)
    testcondition()