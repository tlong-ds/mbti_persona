import streamlit as st
import pandas as pd
import base64
from datetime import datetime

class VisualHandler:
    # Convert image to base64
    @staticmethod
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    @classmethod
    @st.cache_data
    def set_background(cls, image):
        background = cls.get_img_as_base64(image)
        
        page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{background}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(page_bg_img, unsafe_allow_html=True)
    @classmethod
    def set_sidebar(cls, image):
        sidebar = cls.get_img_as_base64(image)
        pg_sidebar_img = f"""
        <style>
        [data-testid="stSidebar"] > .main {{
        background-image: url("data:image/png;base64,{sidebar}");
        background-size: cover;
        }}
        </style>
        """
        st.markdown(page_sidebar_img, unsafe_allow_html=True)
    @classmethod
    def load_css(cls, css: str):
        with open(css) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

class Time:
    @staticmethod
    def real_time():
        hour = datetime.now().hour
        return 'morning' if 5 <= hour < 12 else 'afternoon' if 12 <= hour < 18 else 'evening'
    
def reset_app():
    st.session_state.clear()  # Clear all session state variables
