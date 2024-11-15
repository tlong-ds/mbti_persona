import streamlit as st
import pandas as pd
import base64
from datetime import datetime
from streamlit_extras.switch_page_button import switch_page
from Account import User

class Time:
    @staticmethod
    def real_time():
        hour = datetime.now().hour
        return 'morning' if 5 <= hour < 12 else 'afternoon' if 12 <= hour < 18 else 'evening'

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

    @classmethod
    def light_dark(cls):
        with st.sidebar:
            st.toggle("Light/Dark", False)
    @classmethod
    def custom_sidebar(cls):
        st.markdown("""
        <style>
            /* Hide default sidebar navigation */
            [data-testid="stSidebarNav"] {display: none !important;}
            
            /* Hide default sidebar content */
            .css-1d391kg {display: none}
            section[data-testid="stSidebar"] .css-1d391kg {display: none}
            
            /* Hide collapse control */
            [data-testid="collapsedControl"] {display: none}
            
            /* Additional selectors to ensure navigation is hidden */
            .css-1544g2n.e1fqkh3o4 {display: none !important;}
            .css-1adrfps.e1fqkh3o4 {display: none !important;}
        </style>
        """, unsafe_allow_html=True)

        
        with st.sidebar:
            st.title("Navigation")
            if st.button("Home"):
                switch_page("Home")
            if st.button("Personality Test"):
                switch_page("Personality Test")
            if st.button("Personality Types"):
                switch_page("Personality Types")
            if st.button("About"):
                switch_page("About")
            if st.button("Account"):
                switch_page("Account")
            User.user_management()


    
def reset_app():
    st.session_state.clear()  # Clear all session state variables
