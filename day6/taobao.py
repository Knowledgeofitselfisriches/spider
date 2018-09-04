from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from bs4 import BeautifulSoup

SERVICE_ARGS = ['--load-images=false', '--disk-cache=false']

options = webdriver.ChromeOptions()
options.headless = False
# 不加载图片
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service_args=SERVICE_ARGS, chrome_options=options)
driver.set_window_size(width=1360, height=768)
wait = WebDriverWait(driver, 5)


def get_page_total_num():
    print("搜索-->机械工业出版社")
    driver.get("https://www.taobao.com/")
    # 加载搜索框
    input = wait.until(EC.presence_of_element_located((By.ID, "q")))

    input.send_keys("机械工业出版社")

    # 点击搜索--
    sublim = driver.find_element_by_css_selector("#J_TSearchForm > div.search-button > button")
    sublim.click()

    # 得到总页数
    total_page_num = driver.find_element_by_class_name("total").text  # 共 100 页，

    # 使用正则得到数字数据
    page_num = re.compile(r"(\d+)").search(total_page_num).group(1)

    # 调用得到产品信息的函数
    get_product_info()
    return page_num


# 解析页面得到产品信息
def get_product_info():
    # 等待id为mainsrp-itemlistdiv出现,只有此时数据才加载完成
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-itemlist .items .item")))
    # 得到数据
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "lxml")
    items = soup.select("#mainsrp-itemlist .items .item")
    for item in items:
        item_dict = {}
        print("-" * 200)

        image = item.select("img")[0].attrs["data-src"]
        if not image:

            image = item.select("img")[0].attrs["data-ks-lazyloa"]

        # 价格
        price = item.select(".price")[0].text.strip().replace("¥", "")
        # 商品名称
        shopname = item.select(".shopname")[0].text.strip()
        # 销售地
        location = item.select(".location")[0].text.strip()
        # 产品的链接
        product_link = item.select(".J_ClickStat")[0].attrs["href"]

        title = item.select(".title")[0].text.strip()

        item_dict["image"] = "https:" + image
        item_dict["price"] = price
        item_dict["shopname"] = shopname
        item_dict["price"] = price
        item_dict["product_link"] = "https:" + product_link
        item_dict["title"] = title
        item_dict["location"] = location
        # 打印信息
        print(item_dict)

def next_page(page):
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > div.form > input")))
    input.clear()
    input.send_keys(page)

    submit = driver.find_element_by_css_selector("#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit")
    submit.click()
    # 判断页面切换是否成功
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#mainsrp-pager > div > div > div > ul > li.item.active"),
                                         str(page)))

def main():
    page_total_num = get_page_total_num()
    for page in range(2, int(page_total_num)+1):
        try:
            next_page(page)
        except Exception as e:
            print(e)





if __name__ == "__main__":
    main()
    # 退出浏览器
    driver.quit()
