# import asyncio
# import functools
# import time

import crochet
crochet.setup()

from flask import jsonify, render_template_string
# from scrapy import signals
# from scrapy.crawler import CrawlerRunner
# from scrapy.signalmanager import dispatcher

# from .spider import MetadataSpider
from app import table

output_data = list()
# crawl_runner = CrawlerRunner()
# state_scraping = 'defined'


def home():
    return render_template_string('<h1>It works!</h1>')


async def radio_metadata(title=None):
    global state_scraping
    title = title.lower().strip()
    data = list(table.search(title))[0]

    # scrape_data(title)
    # while True:
    #     state_scraping = 'scraping'
    #     time.sleep(.3)
    #     if state_scraping == 'finished':
    #         break
    return jsonify(data)


# @crochet.run_in_reactor
# def scrape_data(t):
#     global output_data
#     output_data = []
#     dispatcher.connect(_crawler_result, signal=signals.item_scraped)
#     eventual = crawl_runner.crawl(MetadataSpider, radio_title=t)
#     eventual.addCallback(_finished_scrape)


# def _crawler_result(item, response, spider):
#     # if title == item['title']:
#     #     spider.crawler.engine.close_spider(reason='finished')
#     output_data.append(dict(item))
#
#
# def _finished_scrape(null):
#     global state_scraping
#     state_scraping = 'finished'

