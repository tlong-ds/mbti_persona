import streamlit as st
import requests
import base64
from Modules import VisualHandler
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# set_background
VisualHandler.set_background("./home/Background.webp")
def display_home(): # Task for Nguyen Dang Minh, Ninh Duy Tuan
    st.balloons()
    # Your function goes here!
    st.write('Hello')

display_home()