# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        # 允许的url。所有满足这个正则表达式的url都会被提取  去掉callback，让它继续爬取
        # follow 是继续跟进
        Rule(LinkExtractor(allow=r".+mod=list&catid=2&page=[1-2]"), follow=True), # 前 10 页
        Rule(LinkExtractor(allow=r".+article-.+\.html"),callback="parse_detail",follow=False) # +表示1-无穷  article-4673-1.html

    )


    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()

        author_p = response.xpath("//p[@class='authors']")
        author = author_p.xpath("./a/text()").get()
        pub_time = author_p.xpath("./span[@class='time']/text()").get()
        article_content = response.xpath("//td[@id='article_content']//text()").getall() # 因为可能有很多text ,所以需要 //  ，又因为获取多个，所以用 getall()
        article_content = "".join(article_content).strip()  # 因为获取到的是list,所以需要转变成字符串，然后用 strip 去掉多余的空格
        item = WxappItem(title=title,author=author,pub_time=pub_time,article_content=article_content)
        yield item
        # print("="*30)
        # print(title)
        # print(author)
        # print(pub_time)
        # print(article_content)
        print("="*30)