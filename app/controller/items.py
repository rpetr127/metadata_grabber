from scrapy import Item, Field

class Article(Item):
    title = Field()
    logo = Field()
    url = Field()