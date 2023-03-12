import scrapy


class GoodReaderProjectItem(scrapy.Item):
    quotes_text = scrapy.Field()
    author_name = scrapy.Field()
    number_of_likes = scrapy.Field()
