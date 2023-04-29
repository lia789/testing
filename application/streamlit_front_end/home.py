import streamlit as st
from from_validation import validate_and_submit
from spider import trigger_spider

st.header("Welcome to Quotes application")


validate_and_submit(
    url_input_label="Enter quotes URL",
    submit_button_label="Submit",
    submit_function=trigger_spider
)
























