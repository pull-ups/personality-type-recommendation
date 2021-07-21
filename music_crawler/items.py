# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    artist = scrapy.Field()
    lyric = scrapy.Field()
    theme = scrapy.Field()