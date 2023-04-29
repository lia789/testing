import time
import requests

import streamlit as st
import pandas as pd
from scrapyd_api import ScrapydAPI

from data_extraction_module import trigger_spider, server_status
from from_validation_module import validate_and_submit



st.header("Welcome to Quotes application")



scrapyd = ScrapydAPI('http://localhost:6800')
scrapyd_server = "http://localhost:6800/daemonstatus.json"
project_name = "quotes"
spider_name = "spider"



response = requests.get(scrapyd_server)
spider_status = response.json()

if spider_status["running"] != 0 or spider_status["pending"] != 0:
    while spider_status["running"] != 0 or spider_status["pending"] != 0:
        time.sleep(1.5)
        response = requests.get(scrapyd_server)
        spider_status = response.json()
        print("Spider running ............")
    
    #Todo: Streamlit lite code
    st.success("Spider Finish")

    df = pd.read_csv("DATA.csv") 
    st.write(df.head())




# URL input form
validate_and_submit(
    url_input_label="Enter quotes URL",
    submit_button_label="Submit",
    submit_function=trigger_spider
)




response = requests.get(scrapyd_server)
spider_status = response.json()

if spider_status["running"] != 0 or spider_status["pending"] != 0:
    while spider_status["running"] != 0 or spider_status["pending"] != 0:
        time.sleep(1.5)
        response = requests.get(scrapyd_server)
        spider_status = response.json()
        print("Spider running ............")
    
    #Todo: Streamlit code


    st.success("Spider Finish")
    df = pd.read_csv("DATA.csv") 
    st.write(df.head())
























