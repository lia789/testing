from scrapyd_api import ScrapydAPI

scrapyd = ScrapydAPI('http://localhost:6800')
scrapyd.schedule("good_reader_project", "love")