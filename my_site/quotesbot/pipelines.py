from app.models import QuotesText




class QuotesbotPipeline(object):
    def process_item(self, item, spider):
        data = QuotesText(author=item.get("author"), title=item.get("title"))
        data.save()
        return item




class DataCleanerPipeline(QuotesbotPipeline):
    def process_item(self, item, spider):
        item["title"] = item["title"][1:-1]
        item["author"] = item["author"]
        
        return item