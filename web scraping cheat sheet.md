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


