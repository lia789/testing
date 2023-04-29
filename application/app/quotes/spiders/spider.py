import time
import scrapy


class SpiderSpider(scrapy.Spider):
    name = "spider"

    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            }

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            time.sleep(2)
            yield scrapy.Request(response.urljoin(next_page_url))
