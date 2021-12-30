import re
from abc import ABC

from scrapy import Request
from scrapy.exceptions import CloseSpider
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor

from .items import Article
# from twisted.internet import asyncioreactor
#
# asyncioreactor.install(asyncio.get_event_loop())
host_url = 'https://radiomap.eu'


class MetadataSpider(CrawlSpider, ABC):
    def __init__(self, radio_title):
        self.item = Article()
        self.radio_title = radio_title
        self.completed = False
        super(MetadataSpider, self).__init__()

    name = 'metadata'
    allowed_domains = ["radiomap.eu"]
    start_urls = ["https://radiomap.eu/list/"]

    rules = [Rule(LinkExtractor(restrict_css='#rightcontent > a',),
                  callback='parse_item', follow=True, errback='errback_httpbin')]

    def errback_httpbin(self, failure):
        print(self.logger.error(repr(failure)))

    def parse_item(self, response):
        if not self.completed:
            for i in response.css('.fsta *'):
                query_string = i.css('a::text').extract()[1].lower().strip()
                lnk = host_url + i.css('a').attrib['href'][2:]
                if self.radio_title in query_string:
                    self.item['title'] = query_string
                    query_string_2 = i.css('img').attrib['src']
                    query_string_2 = re.sub(r'\.+[^\w\/\_]', '', query_string_2
                    self.item['logo'] = MetadataSpider.allowed_domains[0] + query_string_2
                    return Request(lnk, callback=self.parse_stream_url)
                if self.completed == True:
                    raise CloseSpider(reason='cancelled')
        else:
            raise CloseSpider(reason='cancelled')

    def parse_stream_url(self, response, *args, **kwargs):
        self.item['url'] = response.css('audio').attrib['src']
        self.completed = True
        print(self.item)
        return self.item
