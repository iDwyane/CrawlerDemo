# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WxappItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
    article_content = scrapy.Field()
