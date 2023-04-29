import time
import requests
from scrapyd_api import ScrapydAPI


scrapyd = ScrapydAPI('http://localhost:6800')
project_name = "quotes"
spider_name = "spider"




def trigger_spider(keyword=None):
    scrapyd = ScrapydAPI('http://localhost:6800')
    project_name = "quotes"
    spider_name = "spider"
    scrapyd.schedule(project_name, spider_name)



def server_status():
    """
    Wait until spider finishes running on scrapyd server
    """
    scrapyd_server = "http://localhost:6800/daemonstatus.json"
    response = requests.get(scrapyd_server)
    spider_status = response.json()

    

    while spider_status["running"] != 0 or spider_status["pending"] != 0:
        time.sleep(1.5)
        response = requests.get(scrapyd_server)
        spider_status = response.json()
        print("Spider running ............")
    
    return True









