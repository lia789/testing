# Scrapy


**Scrapy Plugin List**

[`scrapy-playwright`](https://github.com/scrapy-plugins/scrapy-playwright) [`scrapy-splash`](https://github.com/scrapy-plugins/scrapy-splash) [`scrapy-selenium`](https://github.com/clemfromspace/scrapy-selenium)

[`scrapy-zyte-smartproxy`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) [`scrapy-rotating-proxies`](https://github.com/TeamHG-Memex/scrapy-rotating-proxies)


[`scrapy-deltafetch`](https://github.com/scrapy-plugins/scrapy-deltafetch) [`scrapy-statsd-extension`](https://github.com/scrapy-plugins/scrapy-statsd)


[`scrapy-redis`](https://github.com/rolando/scrapy-redis) [`scrapy-mongodb`](https://github.com/sebdah/scrapy-mongodb) [`scrapy-pagestorage`](https://github.com/scrapy-plugins/scrapy-pagestorage) [`scrapy-feedexporter-azure-storage`](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) [`scrapy-dropbox`](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox)

[`scrapy-djangoitem`](https://github.com/scrapy-plugins/scrapy-djangoitem) [`Scrapyd`](https://scrapyd.readthedocs.io/en/stable/) [`Scrapyd-client`](https://github.com/scrapy/scrapyd-client) [`python-scrapyd-api`](https://github.com/djm/python-scrapyd-api) [`scrapy-do`](https://github.com/ljanyst/scrapy-do)


**Scrapy Command Line Code**

    $ scrapy startproject project_name
    $ scrapy genspider spider_name domain_name
    $ scrapy crawl spider_name -o file_name.csv
    $ scrapy crawl spider_name -O file_name.csv #Overwirte existing file
    $ scrapy fetch url
    $ scrapy view url
    $ scrapy crawl spider_name -a keyword=keyword #Scrapy spider with command line argument
    $ scrapy runspider my_spider.py -o file_name.csv #Running scrapy spider as python file without process
    $ scrapy runspider spider_script.py -o - #Print output data into console
    $ scrapy crawl spider_name --nolog #Running spider without logs

**Scrapy Request Pattern**

    # Default start_urls
    start_urls = ["http://quotes.toscrape.com/",]
    start_urls = [
        "https://quotes.toscrape.com/page/1/", 
        "https://quotes.toscrape.com/page/2/",
    ]
    
    # With start_request
    def start_requests(self):
        yield scrapy.Request(url="http://example.com/page1")
    
    def start_requests(self):
	    urls = [
	        "http://example.com/page1",
	        "http://example.com/page2",
	    ]
	    for url in urls:
	        yield scrapy.Request(url=url)

    # Start request with custom settings
    def start_requests(self):
        custom_settings = { 
            "DOWNLOAD_DELAY": 4,
        }                                     
        yield scrapy.Request(url="http://example.com/page1")
     
    
    # Sending meta data with request
    def start_requests(self):
        yield scrapy.Request(
            url="http://example.com/page1",
            callback=self.parse,
            meta={"key": "value"} # Sending data with meta
        )
        
    def parse(self, response):                                                      
        data = response.meta["key"] # Access data with meta
    
    # Next page pagination
    next_page = response.xpath()
    if next_page is not None:
        page_url = f"https://quotes.toscrape.com/{next_page}"
        yield scrapy.Request(page_url, callback=self.parse)
        
        # With scrapy build in base url
        yield response.follow(next_page, callback=self.parse)



**Scrapy Settings**

    # Settings per-spider
    class MySpider(scrapy.Spider):
        name = "myspider"
        custom_settings = {"DOWNLOAD_DELAY": "some value",}
 
    # Settings per-request
    yield scrapy.Request(url, callback=self.parse, meta={'download_delay': 10})
  
    # Access settings in spider
    def parse(self, response):
        print(f"Existing settings: {self.settings.attributes.keys()}")

    # List of Scrapy common settings
    CONCURRENT_ITEMS = 100  #concurrent item to process in paralles
    DOWNLOAD_TIMEOUT = 180
    DOWNLOAD_MAXSIZE = 1073741824 #1024MB
    DUPEFILTER_DEBUG = False  # True will make all duplicate requests log
    
    JOBDIR = ""  # directory for storing the state of a crawl when pausing and resuming crawls
    
    LOG_ENABLED = True
    LOG_FILE = "spider_logs.log"
    LOG_FILE_APPEND = True # False, will overwrite logs file
    
    CLOSESPIDER_ITEMCOUNT = 0
    CLOSESPIDER_PAGECOUNT = 0
    CLOSESPIDER_ERRORCOUNT = 0
    
    HTTPCACHE_ALWAYS_STORE = False
    HTTPCACHE_ENABLED = False
    HTTPCACHE_EXPIRATION_SECS = 0
    HTTPCACHE_IGNORE_HTTP_CODES = []
    HTTPCACHE_IGNORE_SCHEMES = []
    
    RETRY_ENABLED = True
    RETRY_TIMES = 2



**Scrapy Logs**


    $ scrapy crawl spider_name --nolog
    
    #Scrapy logs settings
    LOG_ENABLED = True
    LOG_FILE = "logs.log"
    LOG_FILE_APPEND = False                                                   # Overwrite existing log file
    LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"
    LOG_LEVEL = "INFO"
    
    # Writing custom logs
    import logging
    class MySpider(scrapy.Spider):
        def parse(self, response):
            logging.warning("This is a warning message")
            logging.info("This is an info message")
            logging.debug("This is a debug message")


**Scrapy Items and Data Cleaning**


    # Extract data as Yield Dictionary
    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                'text': quote.xpath('./span[@class="text"]/text()').get(),
                'author': quote.xpath('.//small[@class="author"]/text()').get(),
            }

   	# Extract data as Scrapy Items with out item loader
	       - Steps One: Define Items on items.py
	       - Steps Two: Write spider code based on items
	       - Steps Three: Write data cleaning code on pipeline file
	       - Steps Four: Sync item pipeline on Scrapy settings
        
    #items.py
    import scrapy
    class MyItem(scrapy.Item):
        name = scrapy.Field()
        age = scrapy.Field()
        
    
    #spider.py
    import scrapy
    from ..items import MyItem
    
    def parse(self, response):
        item = MyItem()
        name = sel.xpath('//div[@class="name"]/text()').get()
        age = sel.xpath("normalize-space(//div[@class='age']/text())").get()  # With normalize space
        item['name'] = name
        item['age'] = age
        yield item
   
    #pipelines.py
    import re
    
    def holding_only_int(value):                                                               # Data cleaning function
        if value is not None:
            raw_value = re.findall(r'\d+', value)
            clean_int_value = ''.join(raw_value)
        else:
            clean_int_value = 0
        return clean_int_value
    
    
    class QuotesBotPipeline:  # Default pipeline
        def process_item(self, item, spider):
            return item
        
    
    class DataCleanerPipeline(QuotesBotPipeline):
        def process_item(self, item, spider):  # Define columns, that need data cleaning
            item["text"] = item["text"][1:-1]
            item["fixed"] = holding_only_int(item["fixed"]
            return item
       
    #settings.py
    ITEM_PIPELINES = {
        'quotes_bot.pipelines.DataCleanerPipeline': 200,
        # 'quotes_bot.pipelines.QuotesBotPipeline': 300,
    }




**Scrapy spiders with Python program**


    # Running spider with Python script synchronously with Subprocess
    import subprocess
    subprocess.run(["scrapy", "crawl", "quotes", "-o", "quotes_all.json"])
   
    # Running spider with Python script asyncronously and symonitiosly
    process_1 = subprocess.Popen(["scrapy", "crawl", "quotes", "-o", "Data.csv"])
    process_2 = subprocess.Popen(["scrapy", "crawl", "quotes", "-o", "Data_2.csv"])
    process_1.wait()
    process_2.wait()

    # Running Scrapy project spider with crawler process
    from scrapy.crawler import CrawlerProcess
    from quotes_bot.spiders.quotes import QuotesSpider
    from scrapy.utils.project import get_project_settings
    
    process = CrawlerProcess(get_project_settings())
    process.crawl(QuotesSpider)
    process.start()

    # Running Scrapy spider with a Python script
    import scrapy
    from scrapy.crawler import CrawlerProcess
    
    class QuotesSpider(scrapy.Spider):
        name = 'quotes'
        start_urls = ['http://quotes.toscrape.com/']
    
        def parse(self, response):
            pass
    
    if __name__=="__main__":
        process = CrawlerProcess(
            settings={
                "FEEDS": {"items.json": {"format": "json"},
                },
            })
        
        process.crawl(QuotesSpider)
        process.start()

    # Saving Scrapy data as pandas df from Python script
    
    #main.py
    import pandas as pd
    from scrapy import signals
    from scrapy.crawler import CrawlerProcess, Crawler
    from scrapy.utils.project import get_project_settings
    from quotes_bot.spiders.quotes import QuotesSpider
    
    # Twisted reactor installation code
    from twisted.internet import asyncioreactor
    asyncioreactor.install()
    
    items = []
    
    process = CrawlerProcess(get_project_settings())
    quote_crawler = Crawler(QuotesSpider, get_project_settings())
    
    def handle_item_scraped(item):  # Singnal function
        text =  item["text"] 
        author = item["author"]
        data = {"text": text, "author": author}
        items.append(data)
        
    quote_crawler.signals.connect(handle_item_scraped, signal=signals.item_scraped)  # Defining signal
    process.crawl(quote_crawler)
    process.start()
    
    # Save data as pandas df
    df = pd.DataFrame(items)
    df.to_csv("quotes.csv", index=False)


