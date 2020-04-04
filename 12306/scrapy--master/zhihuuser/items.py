# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class UserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    url_token = scrapy.Field()
    gender = scrapy.Field()
    headline = scrapy.Field()
    avatar_url = scrapy.Field()
    is_org = scrapy.Field()
    type = scrapy.Field()
    badge = scrapy.Field()
    follower_count = scrapy.Field()
    answer_count = scrapy.Field()
    articles_count = scrapy.Field()
    use_default_avatar = scrapy.Field()
    is_vip = scrapy.Field()
    url = scrapy.Field()

