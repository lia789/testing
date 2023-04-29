import streamlit as st
# from . module import validate_and_submit
import module as mn


st.header("Welcome to quotes application")



def h():
    print("Hello World")


mn.validate_and_submit(
    url_input_label="Enter Your URL Here",
    submit_button_label="Start",
    submit_function=h
    )


