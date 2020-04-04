# -*- coding: utf-8 -*-
import scrapy


class ZhSpider(scrapy.Spider):
    name = 'zh'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_user = 'wai-wai-57-71'
    print("*"*50)
    def parse(self, response):
        print("*" * 100)
        print(response.url)
