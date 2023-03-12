import scrapy
from ..items import GoodReaderProjectItem


class LoveSpider(scrapy.Spider):
    name = "love"
    start_urls = [
        # "https://www.goodreads.com/quotes/tag?utf8=%E2%9C%93&id=love",
        "https://www.goodreads.com/quotes/tag?utf8=%E2%9C%93&id=AI"
        ]



    def parse(self, response):
        quotes = response.xpath("//div[@class='leftContainer']/div[@class='quote mediumText ']")

        for quote in quotes:
            quotes_text = quote.xpath("normalize-space(.//div[@class='quoteText']/text())").get()
            author_name = quote.xpath("normalize-space(.//span[@class='authorOrTitle']/text())").get()
            number_of_likes = quote.xpath("normalize-space(//a[@class='smallText']/text())").get()
            image_url = quote.xpath(".//a[@class='leftAlignedImage']/img/@src").get()

            item = GoodReaderProjectItem()

            item["quotes_text"] = quotes_text
            item["author_name"] = author_name
            item["number_of_likes"] = number_of_likes

            yield item

        next_page = response.xpath("//a[@class='next_page']/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
