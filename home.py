import streamlit as st
import requests
import base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# set_background
img = get_img_as_base64("Background.png")
def set_background():
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
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