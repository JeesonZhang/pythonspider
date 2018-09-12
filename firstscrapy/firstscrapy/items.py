# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    img = scrapy.Field()
    name = scrapy.Field()
    intro = scrapy.Field()
    score = scrapy.Field()
    fans_num = scrapy.Field()
    quote = scrapy.Field()
