import time
import requests

import streamlit as st
import pandas as pd
from scrapyd_api import ScrapydAPI

from from_validation_module import validate_and_submit


SCRAPYD = ScrapydAPI('http://localhost:6800')
SCRAPYD_SERVER = "http://localhost:6800/daemonstatus.json"
SCRAPY_PROJECT_NAME = "quotes"
SPIDER_NAME = "spider"



def trigger_spider(keyword=None):
    SCRAPYD.schedule(SCRAPY_PROJECT_NAME, SPIDER_NAME)

def convert_df(df):
    return df.to_csv().encode('utf-8')





st.title("Welcome to Zillow property scraper")




# Scrapyd server current status
response = requests.get(SCRAPYD_SERVER)
spider_status = response.json()


# 2nd page
if spider_status["running"] != 0 or spider_status["pending"] != 0:
    spider_status_placeholder = st.empty()
    spider_status_placeholder.info("Spider is already running...")
    
    while spider_status["running"] != 0 or spider_status["pending"] != 0:
        time.sleep(1.5)
        response = requests.get(SCRAPYD_SERVER)
        spider_status = response.json()
    spider_status_placeholder.success("Spider Finish")

    df = pd.read_csv("DATA.csv") 
    st.write(df.head(n=3))

    csv = convert_df(df)

    download_button = st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='data.csv',
        mime='text/csv',

    )








# 1st page
else:
    # URL input form
    validate_and_submit(
        url_input_label="Enter property URL",
        submit_button_label="Submit",
        submit_function=trigger_spider
    )

    
    response = requests.get(SCRAPYD_SERVER)
    spider_status = response.json()

    if spider_status["running"] != 0 or spider_status["pending"] != 0:
        spider_status_placeholder = st.empty()
        spider_status_placeholder.info("Spider is running...")
        while spider_status["running"] != 0 or spider_status["pending"] != 0:
            time.sleep(1.5)
            response = requests.get(SCRAPYD_SERVER)
            spider_status = response.json()

        spider_status_placeholder.success("Spider Finish")
        df = pd.read_csv("DATA.csv", index_col=0) 
        st.write(df.head(n=3))

        csv = convert_df(df)

        download_button = st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='data.csv',
            mime='text/csv',
        )































