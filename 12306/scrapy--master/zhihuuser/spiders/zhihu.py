# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Spider, Request
from zhihuuser.items import UserItem

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']          #定义爬虫能爬取的范围
    start_urls = ['http://www.zhihu.com/']       #开始的Url

    start_user = 'wai-wai-57-71'                 #这是我们传进去的第一个人，我们讲从他开始获取他的粉丝， 然后获取他粉丝的粉丝

    #个人信息接口
    user_info_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'     #使用.format（）方法来动态获取每个用户的信息
    #include内容单独取出来
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    #关注用户的人接口
    followees_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    followees_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    #用户关注信息接口
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        #用来获取启动各个方法,format（）函数构造完整的url
        yield Request(self.user_info_url.format(user=self.start_user, include=self.user_query), callback=self.parse_user_info)
        yield Request(self.followees_url.format(user=self.start_user, include=self.followees_query, offset=0, limit=20), callback=self.parse_followees)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=0, limit=20), callback=self.parse_followers)

    #用来获取用户个人信息的方法，并将这个人的url_token传递给用户粉丝和关注列表的函数以获取用户粉丝
    #和关注列表的函数以获得这个人的粉丝和关注列表
    def parse_user_info(self, response):
        result = json.loads(response.text)          #将获取到的Python对象转换为json对象
        item = UserItem()                           #实例化一个item用来传递信息
        #这个方法很有用可以快速取得自己要的内容（json返回），然后在使用判断进行快速赋值
        for field in item.fields:                   #item的属性fields，是一个集合，循环给item赋值
            #保证取得了我们定义好的数据而没有定义的数据不会出现
            if field in result.keys():
                #依次给item赋值
                item[field] = result.get(field)
        #返回给item
        yield item
        #将url_token传递给获取用户关注列表的函数，爬取关注列表中的关注列表，从而进行层层递归爬取个人信息
        yield Request(self.followees_url.format(user=result['url_token'], include=self.followees_query, offset=0, limit=20), callback=self.parse_followees)
        #将url_token传递给获取用户粉丝列表的函数
        yield Request(self.followers_url.format(user=result['url_token'], include=self.followers_query, offset=0, limit=20), callback=self.parse_followers)

    #作者关注的人
    def parse_followees(self, response):
        result = json.loads(response.text)
        if 'data' in result.keys():
            for user in result.get('data'):
                yield Request(self.user_info_url.format(user=user.get('url_token'), include=self.followees_query), callback=self.parse_followees)
        if 'paging' in result.keys() and result.get('paging').get('is_end') == False:
            next_url = result.get('paging').get('next')         #分页的下一页链接
            yield Request(next_url, callback=self.parse_followees)      #回调自己，作者关注的列表信息

    #当我们得到了用户的关注者后，将这些关注者再次调用这个方法，继续得到关注者，这里采用了递归的思想
    def parse_followers(self, response):
        result = json.loads(response.text)      #将Python对象转换为json对象
        #判断返回的数据中是否有data如果有就获取这个人的url，如果没有就去判断是否有下一页
        if 'data' in result.keys():
            #循环遍历data中的每个人，然后获取他的url_token传给parse_user_info函数处理
            for user in result.get('data'):
                #传递url_token给个人信息处理函数进行处理
                yield Request(self.user_info_url.format(user=user.get('url_token'), include=self.user_query), callback=self.parse_user_info)
        #判断是否有一下一页
        if 'paging' in result.keys() and result.get('paging').get('is_end') == False:
            #这里判断用户的列表有没有下一页，这个功能在每次取完本页后调用
            next_url = result.get('paging').get('next')
            yield Request(next_url,callback=self.parse_followers)
