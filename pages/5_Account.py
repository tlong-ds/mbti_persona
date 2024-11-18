import streamlit as st
from account.pass_change import password
from account.membership import display_membership
from account.info import user_info
from Modules import VisualHandler

st.set_page_config(
    page_title="Account",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("Account Management")
if not st.session_state:
    VisualHandler.initial()
else:
    VisualHandler.custom_sidebar()


# Main display function
def display_user():
    if not st.session_state.get('login'):
        st.write("Please login to continue. Thank you!")
        return
    if 'view' not in st.session_state:
        st.session_state.view = 'info'
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write("Functions")
        if st.button("Your Information", use_container_width=True):
            st.session_state.view = "info"
        if st.button("Change Password", use_container_width=True):
            st.session_state.view = "password"
        if st.button("Your membership", use_container_width=True):
            st.session_state.view = "membership"
    with col2:
        # Display the selected view
        if st.session_state.view == "info":
            user_info()
        if st.session_state.view == "password":
            password()
        if st.session_state.view == "membership":
            display_membership()

display_user()