import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from Modules import VisualHandler


# Task for Pham Khanh Linh, Bui Viet Huy
st.set_page_config(
    page_title="Personality Types",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="collapsed",
)
if 'ptype' not in st.session_state:
    st.session_state['ptype'] = 'None'

data = pd.read_csv("./p_types/type_data.csv", index_col = "type")

st.title("Personality Types")
VisualHandler.initial()

def personality_info(text): 
    # Your function goes here
    print(data.loc[text]["img"])
    st.image(f"{data.loc[text]['img']}")
    st.markdown(f"<font size = '8'>**{text}: {data.loc[text]['title']}**</font>", unsafe_allow_html = True)
    st.markdown(f"<font size = '5'>{data.loc[text]['description']} </font>", unsafe_allow_html = True)
    st.markdown(f"<font size = '4'>{data.loc[text]['percentage']} of the population</font>", unsafe_allow_html = True)
    
    col1, col2 = st.columns([1, 5])
    with col1:
        st.write("Explore this type:")
        columns = [i.title() for i in list(data.columns)[4:]]
        selected = st.selectbox("Select", columns, index = 0, label_visibility = "collapsed")
    with col2:
        st.markdown(data.loc[text][selected.lower()], unsafe_allow_html = True)
    

def display_types():
    if "stage_type" not in st.session_state:
        st.session_state.stage_type = 0
    # Select type:
    ptypes = ['None', 'ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENTP', 'ENFP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ', 'Not sure']
    placeholder = st.empty()
    
    placeholder.markdown('Select your personality type')
    selected = st.selectbox('asa', ptypes, label_visibility="collapsed", index = ptypes.index(st.session_state.ptype))
    if selected == 'Not sure':
        st.session_state.stage_type = 1
    elif selected == 'None':
        st.session_state.stage_type = 0
    else:
        st.session_state.stage_type = 2
    
    if st.session_state.stage_type == 1:
        placeholder.markdown('We recommend you to take your first personality test. Do you want to take it now?')
        if st.button('Yes'):
            switch_page('Personality Test')
    if st.session_state.stage_type == 2:
        personality_info(selected)
        
display_types()

        
    