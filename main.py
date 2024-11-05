import streamlit as st
from st_pages import add_page_title, get_nav_from_toml 
st.set_page_config(layout = "wide")
@st.cache_data

# main function
def main():
    nav = get_nav_from_toml("pages.toml")
    pg = st.navigation(nav)
    add_page_title(pg)
    pg.run()
    
if __name__ == "__main__":
    main()