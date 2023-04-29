import re
import time
from typing import Optional

import streamlit as st


def validate_url(url: str) -> bool:
    """
    Validates given URL based on requirements
    Args:
        url (str): The URL to be validated
    Returns:
        bool: True if the URL is valid, False otherwise
    """
    pattern = r"^https://quotes\.toscrape\.com(/(page/([1-9]|10))?|)$"  # Write regular expression based on requirements
    return bool(re.match(pattern, url.rstrip("/")))





def validate_and_submit(url_input_label: str, submit_button_label: str, submit_function):
    """
    Creates a Streamlit form that takes a URL as input, validates it and enables/disables the submit button accordingly

    Args:
        url_input_label (str): The label to be displayed on the input box for the URL
        submit_button_label (str): The label to be displayed on the submit button
        submit_func (function): The function to be called when the form is submitted
    """
    def disable():
        st.session_state.disabled = True

    if "disabled" not in st.session_state:
        st.session_state.disabled = False

    
    with st.form("url_form"):
        url = st.text_input(label=url_input_label)
        submit_button = st.form_submit_button(
            label=submit_button_label,
            on_click=disable,
            disabled=st.session_state.disabled,
        )

    if submit_button:
        if validate_url(url):
            submit_function(url) # Write submit_function based on requirements
        else:
            st.error("Invalid URL, please enter a valid URL.") # Write error message here
            st.session_state.disabled = False
            time.sleep(2)
            st.experimental_rerun()



