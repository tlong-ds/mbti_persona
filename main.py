import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages
from Account import User

st.set_page_config(
    page_title="Your App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# session state
if "login" not in st.session_state:
    st.session_state.login = False
if "username" not in st.session_state:
    st.session_state.username = None
if "name" not in st.session_state:
    st.session_state.name = None
if "ptype" not in st.session_state:
    st.session_state.ptype = None
if "phone" not in st.session_state:
    st.session_state.phone = None
if "email" not in st.session_state:
    st.session_state.email = None
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