# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuSpiderItem(scrapy.Item):
    # # 标题
    # title = scrapy.Field()
    # # 作者头像
    # avatar = scrapy.Field()
    # # 作者ID
    # author = scrapy.Field()
    # # 发布时间
    # pub_time = scrapy.Field()
    # # 文章地址
    # origin_url = scrapy.Field()
    # # 文章id
    # article_id = scrapy.Field()
    # # 文章内容
    # content = scrapy.Field()
    # # 文章字数
    # word_count = scrapy.Field()
    # # 浏览量
    # view_count = scrapy.Field()
    # # 评论数
    # comment_count = scrapy.Field()
    # # 喜欢数
    # like_count = scrapy.Field()
    # # 文章标签
    # subjects = scrapy.Field()
    # ******************************************
    title = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
    like_num = scrapy.Field()
    read_num = scrapy.Field()