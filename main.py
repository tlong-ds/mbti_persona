import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages
from Account import User

st.set_page_config(
    page_title="MBTI Persona",
    page_icon="🌈",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# session state
if "login" not in st.session_state:
    st.session_state.login = False
User.create_user_table()
User.user_management()

# main function
def main():
    nav = get_nav_from_toml("pages.toml")
    pg = st.navigation(nav)    
    add_page_title(pg)
    pg.run()
    
if __name__ == "__main__":
    main()