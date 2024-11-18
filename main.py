import streamlit as st
from Account import User
from Modules import VisualHandler
from streamlit_extras.switch_page_button import switch_page

if 'ptype' not in st.session_state:
    st.session_state['ptype'] = None

bg = "bg_d.webp"
VisualHandler.set_background(bg)
VisualHandler.load_css("./style/style.css")
VisualHandler.custom_sidebar()

User.create_user_table()
# main function
def main():
    switch_page("Home")
if __name__ == "__main__":
    main()