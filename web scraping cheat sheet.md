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



