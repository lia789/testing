"""
ProcessCSV class responsibility:
    - reading scrapy feed scraping csv file to pandas df
    - reading google worksheet data to pandas df
    - concat two df
    - filter duplicate
    - save a csv file

"""

import pandas as pd
from utils.googlesheet import GoogleSheet


class ProcessCSV(GoogleSheet):
    """
    this class will do, this list of jobs:
            - reading scraping csv file to df
            - reading google worksheet csv file to df
            - concat df and filter df
            - save processed csv file
    """

    def __init__(self, credentials, work_book, scraping_csv_file) -> None:
        super().__init__(credentials, work_book)
        self.scraping_csv_file = scraping_csv_file

    def _reading_scraping_csv(self):
        """
        this method read scraping csv file with df

        Returns
        -------
        _type_: df
            scraping csv to pandas data frame
        """
        df = pd.read_csv(self.scraping_csv_file)
        return df

    def filter_duplicate(self, worksheet, processed_csv_name):
        """
        this method read existing scraping csv file and google sheet worksheet
        as pandas data frame,
        concat both df and filter duplicate.
        It return ready to upload csv file

        Returns
        --------
        csv file
        """
        scraping_data_df = self._reading_scraping_csv()
        google_worksheet_df = super().reading_worksheet(work_sheet=worksheet)
        processed_csv_df = pd.concat(
            [scraping_data_df, google_worksheet_df]).drop_duplicates()


        # Todo: Fix relative export path
        
        path = r"/home/lia/Desktop/news scraper/prothomalo_scraper/utils"
        processed_csv_df.to_csv(f"{path}/{processed_csv_name}", index=False)


if __name__ == '__main__':
    CREDENTIALS = "prothomalo-credentials.json"
    WORK_BOOK = "prothomalo_news_scraping_tools"
    WORKSHEET = "today-headlines"

    app = ProcessCSV(
        credentials="prothomalo-credentials.json",
        work_book=WORK_BOOK,
        scraping_csv_file="headline.csv",
    )
    app.filter_duplicate(worksheet=WORKSHEET, processed_csv_name="process")

    gspread_app = GoogleSheet(credentials=CREDENTIALS, work_book=WORK_BOOK)
    gspread_app.writing_worksheet(
        work_sheet=WORKSHEET,
        csv_file="process.csv",
        )
