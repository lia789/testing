import requests

import scrapy
from parsel import Selector
from scrapy.loader import ItemLoader
from ..items import ProthomaloScraperItemSubHeadline


class SubHeadlineScraperSpider(scrapy.Spider):
    name = 'sub_headline_scraper'
    start_urls = ['https://quotes.toscrape.com/']


    def parse(self, response):
        r = requests.get('https://www.prothomalo.com/collection/latest')
        html = r.text
        res = Selector(text=html)

        stories = res.xpath('//div[@class="stories-set stories2AdWithLoadMore-m__stories_set__27iKs"]/div[@class="left_image_right_news news_item leftImageRightNews-m__base__c1lVS"]')
        for tags in stories:
            items = ItemLoader(item=ProthomaloScraperItemSubHeadline(), selector=tags)
            items.add_xpath('sub_headline', 'normalize-space(.//h3/span/text())')
            items.add_xpath('sub_headline_url', './a/@href')
            # items.add_value("publish_date", "Date")
            yield items.load_item()




        
