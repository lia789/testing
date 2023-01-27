import datetime
import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def current_date(value):
    current_date = datetime.datetime.now()
    publish_date = current_date.strftime("%d-%m-%Y")
    return publish_date

class ProthomaloScraperItem(scrapy.Item):
    headline = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    headline_url = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    # publish_date = scrapy.Field(input_processor=MapCompose(remove_tags, current_date), output_processor=TakeFirst())


class ProthomaloScraperItemSubHeadline(scrapy.Item):
    sub_headline = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    sub_headline_url = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    # publish_date = scrapy.Field(input_processor=MapCompose(remove_tags, current_date), output_processor=TakeFirst())

