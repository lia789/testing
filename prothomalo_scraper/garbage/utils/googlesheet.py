"""
This script file contain GoogleSheet class.
GoogleSheet class responsibility:
        - authenticate with google sheet
        - reading google sheet data to pandas df
        - writing google sheet

we used two google sheet library:
    - gspread reading google sheet data
    - pygsheets for writing google sheet data
"""
import time

import gspread
import pandas as pd
import pygsheets


class GoogleSheet:
    """
    Google Sheet class responsibility:
            - authenticate with google sheet
            - reading worksheet as df
            - writing worksheet from csv file
    """


    def __init__(self, credentials, work_book) -> None:
        """
        it take credentials json file and google sheet work book to authenticate google sheet,
        this parameter will used both reading and writing google sheet module
        Parameters
        ----------
        credentials : json
            google sheet service account json file
        work_book : str
            authorize google workbook
        """

        self.credentials = credentials
        self.work_book = work_book



    def _authentication(self, action_type):
        """
        this method will authentication Google sheet and return workbook for future read and write
        Parameters
        ----------
        action_type : read|write
            if read it will use 'gspread'
            if write it will use 'pygsheets'
        Returns
        -------
        google sheet workbook
        """

        if action_type == "read":
            gspread_client = gspread.service_account(self.credentials)
            work_book = gspread_client.open(self.work_book)
            return work_book
        if action_type == "write":
            pygsheets_client = pygsheets.authorize(
                service_file=self.credentials)
            work_book = pygsheets_client.open(self.work_book)
            return work_book


    def reading_worksheet(self, work_sheet, clear=False):
        """
        this method read a work sheet and return pandas df, and also raw worksheet for if clear is True
        it first authenticate with '_authentication' method then read worksheet
        Parameters
        ----------
        work_sheet : str
            authentication worksheet name from google sheet workbook
        Returns
        -------
        pandas df
        """

        # Workbook _authentication method
        work_book = self._authentication(action_type='read')
        worksheet = work_book.worksheet(work_sheet)

        if clear is True:
            return worksheet

        df = pd.DataFrame(worksheet.get_all_records())
        return df


    def writing_worksheet(self, work_sheet, csv_file):
        """
        this method write google worksheet with processed csv file,
        it clear full worksheet help of gspread. And upload on google worksheet
        Parameters
        ----------
        work_sheet : str
            name of google worksheet which data frame update 
        csv_file : csv file
            name of process  CSV file for upload
        """
        time.sleep(5)
        # TODO: Need to change this static path to relative path
        # file = f'/home/lia/Desktop/news scraper/prothomalo_scraper/{csv_file}'
        df = pd.read_csv(csv_file)   # Formate csv file

        gspread_worksheet = self.reading_worksheet(work_sheet=work_sheet, clear=True)
        gspread_worksheet.clear()

        work_book = self._authentication(action_type="write")
        worksheet = work_book.worksheet_by_title(work_sheet)
        worksheet.set_dataframe(df, (1, 1), copy_head=True)

        print("Upload Data on google sheet")



if __name__ == '__main__':
    CREDENTIALS = "prothomalo-credentials.json"
    WORK_BOOK = "prothomalo_news_scraping_tools"

    app = GoogleSheet(credentials=CREDENTIALS, work_book=WORK_BOOK)

    # # reading google sheet
    # df_headline = app.reading_worksheet(work_sheet="today-headlines")
    # df_sub_headline = app.reading_worksheet(work_sheet="today-sub-headlines")
    # df_headline.to_csv("df_headline.csv", index=False)
    # df_sub_headline.to_csv("df_sub_headline.csv", index=False)

    # writing work sheet
    app.writing_worksheet(
        work_sheet="today-headlines",
        csv_file="headline.csv",
        )
