import streamlit as st
import requests  
import base64
from bs4 import BeautifulSoup
from Modules import VisualHandler
from p_types.type_info import personality_info
VisualHandler.set_background("./p_test/Background.webp")

def display_types():
    
    if "stage_type" not in st.session_state:
        st.session_state.stage_type = 0
    # Select type:
    ptypes = ['-', 'ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENTP', 'ENFP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ', 'Not sure']
    placeholder = st.empty()
    placeholder.markdown('Select your personality type')
    selected = st.selectbox('asa', ptypes, label_visibility="collapsed")
    if selected == 'Not sure':
        st.session_state.stage_type = 1
    elif selected == '-':
        st.session_state.stage_type = 0
    else:
        st.session_state.stage_type = 2
    
    if st.session_state.stage_type == 1:
        placeholder.markdown('We recommend you to take your first personality test. Do you want to take it now?')
        st.markdown('[Click here to head to the Personality Test](./p_test)', unsafe_allow_html=True)
    if st.session_state.stage_type == 2:
        personality_info()
        
display_types()

        
    