# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerLyricsItem(scrapy.Item):
    title = scrapy.Field()
    lyric = scrapy.Field()
    author = scrapy.Field()
    cifra = scrapy.Field()
    link_ref = scrapy.Field()

