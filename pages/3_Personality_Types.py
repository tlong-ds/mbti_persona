import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from Modules import VisualHandler

st.set_page_config(
    page_title="Personality Types",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed",
)
if 'ptype' not in st.session_state:
    st.session_state['ptype'] = None

st.title("Personality Types")
if not st.session_state:
    VisualHandler.initial()
else:
    VisualHandler.custom_sidebar()
    VisualHandler.set_background(st.session_state.bg)

def personality_info(): # Task for Pham Khanh Linh, Bui Viet Huy
    # Your function goes here
    st.write("Explore this type")
    

def display_types():
    if "stage_type" not in st.session_state:
        st.session_state.stage_type = 0
    # Select type:
    ptypes = [None, 'ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENTP', 'ENFP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ', 'Not sure']
    placeholder = st.empty()
    placeholder.markdown('Select your personality type')
    selected = st.selectbox('asa', ptypes, label_visibility="collapsed", index = ptypes.index(st.session_state.ptype))
    if selected == 'Not sure':
        st.session_state.stage_type = 1
    elif selected == None:
        st.session_state.stage_type = 0
    else:
        st.session_state.stage_type = 2
    
    if st.session_state.stage_type == 1:
        placeholder.markdown('We recommend you to take your first personality test. Do you want to take it now?')
        if st.button('Yes'):
            switch_page('Personality Test')
    if st.session_state.stage_type == 2:
        personality_info()
        
display_types()

        
    