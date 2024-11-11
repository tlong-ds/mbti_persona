import streamlit as st
from Account import User
from datetime import date

def save_changes():
    try:
        name = st.session_state.name_input
        dob = st.session_state.dob_input
        gender = st.session_state.gender_input
        email = st.session_state.email_input
        phone = st.session_state.phone_input
        avatar = st.session_state.temp_avatar if st.session_state.temp_avatar else st.session_state.avt
        User.change_info(
            st.session_state.username, name, dob, gender, phone, email, avatar
        )
        st.session_state.view = "info"
        st.session_state.temp_avatar = None
        st.success("Profile updated successfully!")

    except Exception as e:
        st.error(f"Failed to update profile: {str(e)}")
def edit_info():
    with st.form(key="edit_form"):
        col1, col2 = st.columns([1, 1])
        with col1:
        # Pre-fill with current values
            st.text_input("Name", value=st.session_state.name, key="name_input")
            st.date_input(
                "Date of Birth",
                min_value=date(1900, 1, 1),
                max_value=date.today(),
                value=date.today(),
                key="dob_input"
            )
            st.selectbox("Gender", options = ["Male", "Female", "Other"], index = 2, key="gender_input")
            st.text_input("Email", value=st.session_state.email, key="email_input")
            st.text_input("Phone number", value=st.session_state.phone, key="phone_input")
        st.form_submit_button("Save Changes", on_click=save_changes)        


def user_info():
    st.header("Your Information")
    if 'temp_avatar' not in st.session_state:
        st.session_state.temp_avatar = None
    if 'view' not in st.session_state:
        st.session_state.view = 'info'

    if st.session_state.view == "info":
        with st.form(key="info_form"):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown(f"<h3>{st.session_state.name}, {st.session_state.gender}, {st.session_state.ptype}</h3>", unsafe_allow_html=True)
                st.markdown(f"<h4>{st.session_state.dob}</h4>", unsafe_allow_html=True)
                st.markdown(f"Your email: {st.session_state.email}", unsafe_allow_html=True)
                st.markdown(f"Your phone number: {st.session_state.phone}", unsafe_allow_html=True)
            with col2:
                st.image(st.session_state.avt, width=200)
            if st.form_submit_button("Edit your information"):
                st.session_state.view = "edit"

    if st.session_state.view == "edit":
        edit_info()