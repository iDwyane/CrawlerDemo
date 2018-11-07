

# 多线程爬取
import requests
from lxml import etree
from queue import Queue
from urllib import  request
import os
import re
import threading

class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    # 创建构造函数， *args, **kwargs  可表示所有参数
    def __init__(self,page_queue,img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get() # 获取 url
            self.parse_page(url)

    def parse_page(self,url):
        response = requests.get(url, headers=self.headers)
        # print(response.text) # 打印html源代码
        html = etree.HTML(response.text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            # print(etree.tostring(img))
            img_url = img.get('data-original')  # 不知道为什么多个 ！data ,去掉它
            img_url = img_url.replace("!dta", "")
            # print(img_url)
            alt = img.get('alt')  # 获取图片名字
            # alt 可能某些情况下需要处理非法字符（这些字符不可以当做名字保存）

            suffix = os.path.splitext(img_url)[1]  # 对url进行分割，取数组中的第二位，得到后缀名
            filename = alt + suffix
            # print(filename)
            self.img_queue.put(img_url) # 注意队列的存取操作： 先进先出
            self.img_queue.put(filename)

# 消费者
class Consumer(threading.Thread):

    # 创建构造函数， *args, **kwargs  可表示所有参数
    def __init__(self,page_queue,img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
        # print("img地址：%s" % self.img_queue)
        # print("page地址 %s" % self.page_queue)

    def run(self):
        while True:

            # 如果图片队列和页面队列都为空，page_queue证明没数据，就退出队列，线程也会自动退出
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url = self.img_queue.get() # 注意队列的存取操作： 先进先出
            filename=  self.img_queue.get()
            # print(img_url)
            request.urlretrieve(img_url, 'images/'+filename)
            print(filename+ "下载完成！")

def main():
    page_queue = Queue(100)
    img_queue = Queue(500)
    for x in range(1,51): # 爬取前50页 range(1,3) 这里相当于 1 2

        url = 'https://www.doutula.com/photo/list/?page=%d' % x
        # print(url)
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue,img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()