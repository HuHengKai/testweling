# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from demoCrawl.items import DemocrawlItem

class BaiduSpider(CrawlSpider):
    name = 'baidu2'
    allowed_domains = ['5i5j.com']
    #测试首页，n1,n2
    start_urls = ['https://nj.5i5j.com/zufang/']
    #测试详情页来源https://nj.5i5j.com/zufang/n2/
    start_urls=['https://nj.5i5j.com/zufang/n2/']
    rules = (
        #https://nj.5i5j.com/zufang/n2/
        # Rule(LinkExtractor(allow=r'/zufang/n\d+/'),callback=False, follow=True),
        # 测试详情页来源https://nj.5i5j.com/zufang/43988454.html
        Rule(LinkExtractor(allow=r'/zufang/\d+.html'), callback=True, follow=False),
    )

    def parse_item(self, response):
        print("*"*50)
        print(response.url)
        # print("success")
        # print(response.url)
        # item=DemocrawlItem()
        # pass
        # url=response.url
        # jianjie=response.xpath('//div[@class="h-d-content"]/p[1]/span[2]/text()').get().strip()
        # print(jianjie)
        # jianjie_url=response.xpath('//div[@class="h-d-content"]/p[1]/a/@href').get()
        # localtion=response.xpath('//div[@class="h-d-content"]/p[2]/span[2]/text()').get().strip()
        # localtion_url=response.xpath('//div[@class="h-d-content"]/p[2]/a/@href').get()
        # tel=response.xpath('//div[@class="h-d-content"]/p[4]/span[2]/text()').get()
        # doctors = response.xpath('//span[@class="m-h-title-grey"]/text()').get()[1:-1]
        # item['url']=url
        # item['jianjie']=jianjie
        # item['jianjie_url'] =jianjie_url
        # item['localtion'] =localtion
        # item['localtion_url'] =localtion_url
        # item['tel'] =tel
        # item['doctors'] =doctors
        # print(item)
        # yield item

        # print("*"*50)
        # print(response.url)
        # pass
        # print("*" * 50)
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
