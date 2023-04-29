import time
import requests
from scrapyd_api import ScrapydAPI


scrapyd = ScrapydAPI('http://localhost:6800')
project_name = "quotesbot"
spider_name = "toscrape-xpath"




def trigger_spider(keyword=None):
    scrapyd = ScrapydAPI('http://localhost:6800')
    project_name = "quotesbot"
    spider_name = "toscrape-xpath"
    scrapyd.schedule(project_name, spider_name)



def wait_for_spider_finish(scraper_url: str) -> None:
    """
    Wait until spider finishes running on scrapyd server
    """
    response = requests.get(scraper_url)
    spider_status = response.json()

    while spider_status["running"] != 0:
        time.sleep(2)
        response = requests.get(scraper_url)
        spider_status = response.json()





