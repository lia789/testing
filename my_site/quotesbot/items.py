import scrapy
from scrapy_djangoitem import DjangoItem
from app.models import QuotesText



# class QuotesbotItem(scrapy.Item):
#     title = scrapy.Field()
#     author = scrapy.Field()



class QuotesbotItem(DjangoItem):
    django_model = QuotesText

