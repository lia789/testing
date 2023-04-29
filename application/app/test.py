import time
import requests
import pandas as pd
import streamlit as st
from scrapyd_api import ScrapydAPI
from typing import Dict, Union



from data_extraction_module import trigger_spider, server_status
from from_validation_module import validate_and_submit


def check_spider_status(scrapyd_server: str) -> Dict[str, Union[int, str]]:
    response = requests.get(scrapyd_server)
    spider_status = response.json()
    while spider_status["running"] != 0 or spider_status["pending"] != 0:
        time.sleep(1.5)
        response = requests.get(scrapyd_server)
        spider_status = response.json()
        st.spinner("Spider running ............")
    return spider_status



def convert_df(df: pd.DataFrame) -> bytes:
    return df.to_csv().encode('utf-8')



def main():
    st.header("Welcome to Quotes application")
    scrapyd = ScrapydAPI('http://localhost:6800')
    scrapyd_server = "http://localhost:6800/daemonstatus.json"
    project_name = "quotes"
    spider_name = "spider"

    # check if spider is already running
    spider_status = check_spider_status(scrapyd_server)

    if spider_status["running"] == 0 and spider_status["pending"] == 0:
        st.success("Spider finished running!")
        df = pd.read_csv("DATA.csv")
        st.write(df.head())

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='data.csv',
            mime='text/csv',
        )
    else:
        # URL input form
        url_input_label="Enter quotes URL"
        submit_button_label="Submit"
        submit_function=trigger_spider

        validate_and_submit(
            url_input_label=url_input_label,
            submit_button_label=submit_button_label,
            submit_function=submit_function
        )

        # check spider status again after it has finished running
        spider_status = check_spider_status(scrapyd_server)

        if spider_status["running"] == 0 and spider_status["pending"] == 0:
            st.success("Spider finished running!")
            df = pd.read_csv("DATA.csv")
            st.write(df.head())

            csv = convert_df(df)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='data.csv',
                mime='text/csv',
            )

if __name__ == "__main__":
    main()
