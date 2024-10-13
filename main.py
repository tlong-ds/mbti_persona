import streamlit as st
from streamlit_option_menu import option_menu as opts
from st_pages import add_page_title, get_nav_from_toml
import base64
import webbrowser
st.set_page_config(layout = "wide")
@st.cache_data 

# import css
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# import image
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# set_background
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


# main function
def main():
    set_background()
    nav = get_nav_from_toml("pages.toml")
    pg = st.navigation(nav, expanded=False)
    add_page_title(pg)
    pg.run()
    
if __name__ == "__main__":
    main()