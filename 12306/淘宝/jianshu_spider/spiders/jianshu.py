# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import JianshuSpiderItem
import json


class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']
    # url="https://www.jianshu.com/p/1e31b903af08"
    rules = (
        Rule(LinkExtractor(allow=r'.*p/[0-9a-z]{12}.*'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item=JianshuSpiderItem()
        item['title'] = response.xpath('//h1[contains(@class,"_1RuRku")]/text()').get()
        print(item['title'])
        num = response.xpath('//div[contains(@class,"s-dsoj")]/span/text()').getall()
        item['read_num'] = num[1].split()[1]
        item['like_num'] = response.xpath('//span[@class="_3tCVn5"]/span/text()').get()
        item['pub_time'] = response.xpath('//div[contains(@class,"s-dsoj")]/time/text()').get()
        item['author'] = response.xpath('//span[@class="_22gUMi"]/text()').get()
        contents = response.xpath('//article[contains(@class,"_2rhmJa")]/p/text()').getall()
        item['content'] = ''.join(contents)
        yield item
        pass
        # title = response.xpath("//h1[@class='_1RuRku']/text()").get()
        # #头像获取不到
        # # avatar = response.xpath("//div[@class='_2mYfmT']/a/img/@src").get()
        # author = response.xpath("//span[@class='FxYr8x']/a/text()").get()
        # # pub_time = response.xpath("//div[@class='_3U4Smb']//span[@class='FxYr8x']//text()").get().strip("*")
        # # origin_url = response.url
        # pass
        # # article_id = origin_url.split("?")[0].split("/")[-1]
        # # content = response.xpath("//div[@class='show-content-free']").get()
        # # json_str = response.xpath("//script[@type='application/json']/text()").get()
        # # article_data = json.loads(json_str)
        # # word_count = article_data['note']['public_wordage']
        # # view_count = article_data['note']['views_count']
        # # comment_count = article_data['note']['comments_count']
        # # like_count = article_data['note']['likes_count']
        # # subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div//text()").getall())
        # # print(response.url)
        # # item = {}
        # # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # # #item['name'] = response.xpath('//div[@id="name"]').get()
        # # #item['description'] = response.xpath('//div[@id="description"]').get()
        # # item = JianshuSpiderItem(
        # #     title=title,
        # #     avatar=avatar,
        # #     pub_time=pub_time,
        # #     origin_url=origin_url,
        # #     article_id=article_id,
        # #     author=author,
        # #     content=content,
        # #     word_count=word_count,
        # #     view_count=view_count,
        # #     comment_count=comment_count,
        # #     like_count=like_count,
        # #     subjects=subjects
        # # )
        # yield item
