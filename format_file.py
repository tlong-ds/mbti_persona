import streamlit as st

def formatting():
    def load_css():
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    def buttons_css():
        st.markdown("""
        <style>
        /* Style the selectbox */
        .stSelectbox label {
        color: #4CAF50;  /* Label text color */
        font-size: 16px; /* Label font size */
        }

        /* Style the dropdown itself */
        .stSelectbox .st-bq {
        border-radius: 10px;        /* Rounded corners */
        padding: 5px;               /* Padding inside */
        }
        </style>
        """, unsafe_allow_html=True)        
    
    # run the function
    load_css()
    buttons_css()