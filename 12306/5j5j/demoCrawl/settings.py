# -*- coding: utf-8 -*-
import scrapy_fake_useragent
#控制台输出级别
# LOG_LEVEL='ERROR'
LOG_LEVEL='DEBUG'
# CRITICAL - 严重错误
#
# ERROR - 一般错误
#
# WARNING - 警告信息
#
# INFO - 一般信息
#
# DEBUG - 调试信息
# Scrapy settings for demoCrawl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'demoCrawl'

SPIDER_MODULES = ['demoCrawl.spiders']
NEWSPIDER_MODULE = 'demoCrawl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'demoCrawl (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'demoCrawl.middlewares.DemocrawlSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
'demoCrawl.middlewares.DemocrawlDownloaderMiddleware': 543,
    #使用代理ip
# 'demoCrawl.middlewares.ProxyMiddleware':300,
#添加请求代理头，大于默认得543即可
'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware':400
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'demoCrawl.pipelines.DemocrawlPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#setting里面添加代理ip，middleware中进行设置
PROXIES=[
# "http://112.113.68.188:4335",
# "http://180.119.141.29:4345",
# "http://14.106.107.109:4337",
# "http://122.195.216.22:4307",
# "http://112.195.204.106:4378"

"https://58.254.220.116:52470",
"https://58.218.214.152:2231",
"https://58.218.214.154:9193",
"https://58.218.214.147:10958",
"https://58.218.214.165:6339",
"https://58.218.214.152:9283"
]
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'haodf'         #数据库名字
MYSQL_USER = 'root'            #数据库账号
MYSQL_PASSWD = 'root'          #数据库密码
MYSQL_PORT = 3306              #数据库端口，在dbhelper中使用