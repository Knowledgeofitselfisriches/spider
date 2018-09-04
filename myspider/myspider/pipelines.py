# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json


# 注意管道文件一定要在：settings.py注册
# 管道，存储数据，例如把数据存到本地文件，或者数据库，或者对数据进行修改和添加都在这里
# class MyspiderPipeline(object):
    # 当爬虫启动的时候调用该方法

    # def __init__(self):
    #     # 创建保存数据的文件
    #     self.file = open("尚硅谷老师.json", "w", encoding="utf-8")
    #     print("爬虫启动了---------------------------------------------------")

    # def open_spider(self, spider):
    #     # 创建保存数据的文件
    #     self.file = open("尚硅谷老师.json", "w", encoding="utf-8")
    #     print("爬虫启动了---------------------------------------------------", spider)

    # 处理某一条数据的，第二参数就是一条数据，这个条数据是parse方法用yield返回回来
    # def process_item(self, item, spider):
    #     # 1.转换成字典
    #     dict_item = dict(item)
    #
    #     # 2.每行添加\n
    #     dict_str = json.dumps(dict_item, ensure_ascii=False) + "\n"
    #
    #     # 3.保存数据,只能保存字符串
    #     self.file.write(dict_str)
    #
    #     return item  # 不返回下一个管道会没有数据

    # 当爬虫结束的时候调用，释放资源关闭文件
    # spider就是AtguiguSpider
    # def close_spider(self, spider):
    #     self.file.close()
    #     print("爬结束了---------------------------------------------------", spider)
class MyspiderPipeline(object):
    def __init__(self):
        # 创建保存数据的文件
        self.file = open("wiki.json", "w", encoding="utf-8")
        print("爬虫启动了---------------------------------------------------")

    def process_item(self, item, spider):

        dict_item = dict(item)

        dict_str = json.dumps(dict_item, ensure_ascii=False) + "\n"

        self.file.write(dict_str)

        return item

    def close_spider(self, spider):
        self.file.close()
        print("爬结束了-----------]", spider)