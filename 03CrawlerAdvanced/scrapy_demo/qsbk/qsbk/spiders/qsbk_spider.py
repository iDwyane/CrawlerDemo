# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = "https://www.qiushibaike.com"
    def parse(self, response):

        contentLeft = response.xpath("//div[@id='content-left']/div") # 获得的数据是 SelectorList 类型，实际上也是继承 Selector
        # items = []
        for duanzidiv in contentLeft:
            # print(duanzidiv)
            author = duanzidiv.xpath(".//h2/text()").get().strip()
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()
            content = "".join(content).strip()
            # duanzi = {'author':author, 'content':content}
            item = QsbkItem(author=author,content=content) # 不使用字典返回，返回item
            yield item
            # items.append(item)
        # return items
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        print('网页'+next_url)
        print("="*50)
        if not next_url:
            return
        else:
            # 发送另外一个请求 callback 代表请求回来后，执行self.parse()的函数
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse)
