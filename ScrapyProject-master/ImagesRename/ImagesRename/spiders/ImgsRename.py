# -*- coding: utf-8 -*-
"""
功能：本项目主要演示Scrapy下载图片重命名并放入不同目录；
运行环境：win7 64 + python3.6 + scrapy1.4 +  mongodb3.4 + pymongo-3.6.0
运行方式：进入ImagesRename目录（scrapy.cfg所在目录)输入：

scrapy crawl ImgsRename

项目详情：http://www.scrapyd.cn/example/175.html；
创建时间：2018年2月28日20:50:24；
创建者：scrapy中文网（http://www.scrapyd.cn）；
"""
import scrapy
from ImagesRename.items import ImagesrenameItem

class ImgsrenameSpider(scrapy.Spider):
    name = 'ImgsRename'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['https://www.plmm.com.cn/xinggan/4324.html'
                  ]

    def parse(self, response):
        # 实例化item
        item = ImagesrenameItem()
        # 注意imgurls是一个集合也就是多张图片item['imgurl']
        img_url=[]

        img_urls=response.xpath('//div[@id="demo-test-gallery"]/ul/a/@href').getall()
        pass
        # 抓取文章标题作为图集名称
        for url in img_urls:
            a="http:"+url[0:-7]
            img_url.append(a)
        item['imgurl']=img_url
        item['referee']=response.url
        item['imgname'] =response.xpath('//h1/text()').get()
        yield item
