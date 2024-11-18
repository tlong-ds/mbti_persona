import streamlit as st
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
    # Set background
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
    # Set sidebar
    @classmethod
    def set_sidebar(cls, image):
        sidebar = cls.get_img_as_base64(image)
        pg_sidebar_img = f"""
        <style>
        [data-testid="stSidebar"] > div:first-child {{
        background-image: url("data:image/png;base64,{sidebar}");
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
        }}
        </style>
        """
        st.markdown(pg_sidebar_img, unsafe_allow_html=True)
    # Set page config
    @classmethod
    def load_css(cls, css: str):
        with open(css) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Custom sidebar
    @classmethod
    def custom_sidebar(cls):
        with st.sidebar:
            bg = "bg_d.webp"
            logo = "logo_d.png"
            sb = "sb_d.webp"
            if st.toggle("Dark/Light Mode"):
                bg = "bg_l.webp"
                logo = "logo_l.png"
                sb = "sb_l.webp"
            st.image(logo, width=280)
            VisualHandler.load_css("./style/style.css")
            VisualHandler.set_sidebar(sb)
            VisualHandler.set_background(bg)
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
            st.divider()
            st.title("User Management")
            User.user_management()
            st.divider()
            st.markdown('<div style="text-align: center;">© 2024 by Group 6 - DSEB 65B</div>', unsafe_allow_html=True)
    
def reset_app():
    st.session_state.clear()  # Clear all session state variables
