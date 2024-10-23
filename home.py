import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import os
import base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# set_background
def set_background():
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("/static/Background.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
def display_home(): # Task for Nguyen Dang Minh, Ninh Duy Tuan
    set_background()
    st.balloons()

    # Your function goes here!
    st.write('Hello')

display_home()