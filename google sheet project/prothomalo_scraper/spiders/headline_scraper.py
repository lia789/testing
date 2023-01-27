import requests
import scrapy
from parsel import Selector

from ..items import ProthomaloScraperItem




class HeadlineScraperSpider(scrapy.Spider):
    name = 'headline_scraper'
    start_urls = ['https://quotes.toscrape.com/']



    def parse(self, response):
        r = requests.get('https://www.prothomalo.com/collection/latest')
        html = r.text
        res = Selector(text=html)


        news_container = res.xpath("//div[@class='stories-set gqNK1']/div")
        for news in news_container:
            headline = news.xpath(".//h3/span/text()").get()
            headline_url = news.xpath(".//a[@class='card-with-image-zoom']/@href").get()

            item = ProthomaloScraperItem()

            item["headline"] = headline
            item["headline_url"] = headline_url

            yield item









        
