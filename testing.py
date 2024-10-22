import streamlit as st

st.set_page_config(page_title="My App", page_icon=":tada:")

# Navigation bar
st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: space-around;
        background-color: #f8f9fa;
        padding: 10px;
        border: 1px solid #dee2e6;
        border-radius: 5px;
    }
    .navbar a {
        text-decoration: none;
        color: #007bff;
        padding: 8px 15px;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .navbar a:hover {
        background-color: #007bff;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Horizontal navigation links
st.markdown('<div class="navbar">'
            '<a href="/home">Home</a>'
            '<a href="/about">About</a>'
            '<a href="/contact">Contact</a>'
            '</div>', unsafe_allow_html=True)

# Main content
st.title("Welcome to My Streamlit App!")
st.write("Use the navigation bar above to switch between pages.")