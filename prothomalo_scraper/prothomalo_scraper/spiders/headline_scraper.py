import requests

import scrapy
from parsel import Selector
from scrapy.loader import ItemLoader
from ..items import ProthomaloScraperItem


class HeadlineScraperSpider(scrapy.Spider):
    name = 'headline_scraper'
    start_urls = ['https://quotes.toscrape.com/']


    def parse(self, response):
        r = requests.get('https://www.prothomalo.com/')
        html = r.text
        res = Selector(text=html)

        items = ItemLoader(item=ProthomaloScraperItem(), selector=res)
        items.add_xpath('headline', 'normalize-space(//h1/span/text())')
        items.add_xpath('headline_url', '//div[@class="organism1-m__lead_story__1IQBR"]/a/@href')
        # items.add_value("publish_date", "Date")
        yield items.load_item()

        
