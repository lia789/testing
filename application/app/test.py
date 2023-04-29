import streamlit as st
import time


st.header("Hello World")


def f():
  st.write("Function Start")
  time.sleep(5)

  return True


f = f()

if not f:
  st.stop()

st.info("Program Finish")





