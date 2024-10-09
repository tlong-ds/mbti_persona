import streamlit as st
from streamlit_option_menu import option_menu as opts
import base64
import webbrowser

from home import display_home
from p_test import display_test
from p_types import display_types
from about import display_about

if "page" not in st.session_state:
    st.session_state.page = 0

@st.cache_data
# import image
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background():
    img = get_img_as_base64("Background.png")
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

def main():
    set_background()
    placeholder = st.empty()
        
    with st.sidebar:
        selected = opts(
            menu_title = None,
            options = ['Home', 'Personality Test', 'Personality Types', 'About Us'],
            icons = ['house', 'person', 'star', 'info-circle'],
            default_index=0,
            styles={"container": {"padding": "0 !important", "background-color": "#262730"},
                    "icon": {"color": "white", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "15px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#ffe8e8",
                    },
                "nav-link-selected": {"background-color": "pink"},
            }
        )
    
    if selected == 'Home':
        st.session_state.page = 0
        display_home()
        
    if selected == 'Personality Test':
        st.session_state.page = 1
        display_test()
    if selected == 'Personality Types':
        st.session_state.page = 2 
        display_types()
    if selected == 'About Us':
        st.session_state.page = 3
        display_about()
    with placeholder:
        if st.session_state.page == 0:
            st.title('MBTI Personality Test')
        if st.session_state.page == 1:
            st.title('The Personality Test')
        if st.session_state.page == 2:
            st.title('Personality Types')
        if st.session_state.page == 3:
            st.title('About Us')

if __name__ == "__main__":
    main()