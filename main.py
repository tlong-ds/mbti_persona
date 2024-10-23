import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
import base64
import webbrowser
st.set_page_config(layout = "wide")
@st.cache_data


# import css
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# main function
def main():
    set_background()
    nav = get_nav_from_toml("pages.toml")
    pg = st.navigation(nav)
    add_page_title(pg)
    pg.run()
    
if __name__ == "__main__":
    main()