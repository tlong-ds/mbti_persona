import streamlit as st
import pandas as pd

def user_info():
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f"<h2>{st.session_state.name}</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3>{st.session_state.dob} - {st.session_state.ptype}</h3>", unsafe_allow_html=True)
        st.markdown(f"Your email:", unsafe_allow_html=True)
        st.markdown(f"<h4>{st.session_state.email}</h4>", unsafe_allow_html=True)
        st.markdown(f"Your phone number:", unsafe_allow_html=True)
        st.markdown(f"<h4>{st.session_state.phone}</h4>", unsafe_allow_html=True)
    with col2:
        st.image("https://static.vecteezy.com/system/resources/previews/009/292/244/non_2x/default-avatar-icon-of-social-media-user-vector.jpg", width=200)
        st.write("Change your profile picture")

def display_user():
    if not st.session_state.login:
        st.write("Please login to continue. Thank you!")
        return
    else:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.write("Functions")
            f1 = st.button("Your information", use_container_width = True)
            f2 = st.button("Change password", use_container_width = True)
            f3 = st.button("Your membership", use_container_width = True)
        with col2:
            if f1:
                user_info()

display_user()