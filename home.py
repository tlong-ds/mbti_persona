import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import os

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def display_home():
    load_css()
    st.text('Hello')