# -*- coding: utf-8 -*-
import scrapy
from ..items import QuotesbotItem


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]


    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):

            title = quote.xpath('./span[@class="text"]/text()').extract_first()
            author = quote.xpath('.//small[@class="author"]/text()').extract_first()


            item = QuotesbotItem()


            item["title"] = title
            item["author"] = author

            yield item






        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

