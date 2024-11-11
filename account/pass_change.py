import streamlit as st
from Account import User

def password():
    st.header("Change Your Password")

    with st.form(key='password_form'):
        old = st.text_input("Old password", type="password", key='old_password')
        new = st.text_input("New password", type="password", key='new_password')
        confirm = st.text_input("Confirm new password", type="password", key='confirm_password')
        submit_button = st.form_submit_button(label='Change Password')

    if submit_button:
        if old == "" or new == "" or confirm == "":
            st.error("Please fill in all fields!")
        elif not User.login(st.session_state.username, old):
            st.error("Your old password is incorrect!")
        elif old == new:
            st.error("New password must be different from the old one!")
        elif new != confirm:
            st.error("Passwords do not match!")
        else:
            User.change_password(st.session_state.username, new)
            st.success("Password changed successfully")