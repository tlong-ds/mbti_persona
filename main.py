import streamlit as st
from Account import User
from Modules import VisualHandler
from streamlit_extras.switch_page_button import switch_page

User.create_user_table()

if "bg" not in st.session_state:
    st.session_state.bg = None


# main function
def main():
    switch_page("Home")
if __name__ == "__main__":
    main()