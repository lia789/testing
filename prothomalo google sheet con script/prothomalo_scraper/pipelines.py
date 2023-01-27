import sqlite3
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem




class ProthomaloScraperPipeline:

    def __init__(self) -> None:
        self.con = sqlite3.connect("prothomalo.db")
        self.cur = self.con.cursor()


    def process_item(self, item, spider):
        if not item["headline"]:
            raise DropItem("Missing headline")
        if not item["headline_url"]:
            raise DropItem("Missing headline_url")


        self.cur.execute("""
            SELECT * FROM news WHERE headline_url = ?
        """,
        (
            item["headline_url"],
        ))

        if self.cur.fetchone():
            self.cur.execute("""
                UPDATE news SET headline = ? WHERE headline_url = ?
            """,
            (
                item["headline"],
                item["headline_url"],
            ))
        else:
            self.cur.execute("""
                INSERT INTO news (headline, headline_url, status) VALUES (?, ?, ?)
            """,
            (
                item["headline"],
                item["headline_url"],
                True
            ))

        self.con.commit()
        return item








