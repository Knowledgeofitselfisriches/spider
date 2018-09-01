from queue import Queue
from threading import Thread, Lock
import time
import requests
import json
from lxml import etree


crawl_exit = False
parse_exit = False


# 采集数据的线程
class ThreadCrawl(Thread):
    def __init__(self, thread_name, page_queue, data_queue):
        super(ThreadCrawl, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}

    def run(self):
        while not crawl_exit:
            try:
                page = self.page_queue.get(block=False)
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                print("%s开始工作了,页数是:%d,url=%s" % (self.thread_name, page, url))
                request = requests.get(url, headers=self.headers)
                html = request.text

                # 把数据装入data_queue队列
                self.data_queue.put(html)
                time.sleep(1)
            except Exception as e:
                pass
                # break


# 解析数据的线程
class ThreadParse(Thread):
    def __init__(self, thread_name, data_queue, file_name, lock):
        super(ThreadParse, self).__init__()
        self.thread_name = thread_name
        self.file_name = file_name
        self.data_queue = data_queue
        self.lock = lock

    def run(self):
        while not parse_exit:
            try:

                html = self.data_queue.get(block=False)
                print("%s开始解析数据:%s" % (self.thread_name, html[:10]))
                self.parse(html)
            except Exception as e:
                pass
            # break

    # 解析数据
    def parse(self, html):
        content = etree.HTML(html)

        node_lists = content.xpath("//div[contains(@id, 'qiushi_tag_')]")
        print('当前页面共有', len(node_lists), '条')

        for node in node_lists:
            item = {}
            user_image = node.xpath('.//div/a/img[@class="illustration"]/@src')
            user_name = node.xpath(".//div//h2/text()")
            text = node.xpath(".//a/div/span/text()")
            zan = node.xpath(".//div/span/i/text()")
            comments = node.xpath(".//div/span/a/i/text()")
            # print(user_name,user_image,text,zan,comments)
            if len(user_image) > 0:
                item["user_image"] = user_image[0]
            if len(user_name) > 0:
                item["user_name"] = user_name[0]
            if len(text) > 0:
                item["text"] = text[0]

            if len(zan) > 0:
                item["zan"] = zan[0]
            if len(comments) > 0:
                item["comments"] = comments[0]
            print(item)

            # 添加到列表里面
            # items.append(item)
            # 获得锁,释放锁的功能,其他线程无法获得
            with self.lock:
                # 保存到qiushibaike.json中
                # item = f'{item}\n'
                # json.dump(item, self.file_name, ensure_ascii=False)
                item = json.dumps(item, ensure_ascii=False) + '\n'
                self.file_name.write(item)


# 定义入口函数
def main():
    global crawl_exit
    global parse_exit
    # 创建互斥锁
    lock = Lock()
    # 定义装页数的队列,最多爬取十个页面的数据
    page_queue = Queue(10)
    for page in range(1, 11):
        page_queue.put(page)

    # 定义装每页的数据的队列
    data_queue = Queue()

    # 创建三个采集线程用于:数据的采集(请求网络得到数据)
    # 存储三个采集线程

    thread_crawls = []
    thread_names = ["采集线程1", "采集线程2", "采集线程3"]
    for thread_name in thread_names:
        crawl = ThreadCrawl(thread_name, page_queue, data_queue)
        # 启动线程
        crawl.start()
        thread_crawls.append(crawl)
    # 存储json数据的文件
    file_name = open("糗事百科.json", "a", encoding="utf-8")
    # 创建三个解析线程用于:解析html页面的数据

    thread_parses = []
    thread_names = ["解析线程1", "解析线程2", "解析线程3"]
    for thread_name in thread_names:
        parse = ThreadParse(thread_name, data_queue, file_name, lock)
        # 启动线程
        parse.start()
        thread_parses.append(parse)

    # 采集线程------
    # 等待采集线程接收,主线程才能结束
    while not page_queue.empty():
        pass
    # 采集线程结束了,退出结束
    crawl_exit = True

    # 等待采集线程结束
    for crawl in thread_crawls:
        crawl.join()
        print("%s线程结束" % str(crawl))

    # 解析线程------
    while not data_queue.empty():
        pass

    # 解析线程结束
    parse_exit = True

    # 等待采集线程结束
    for parse in thread_parses:
        parse.join()
        print("%s线程结束" % str(parse))

    # 获得锁后,其他线程无法操作文件,关闭文件--------------
    with lock:
        file_name.close()

    print("主线程执行结束了------------")


if __name__ == "__main__":
    main()

