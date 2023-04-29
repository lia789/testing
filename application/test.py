import streamlit as st
# from . module import validate_and_submit

from from_validation import validate_and_submit


st.header("Welcome to quotes application")



def h(url):
    print(url)


validate_and_submit(
    url_input_label="Enter Your URL Here",
    submit_button_label="Start",
    submit_function=h
    )




