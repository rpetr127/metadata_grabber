from abc import ABC
import json
import re

from alphabet_detector import AlphabetDetector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MetadataSpider(CrawlSpider, ABC):
    def __init__(self):
        self.metadata_list = list()
        self.items = {
                'cyr': [],
                'lat': [] }
        super(MetadataSpider, self).__init__()

    name = 'metadata_spider'
    allowed_domains = ["radiomap.eu"]
    start_urls = ["https://radiomap.eu/list/"]

    rules = [Rule(LinkExtractor(restrict_css='#rightcontent > a',),
                  callback='parse_item', follow=False, errback='errback_httpbin')]

    def errback_httpbin(self, failure):
        print(self.logger.error(repr(failure)))

    def parse_item(self, response):
        print(response.url)
        a_dect = AlphabetDetector()
        for i in response.css('.fsta'):
            radio_station = dict()
            query_string = i.css('* a::text').extract()[1].lower().strip()
            radio_station['radio_name'] = query_string
            query_string_2 = i.css('* img').attrib['src']
            query_string_2 = re.sub(r'\.+[^\w\/\_]', '', query_string_2)
            radio_station['radio_logo'] = MetadataSpider.allowed_domains[0] + query_string_2
            if query_string in self.metadata_list:
                continue
            else:
                self.metadata_list.append(query_string)
                if a_dect.is_cyrillic(radio_station['radio_name']):
                    self.items['cyr'].append(radio_station)
                else:
                    self.items['lat'].append(radio_station) 

    def closed(self, reason):
        file = open('metadata.json', 'w')
        json.dump(self.items, file)
