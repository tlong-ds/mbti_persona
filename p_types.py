import streamlit as st
import requests  
from bs4 import BeautifulSoup

def personality_info():
    pass

def display_types():
    if "stage" not in st.session_state:
        st.session_state.stage = 0
    # Select type:
    ptypes = ['-', 'ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENTP', 'ENFP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ', 'Not sure']
    placeholder = st.empty()
    placeholder.markdown('Select your personality type')
    selected = st.selectbox('asa', ptypes, label_visibility="collapsed")
    if selected == 'Not sure':
        st.session_state.stage = 1
    elif selected == '-':
        st.session_state.stage = 0
    else:
        st.session_state.stage = 2
    
    if st.session_state.stage == 1:
        placeholder.markdown('We recommend you to take your first personality test. Do you want to take it now?')
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Yes'):
                placeholder.markdown('Please head to <b>Personality Test</b> to take the test!', unsafe_allow_html = True)
        with col2:
            if st.button('No'):
                placeholder.markdown('We hope you will identify your personality in the future!', unsafe_allow_html = True)
    if st.session_state.stage == 2:
        print('temp')
        # Your function goes here
                

        
    