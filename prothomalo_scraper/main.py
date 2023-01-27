"""
This main.py file will run every hour in Heroku, and it is our main application file
list of work will do this main.py file:
    - run headline_scraper Scrapy spider and save headline.csv file with new data
    - run sub_headline_scraper Scrapy spider sub_headline.csv file with new data
    - authenticate "prothomalo_news_scraping_tools" google workbook
    - work about data manipulation and update google sheets
list of work every google sheet need:
    - google worksheet data
    - concat and filter
    - upload data
"""


import os

from googlesheet import GoogleSheet
from processcsv import ProcessCSV


def scraper_tool(spider_name, scraping_csv_file_name, worksheet_name, client_reading_app, client_write_app, ready_to_up_filename,):
    os.system(f"scrapy crawl {spider_name} -O {scraping_csv_file_name}")
    client_reading_app.filter_duplicate(worksheet=worksheet_name, processed_csv_name=ready_to_up_filename)
    client_write_app.writing_worksheet(work_sheet=worksheet_name, csv_file=ready_to_up_filename) #!





if __name__ == "__main__":
    CREDENTIALS = "prothomalo-credentials.json"
    WORK_BOOK = "prothomalo_news_scraping_tools"

    # Headline scraper
    scraper_tool(
        spider_name="headline_scraper",
        scraping_csv_file_name="headline.csv",
        worksheet_name="today-headlines",
        client_reading_app=ProcessCSV(credentials=CREDENTIALS, work_book=WORK_BOOK, scraping_csv_file="headline.csv"),
        client_write_app=GoogleSheet(credentials=CREDENTIALS, work_book=WORK_BOOK),

        ready_to_up_filename="headline_process_file.csv" #!
    )

    # Sub headline scraper
    scraper_tool(
        spider_name="sub_headline_scraper",
        scraping_csv_file_name="sub_headline.csv",
        worksheet_name="today-sub-headlines",
        client_reading_app=ProcessCSV(credentials=CREDENTIALS, work_book=WORK_BOOK, scraping_csv_file="sub_headline.csv"),
        client_write_app=GoogleSheet(credentials=CREDENTIALS, work_book=WORK_BOOK),
        ready_to_up_filename="sub_headline_process_file.csv" #!
    )



