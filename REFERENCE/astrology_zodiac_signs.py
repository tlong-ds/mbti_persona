import streamlit as st
import requests  
from bs4 import BeautifulSoup

def display_zodiac_info():
    st.title("Astrology Zodiac Signs")

    selectedd = st.selectbox("Choose your Zodiac", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    zodiac = st.radio("Select Option", ["Love", "Lifestyle", "Friendship", "Health"])

    url = f"https://www.horoscope.com/zodiac-signs/{selectedd.lower()}/{zodiac.lower()}"

    res = requests.get(url)

    content = BeautifulSoup(res.content, 'html.parser')  # Ensure BeautifulSoup is imported and available

    sections = content.find_all(['h3', 'p'])

    displayed_text = ""
    for section in sections:
        if section.name == 'h3':
            displayed_text += f"<h3>{section.text}</h3>"
        elif section.name == 'p':
            displayed_text += f"<p>{section.text}</p>"

    st.markdown(displayed_text, unsafe_allow_html=True) 
