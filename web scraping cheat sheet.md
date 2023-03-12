# **Scrapy**


**Scrapy Plugin List**

[`scrapy-playwright`](https://github.com/scrapy-plugins/scrapy-playwright) [`scrapy-splash`](https://github.com/scrapy-plugins/scrapy-splash) [`scrapy-selenium`](https://github.com/clemfromspace/scrapy-selenium)

[`scrapy-zyte-smartproxy`](https://github.com/scrapy-plugins/scrapy-zyte-smartproxy) [`scrapy-rotating-proxies`](https://github.com/TeamHG-Memex/scrapy-rotating-proxies)


[`scrapy-deltafetch`](https://github.com/scrapy-plugins/scrapy-deltafetch) [`scrapy-statsd-extension`](https://github.com/scrapy-plugins/scrapy-statsd)


[`scrapy-redis`](https://github.com/rolando/scrapy-redis) [`scrapy-mongodb`](https://github.com/sebdah/scrapy-mongodb) [`scrapy-pagestorage`](https://github.com/scrapy-plugins/scrapy-pagestorage) [`scrapy-feedexporter-azure-storage`](https://github.com/scrapy-plugins/scrapy-feedexporter-azure-storage) [`scrapy-dropbox`](https://github.com/scrapy-plugins/scrapy-feedexporter-dropbox)

[`scrapy-djangoitem`](https://github.com/scrapy-plugins/scrapy-djangoitem) [`Scrapyd`](https://scrapyd.readthedocs.io/en/stable/) [`Scrapyd-client`](https://github.com/scrapy/scrapyd-client) [`python-scrapyd-api`](https://github.com/djm/python-scrapyd-api) [`scrapy-do`](https://github.com/ljanyst/scrapy-do)


<br>
<br>


**Scrapy Project Building**

```cmd
Scrapy project building steps order:
    - Scrapy Project
    - Spider
    - Work with setting.py file
    - Define models
    - Write spider code, as need integrate Playwright automation code
    - Write data cleaning code
    - Write next page pagination code
    - Integrate prox solutions code
    - Integrate data base code
```


<br>
<br>


**Scrapy Command Line Code**

```cmd
$ scrapy startproject project_name
$ scrapy genspider spider_name domain_name
$ scrapy crawl spider_name -O file_name.csv
$ scrapy fetch url
$ scrapy view url
$ scrapy crawl spider_name -a keyword=keyword
$ scrapy runspider my_spider.py -o file_name.csv #Running scrapy spider as python file without process
$ scrapy runspider spider_script.py -o - #Print output data into console
```

<br>
<br>

**Scrapy Request Pattern**

```python
start_urls = [
    "https://quotes.toscrape.com/page/1/",
    "https://quotes.toscrape.com/page/2/",
    ]


def start_requests(self):
    yield scrapy.Request(url="http://example.com/page1")


# Start request with custom settings and meta
def start_requests(self):
    custom_settings = {
        "DOWNLOAD_DELAY": 4,
        }
    yield scrapy.Request(url="http://example.com/page1", meta={"key":"value"})

def parse(self, response):
    data = response.meta["key"] # Accessing meta data



# Next page pagination
next_page = response.xpath()
if next_page is not None:
    page_url = f"https://quotes.toscrape.com/{next_page}"
    yield scrapy.Request(page_url, callback=self.parse)



# Scrapy response.follow
yield response.follow(next_page, callback=self.parse)

```

<br>
<br>


**Scrapy Settings**

```python
# Settings per-spider
class MySpider(scrapy.Spider):
    name = "my_spider"
    custom_settings = {"DOWNLOAD_DELAY": 5, }


# Settings per-request
yield scrapy.Request(url, callback=self.parse, meta={'download_delay': 10})


# Access settings in spider
def parse(self, response):
    print(f"Existing settings: {self.settings.attributes.keys()}")


# Most common Scrapy settings
CONCURRENT_ITEMS = 100
DOWNLOAD_TIMEOUT = 180
DOWNLOAD_MAXSIZE = 1073741824

DUPEFILTER_DEBUG = False  # True will make all duplicate requests log

JOBDIR = ""

CLOSESPIDER_ITEMCOUNT = 0
CLOSESPIDER_PAGECOUNT = 0
CLOSESPIDER_ERRORCOUNT = 0

RETRY_ENABLED = True
RETRY_TIMES = 2

```


<br>
<br>



**Scrapy Logs**

```python
$ scrapy crawl spider_name --nolog


# Scrapy logs settings
LOG_ENABLED = True
LOG_FILE = "logs.log"
LOG_FILE_APPEND = False # Overwrite existing log file
LOG_FORMAT = "%(asctime)s %(levelname)s: %(message)s"
LOG_LEVEL = "INFO"



# Writing custom logs
import logging
class MySpider(scrapy.Spider):
    def parse(self, response):
        logging.warning("This is a warning message")
        logging.info("This is an info message")
        logging.debug("This is a debug message")

```


<br>
<br>

**Scrapy Items and Data Cleaning**


```cmd
Scrapy data extraction steps:
        1. Define Items on items.py
        2. Write spider code based on items
        3. Write data cleaning code on pipeline file
        4. Sync item pipeline on Scrapy settings
```


```python

# Extract data as Yield Dictionary
def parse(self, response):
for quote in response.xpath('//div[@class="quote"]'):
    yield {
        'text': quote.xpath('./span[@class="text"]/text()').get(),
        'author': quote.xpath('.//small[@class="author"]/text()').get(),
    }


# items.py
import scrapy
class MyItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()


 # spider.py
import scrapy
from ..items import MyItem

def parse(self, response):
    item = MyItem()
    name = response.xpath("").get()
    age = response.xpath("normalize-space()").get()  # Normalize space
    item["name"] = name
    item["age"] = age
    yield item


# pipelines.py
import re

def holding_only_int(value): # Data cleaning function
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
        item["fixed"] = holding_only_int(item["fixed"])
        return item

# settings.py
ITEM_PIPELINES = {
    'quotes_bot.pipelines.DataCleanerPipeline': 200,
    # 'quotes_bot.pipelines.QuotesBotPipeline': 300,
}

```

<br>
<br>




**Scrapy spiders with Python program**

```python

# Running spider with Python script synchronously with Subprocess
import subprocess
subprocess.run(["scrapy", "crawl", "quotes", "-o", "quotes_all.json"])


# Running spider with Python script asynchronously
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
# main.py
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

def handle_item_scraped(item):  # Signal function
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
```

**ScrapyD Setup**

```
Steps about setup Scrapyd with Python program:
    1. Install Scrapyd and Scrapyd client
            $ pip install scrapyd
            $ pip install git+https://github.com/scrapy/scrapyd-client.git
            $ pip install scrapyd-client
            $ pip install python-scrapyd-api

    2. Configure scrapy.cfg file
            # scrapy.cfg
            [settings]
            default = project_name.settings

            [deploy]
            # url = http://localhost:6800/
            project = project_name

    3. Start scrapyd server on terminal
            $ scrapyd
    4. Deploy Scrapy project
            $ scrapyd-deploy default
    5. Check host about Scrapyd servicer status and project, should be always Scrapyd server open for running spider.
```

```python
# Scrapyd with Python program

from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')
scrapyd.schedule("scrapy_project_name", "spider_name")
project_id = scrapyd.schedule("scrapy_project_name", "spider_name")
```





<br>
<br>

# **Playwright**

**Playwright command line**

```cmd
$ pip install scrapy-playwright
$ playwright install chromium
$ playwright codegen wikipedia.org
$ pip install scrapy-playwright
```


**Base Playwright code structure**

```python

# VS-Code
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,
        slow_mo=500,
        args=["--disable-blink-features", "--disable-blink-features=AutomationControlled"],  # Bot detect flag bypass
    )  # Launching browser

    context = browser.new_context(
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        # viewport={ 'width': 1280, 'height': 1024 },
    )
    page = context.new_page()
    page.goto("http://playwright.dev")
    html = page.content()
    page.screenshot(path="screenshot.png", full_page=True)
    print(page.title())

    browser.close()


# Jupyter lab interactive mode
from playwright.async_api import async_playwright

playwright = await async_playwright().start()

browser = await playwright.chromium.launch(
    headless=False,
    slow_mo=500,
    args=["--disable-blink-features", "--disable-blink-features=AutomationControlled"],
    # timeout=0
)

context = await browser.new_context(
    user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
)

page = await context.new_page()
page.set_default_timeout(0)

await page.goto("http://playwright.dev", timeout=0)

await browser.close()
await playwright.stop()
```


**Playwright Locator**

```python
page.get_by_role("button", name="Sign in").click()
page.get_by_label("User Name").fill("John")
page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")
page.get_by_text("Welcome, John")
page.get_by_alt_text("playwright logo").click()
page.get_by_test_id("directions").click()
page.locator("css=button").click()
page.locator("xpath=//button").click()
```

**Playwright Page interaction**

```python
page.get_by_role("textbox").fill("Peter") # Text input
page.get_by_role("button").click()  # Click
page.get_by_text("Item").dblclick() # Double click
page.get_by_text("Item").click(modifiers=["Shift"]) # Shift + Click
page.get_by_label('Choose a color').select_option('blue') # Select option
page.get_by_label('I agree to the terms above').check() # Check box
```

**Playwright Wait**

```python
page.wait_for_selector()
page.wait_for_timeout(5000)
```


**Injecting Custom JavaScript Code**

```python
page.evaluate(expression, **kwargs)
page.get_by_text("example domain").wait_for()
```



# **Scrapy-Playwright**

```python
# settings.py
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"


# Basic request
def start_requests(self):
    yield scrapy.Request("https://httpbin.org/get", meta={"playwright": True})


# Default Scrapy-Playwright settings list
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {}
PLAYWRIGHT_CONTEXTS = {}
PLAYWRIGHT_MAX_CONTEXTS
PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 0
PLAYWRIGHT_PROCESS_REQUEST_HEADERS
PLAYWRIGHT_MAX_PAGES_PER_CONTEXT
PLAYWRIGHT_ABORT_REQUEST


PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": False,
    "args": ["--disable-blink-features", "--disable-blink-features=AutomationControlled"],
    # "slow_mo":500
}


PLAYWRIGHT_CONTEXTS = {
    # Context one
    "custom_context_1": {
        "viewport":{'width': 200, 'height': 200},
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    },
    # Context two
    "custom_context_2": {
        "viewport":{'width': 800, 'height': 800},
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
}


# Supported meta keys in Scrapy request:
"playwright": True
"playwright_context": "context_name"
"playwright_context_kwargs": {}
"playwright_include_page": True
"playwright_page": "page_name"
"playwright_page_methods":
"playwright_page_goto_kwargs": {}
"playwright_security_details":


# Receiving page object in Scrapy parse method
def start_requests(self):
    yield scrapy.Request(
        url="",
        callback=self.parse_playwright_page,
        meta={"playwright": True, "playwright_include_page": True},
        errback=self.errback_close_page,
    )

async def parse_playwright_page(self, response):
    page = response.meta["playwright_page"]
    title = await page.title()
    await page.close() # Page must close after operation

async def errback_close_page(self, failure):
    page = failure.request.meta["playwright_page"]
    await page.close()
```






