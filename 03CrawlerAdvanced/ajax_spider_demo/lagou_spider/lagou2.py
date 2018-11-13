

from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import Select,WebDriverWait

class LagouSpider(object):
    positions = [] # 用于存储
    driver_path = r'/Users/Dwyane/Documents/pycharm/chromedriver'  # 加 r 表示原生字符串
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=LagouSpider.driver_path)
        self.url= 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            self.parse_list_page(source) # 读取每一页的html源码，并得出详情页的 url

            # try catch : 如果报错，则立即打印 source 源码
            try:
                # 获取下一页的按钮
                nextBtn = self.driver.find_element_by_xpath("//div[@class='pager_container']//span[@action='next']")

                # 最后一页不给点击
                if 'pager_next pager_next_disabled' in nextBtn.get_attribute('class'):
                    break
                else:
                    nextBtn.click()
            except:
                print(source)

            time.sleep(1)

    # 读取每一页的html源码，并得出详情页的 url
    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//div[@class='position']//@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)
        print(self.positions) # 打印所有的数据

    # 请求详情页
    def request_detail_page(self,url):
        self.driver.get(url)
        source = self.driver.page_source
        self.parse_detail_page(source)

    # 解析详情页，利用 xpath
    def parse_detail_page(self,source):
        html = etree.HTML(source)
        position_name = html.xpath("//span[@class='name']/text()")[0]
        # print(position_name)

        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_spans[0].xpath('.//text()')[0].strip()  # .strip() 去掉空格
        # print(salary)

        city = job_request_spans[1].xpath(".//text()")[0].strip()
        # 把 / 和 空格符去掉
        city = re.sub(r"[\s/]", "", city)  # \s匹配的是空白字符
        # print(city)

        work_years = job_request_spans[2].xpath(".//text()")[0].strip()
        work_years = re.sub(r"[\s/]", "", work_years)  # \s匹配的是空白字符
        # print(work_years)

        education = job_request_spans[3].xpath(".//text()")[0].strip()
        education = re.sub(r"[\s/]", "", education)
        # print(education)

        # 存储数据
        position = {
            'name':position_name,
            'salary':salary,
            'city':city,
            'work_years':work_years,
            'education':education
        }
        self.positions.append(position)
        print(position)



if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()


# 如果没有下一页，也就是处在最后一页