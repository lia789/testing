import re
# from itemadapter import ItemAdapter
# from tags_app.models import Quote

# class GoodReaderProjectPipeline:
#     def process_item(self, item, spider):
#         return item

# class DataCleanerPipeline(GoodReaderProjectPipeline):
#     def process_item(self, item, spider):
#         item["quotes_text"] = item["quotes_text"][1:-1]
#         item["number_of_likes"] = int(re.findall(r"\d+", item["number_of_likes"])[0]) if item.get("number_of_likes") else 0
#         item["author_name"] = item["author_name"][:-1]

#         Quote.objects.create(
#             author_name=item['author_name'],
#             number_of_likes=item['number_of_likes'],
#             quotes_text=item['quotes_text']
#         )

#         return item



import sqlite3
from itemadapter import ItemAdapter


class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        self.cur.execute(
            "INSERT INTO tags_app_quote (text, author, likes) VALUES (?, ?, ?)",
            (adapter['quotes_text'], adapter['author_name'], adapter['number_of_likes'])
        )
        self.conn.commit()
        return item

class DataCleanerPipeline:
    def process_item(self, item, spider):
        item["quotes_text"] = item["quotes_text"][1:-1]
        item["number_of_likes"] = int(re.findall(r"\d+", item["number_of_likes"])[0]) if item.get("number_of_likes") else 0
        item["author_name"] = item["author_name"][:-1]
        return item

