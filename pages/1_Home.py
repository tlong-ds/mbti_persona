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
VisualHandler.initial()

st.title("MBTI PERSONA")
def display_home():
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
    
    st.divider()
    st.markdown("<h2><i><b>“The more you know yourself, the more patience you have for what you see in others.” ",unsafe_allow_html=True)
    st.markdown('<h2><b><i><div style="text-align: right;"> - Erik Erikson -&nbsp;&nbsp;&nbsp;  </div></h2></b></i>', unsafe_allow_html=True)
    with st.form(key = 'p type'):
        col1, col2,col3 = st.columns([10,3,10])
        with col1: 
            st.markdown("<h2>Empathize others</h2>",unsafe_allow_html=True)
            st.write("In our free type descriptions, you’ll embark on an enlightening journey to discover what truly fuels, motivates, and concerns the diverse array of personality types. By understanding these intricate dynamics, you'll cultivate more profound connections and enrich your relationships, bringing depth and inspiration into your interactions with others. Together, let’s foster understanding and empathy, making every relationship a meaningful exchange.")
            if st.form_submit_button('Discover MBTIs'):
                switch_page('Personality Types')
        with col3:
            st.image('./home/communication.webp',use_column_width='auto')
    st.markdown('<br><br>',unsafe_allow_html=True)
    with st.form(key = 'aboy'):
        col1, col2,col3 = st.columns([10,3,10])
        with col3: 
            st.markdown("<h2>Our mission</h2>",unsafe_allow_html=True)
            st.write("Understanding your personality is key to personal and professional growth. Our engaging personality test reveals your key traits and strengths, helping you make better decisions. Start your self-discovery journey today and uncover the qualities that make you unique. Welcome to a path of growth and empowerment with us!")
            if st.form_submit_button('About us'):
                switch_page('About')
        with col1:
            st.image('./home/type-interactions.webp',use_column_width='auto')
    
    

display_home()
