from scrapyd_api import ScrapydAPI


scrapyd = ScrapydAPI('http://localhost:6800')
project_name = "quotes"
spider_name = "spider"




def trigger_spider(keyword=None):
    scrapyd = ScrapydAPI('http://localhost:6800')
    project_name = "quotes"
    spider_name = "spider"
    scrapyd.schedule(project_name, spider_name)












