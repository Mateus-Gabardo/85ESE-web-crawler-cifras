# Scrapy settings for crawler_lyrics project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "crawler_lyrics"

SPIDER_MODULES = ["crawler_lyrics.spiders"]
NEWSPIDER_MODULE = "crawler_lyrics.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   "crawler_lyrics.pipelines.CrawlerLyricsPipeline": 300,
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# settings.py

DATABASE = {
    'host': 'localhost',
    'user': 'admin',
    'password': '1234',
    'database': 'postgres',
    'port': '5432',
}

