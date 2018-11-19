# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# pipelines 是专门用来保存数据的，其中有三个方法经常用到


# import json
#
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json', 'w', encoding='utf-8')
#
#
# # 下面是三个常用的三个方法
#     def open_spider(self,spider):
#         print("爬虫开始了")
#
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item),ensure_ascii=False) # dumps是将dict转化成str格式，loads是将str转化成dict格式。
#         self.fp.write(item_json+'\n')
#         return item
#
#     def close_spider(self,spider):
#         self.fp.close()
#         print("爬虫结束了。。。")


from scrapy.exporters import JsonItemExporter  # 以json形式导出的导出器

# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json', 'wb')
#         self.exporter = JsonItemExporter(self.fp,ensure_ascii=False,
#                                          encoding='utf-8') # ensure_ascii 使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
#         self.exporter.start_exporting()
#
# # 下面是三个常用的三个方法
#     def open_spider(self,spider):
#         print("爬虫开始了")
#
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print("爬虫结束了。。。")


from scrapy.exporters import JsonLinesItemExporter  # 按行输出，节省内存，但是与上面的输出不一样

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('duanzi.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding='utf-8') # ensure_ascii 使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False

# 下面是三个常用的三个方法
    def open_spider(self,spider):
        print("爬虫开始了")


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
        print("爬虫结束了。。。")