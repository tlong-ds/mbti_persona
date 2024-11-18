import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from Modules import VisualHandler
import base64

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed",
)
if not st.session_state:
    VisualHandler.initial()
else:
    VisualHandler.custom_sidebar()
    VisualHandler.set_background(st.session_state.bg)

st.title("MBTI PERSONA")
def display_home(): # Task for Nguyen Dang Minh, Ninh Duy Tuan
    col1, col2 = st.columns([15,5])
    with col1:
        st.header("""Welcome to our website! \n Only 10 minutes to get a “freakishly accurate” description of who you are and why you do things the way you do.""")
    if st.button("Take the Test", key="test_button"):
        switch_page("Personality Test")
    st.markdown('</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.markdown('<div style="text-align: center; font-size: 40px;">144K+ </div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; font-size: 15rx;">Tests taken today </div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div style="text-align: center; font-size: 40px;">25K+</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; font-size: 15px;">Tests taken in VietNam </div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div style="text-align: center; font-size: 40px;">1000K+</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align: center; font-size: 15px;">Total tests taken </div>', unsafe_allow_html=True)
    
    # Tuan
    
    

display_home()
