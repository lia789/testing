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



def spider_running_status() -> None:
    """
    Wait until spider finishes running on scrapyd server
    """
    time.sleep(2)
    URL = "http://localhost:6800/daemonstatus.json"
    response = requests.get(URL)
    spider_status = response.json()

    while spider_status["running"] != 0:
        time.sleep(1.5)
        response = requests.get(URL)
        spider_status = response.json()
    
    return True









