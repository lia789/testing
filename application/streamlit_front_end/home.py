import re
import time
import streamlit as st




def disable():
    st.session_state.disabled = True

if "disabled" not in st.session_state:
    st.session_state.disabled = False




# Define a function to validate the user's input URL
def validate_input_url(input_url):
    url_pattern = r'^https://quotes\.toscrape\.com(/(page/([1-9]|10))?|)$'
    if re.match(url_pattern, input_url.rstrip('/')):
        return True
    else:
        return False



# Create a Streamlit form
with st.form("my_form"):
    user_input_url = st.text_input("Enter URL Here:")
    submit_button = st.form_submit_button("Submit", on_click=disable, disabled=st.session_state.disabled)



# Validate the user's input URL when the submit button is clicked
if submit_button:
    if validate_input_url(user_input_url):
        #Todo: DO THE TASK HERE
        pass
    else:
        st.error("Invalid input URL, Please enter a valid URL")
        st.session_state.disabled = False
        time.sleep(2)
        st.experimental_rerun()
    