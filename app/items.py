# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MetadataGrabberItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    radio_title = scrapy.Field()
    radio_logo = scrapy.Field()
