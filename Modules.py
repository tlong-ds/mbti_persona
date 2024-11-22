import streamlit as st
import base64
import toml
from datetime import datetime
from streamlit_extras.switch_page_button import switch_page
from Account import User


class Time:
    @staticmethod
    def real_time():
        hour = datetime.now().hour
        return 'morning' if 5 <= hour < 12 else 'afternoon' if 12 <= hour < 18 else 'evening'

class VisualHandler:
    DARK_BG = "bg_d.webp"
    LIGHT_BG = "bg_l.webp"
    DARK_LOGO = "logo_d.png"
    LIGHT_LOGO = "logo_l.png"
    DARK_CSS = "./style/dark.css"
    LIGHT_CSS = "./style/light.css"
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

    @classmethod
    def mode(cls):
        with open('.streamlit/config.toml', 'r') as f:
            config = toml.load(f)
        st.session_state.theme = config['theme']['base']
        selected = st.select_slider("Select theme", options=["dark", "light"], value=st.session_state.theme)
        if selected != st.session_state.theme:
            st.session_state.theme = selected
            st.session_state.bg = cls.LIGHT_BG if selected == "light" else cls.DARK_BG
            st.session_state.logo = cls.LIGHT_LOGO if selected == "light" else cls.DARK_LOGO
            st.session_state.css = cls.LIGHT_CSS if selected == "light" else cls.DARK_CSS
            config['theme']['base'] = selected
            with open('.streamlit/config.toml', 'w') as f:
                toml.dump(config, f)
            st.rerun()
            st.rerun()

    # Custom sidebar
    @classmethod
    def custom_sidebar(cls):
        with st.sidebar:
            VisualHandler.mode() 
            VisualHandler.load_css(st.session_state.css)
            if "logo" in st.session_state and st.session_state.logo != None: 
                st.image(st.session_state.logo, width=280)
            if st.button("Home"):
                st.balloons()
                switch_page("Home")
            if st.button("Personality Test"):
                st.balloons()
                switch_page("Personality Test")
            if st.button("Personality Types"):
                st.balloons()
                switch_page("Personality Types")
            if st.button("About"):
                st.balloons()
                switch_page("About")
            st.divider()
            st.title("User Management")
            User.user_management()
            st.divider()
            st.markdown('<div style="text-align: center">© 2024 by Group 6 - DSEB 65B</div>', unsafe_allow_html=True)

    @classmethod
    def initialize_session_state(cls):
        with open('.streamlit/config.toml', 'r') as f:
            config = toml.load(f)
        current_theme = config['theme']['base']
        if "theme" not in st.session_state:
            st.session_state.theme = current_theme
        if "bg" not in st.session_state:
            st.session_state.bg = cls.LIGHT_BG if current_theme == "light" else cls.DARK_BG
        if "logo" not in st.session_state:
            st.session_state.logo = cls.LIGHT_LOGO if current_theme == "light" else cls.DARK_LOGO
        if "css" not in st.session_state:
            st.session_state.css = cls.LIGHT_CSS if current_theme == "light" else cls.DARK_CSS
    
    @classmethod
    def initial(cls):
        cls.initialize_session_state()  
        cls.custom_sidebar()
        if st.session_state.bg != None:
            cls.set_background(st.session_state.bg)
        