# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass

    url = scrapy.Field()
    slug = scrapy.Field()
    directories = scrapy.Field()
    title = scrapy.Field()
    h1 = scrapy.Field()
    h2 = scrapy.Field()
    h3 = scrapy.Field()
    h4 = scrapy.Field()
    description = scrapy.Field()
    img_count = scrapy.Field()
    img_links = scrapy.Field()
    img_alt_tags = scrapy.Field()
    link_count = scrapy.Field()
    link_urls = scrapy.Field()
    link_text = scrapy.Field()
    load_time = scrapy.Field()
    status_code = scrapy.Field()
