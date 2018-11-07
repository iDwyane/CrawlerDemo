

# 同步爬取
import requests
from lxml import etree
from urllib import  request
import os
import re

def parse_page(url):

    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    # print(response.text) # 打印html源代码
    html = etree.HTML(response.text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        # print(etree.tostring(img))
        img_url = img.get('data-original')  # 不知道为什么多个 ！data ,去掉它
        img_url = img_url.replace("!dta", "")
        # print(img_url)
        alt = img.get('alt') # 获取图片名字
        # alt 可能某些情况下需要处理非法字符（这些字符不可以当做名字保存）
        print(alt)
        suffix = os.path.splitext(img_url)[1] # 对url进行分割，取数组中的第二位，得到后缀名
        filename = alt + suffix
        print(filename)
        request.urlretrieve(img_url, 'images/' + filename) # 保存图片

def main():
    for x in range(1,101): # range(1,3) 这里相当于 1 2
        url = 'https://www.doutula.com/photo/list/?page=%d' % x
        parse_page(url)
        break

if __name__ == '__main__':
    main()