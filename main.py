import streamlit as st
from Account import User
from Modules import VisualHandler
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Home",
    page_icon="🌈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

VisualHandler.load_css("./style/style.css")
VisualHandler.custom_sidebar()

User.create_user_table()

# main function
def main():
    switch_page("Home")
if __name__ == "__main__":
    main()