

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
            print(alt)
            suffix = os.path.splitext(img_url)[1]  # 对url进行分割，取数组中的第二位，得到后缀名
            filename = alt + suffix
            print(filename)
            self.img_queue.put(img_url,filename)
            # request.urlretrieve(img_url, 'images/' + filename) # 保存图片

# 消费者
class Consumer(threading.Thread):

    # 创建构造函数， *args, **kwargs  可表示所有参数
    def __init__(self,page_queue,img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
    def run(self):


def main():
    page_queue = Queue(100)
    img_queue = Queue(500)
    for x in range(1,51): # 爬取前50页 range(1,3) 这里相当于 1 2
        url = 'https://www.doutula.com/photo/list/?page=%d' % x

        # break

if __name__ == '__main__':
    main()