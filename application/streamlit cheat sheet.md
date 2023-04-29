# **Streamlit**


```cmd
$ pip install streamlit
$ streamlit --help
$ streamlit run your_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version
```


```python
# Home page structure
import streamlit as st
from PIL import Image

Title bar icon
icon = Image.open('icon_image.ico')

# Write application description, to view need Hamburger enable
about_application = "# This is application overview, This is an *extremely* cool app!"

# Base page setup
st.set_page_config(
    page_title="application_title",
    page_icon=icon,
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={'About': about_application}
)

# Remove Hamburger and Footer
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Sidebar page title
st.sidebar.title("Home Page") 

# Your Application code start here
st.header("Hello World")
```


```python
# Form
with st.form("my_form", clear_on_submit=True):
   st.write("Inside the form")
   email =st.text_input("Email")
   password =st.text_input("Password")

   submitted = st.form_submit_button("Submit")

st.write("Outside the form")

if submitted:
   print(email)
   print(password)
   st.write(f"Email: {email}, Password: {password}")
```


```python
# Conditional flow
name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')
```

```python
# Try-Except
try:
   st.info(f'**{number_1}/{number_2}=** {number_1/number_2}')
except ZeroDivisionError:
   st.error('Cannot divide by zero')
```



```python
# From validation module
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

```
