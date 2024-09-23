from typing import Any

import scrapy
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time


class Aupropertyspider(CrawlSpider):
    name = "aupropertyspider"

    allowed_domains = ["mention domain"]
    start_urls = ["mention start url"]
    time.sleep(10)

    #define rule to follow specific link

    rules = (Rule(LinkExtractor(allow=r"street-"), callback="parse_item", follow=True),)

   #parse out put
    def parse_item(self, response):
        for gettest in response.css('.css-xqgeg2.e9vzjw56'):
            yield {
                'addr':gettest.css('div::text').getall(),
                'block':response.css('.css-u0btei.e18sdcwj3::text').get()

            }



