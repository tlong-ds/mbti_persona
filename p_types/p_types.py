import streamlit as st
import requests  
import base64
from bs4 import BeautifulSoup

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# set_background
img = get_img_as_base64("./p_types/Background.png")
def set_background():
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
        }}
        </style>
        """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)
def personality_info(): # Task for Pham Khanh Linh, Bui Viet Huy
    # Your function goes here
    pass

def display_types():
    set_background()
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
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Yes'):
                placeholder.markdown('Please head to <b>Personality Test</b> to take the test!', unsafe_allow_html = True)
        with col2:
            if st.button('No'):
                placeholder.markdown('We hope you will identify your personality in the future!', unsafe_allow_html = True)
    if st.session_state.stage_type == 2:
        personality_info()
        
display_types()

        
    