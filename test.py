import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Welcome to MBTI Persona")

st.write("Take the MBTI test to discover your personality type.")

if st.button("Take the Test", key="test_button"):
    switch_page("Test")  # Replace "Test" with the exact name of your test page