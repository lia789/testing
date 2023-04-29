import streamlit as st
from data_extraction_module import trigger_spider, spider_running_status
from from_validation_module import validate_and_submit



st.header("Welcome to Quotes application")


# URL input form
validate_and_submit(
    url_input_label="Enter quotes URL",
    submit_button_label="Submit",
    submit_function=trigger_spider
)


# with st.spinner('Wait for it...'):
#     spider_running_status()
#     st.success("Spider Finish")


spinner = st.empty()
while not spider_running_status():
    spinner.text("Spider is running...")

st.success("Spider finished running!")
























