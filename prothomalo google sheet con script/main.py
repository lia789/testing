import sqlite3
import subprocess
import gspread




def run_spider():
    subprocess.run(["scrapy", "crawl", "headline_scraper"])

def fetch_data_from_db():
    connection = sqlite3.connect("prothomalo.db")
    cursor = connection.cursor()
    cursor.execute("SELECT headline, headline_url FROM news WHERE status = true;")
    rows = cursor.fetchall()
    data = [[row[0], row[1]] for row in rows]
    cursor.execute("UPDATE news SET status = false WHERE status = true")
    connection.commit()
    cursor.close()
    connection.close()
    return data

def append_to_google_sheet(data):
    gs = gspread.service_account("prothomalo-credentials.json")
    work_book = gs.open("prothomalo-scraper")
    worksheet = work_book.sheet1
    worksheet.append_rows(data, value_input_option='RAW')

def main():
    run_spider()
    data = fetch_data_from_db()
    append_to_google_sheet(data)

if __name__ == "__main__":
    main()
