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

