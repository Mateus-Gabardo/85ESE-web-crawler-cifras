import scrapy

class CrawlerLyricsItem(scrapy.Item):
    title = scrapy.Field()
    lyric = scrapy.Field()
    author = scrapy.Field()
    cifra = scrapy.Field()
    link_ref = scrapy.Field()

