# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BookparserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    autor = scrapy.Field()
    oldprice = scrapy.Field()
    newprice = scrapy.Field()
    rating = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()
    pass
