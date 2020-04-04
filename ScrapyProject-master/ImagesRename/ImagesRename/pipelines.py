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
import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request


class ImagesrenamePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        headers = {
            "Referer": item['referee'],
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['imgurl']:
            print("开始获取img_url")
            print(image_url)
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield Request(image_url,meta={'name':item['imgname']},headers=headers)
    #
    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):

        # 提取url前面名称作为图片名。
        print("*"*100)
        print(request.url)
        image_guid = request.url[26:34]
        # 接收上面meta传递过来的图片名称
        name = request.meta['name']
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        name = re.sub(r'[？\\*|“<>:/]', '', name)
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}/{1}'.format(name, image_guid)
        return filename
