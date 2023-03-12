import re
from itemadapter import ItemAdapter





class GoodReaderProjectPipeline:
    def process_item(self, item, spider):
        return item


class DataCleanerPipeline(GoodReaderProjectPipeline):
    def process_item(self, item, spider):
        item["quotes_text"] = item["quotes_text"][1:-1]
        item["number_of_likes"] = int(re.findall(r"\d+", item["number_of_likes"])[0]) if item.get("number_of_likes") else 0
        item["author_name"] = item["author_name"][:-1]
        return item
