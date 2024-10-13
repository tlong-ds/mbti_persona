import streamlit as st
import requests  
from bs4 import BeautifulSoup

# Forecast Function 
def get_horoscope_by_day(zodiac_sign: int, day: str):
    if not "-" in day:
        res = requests.get(
            f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={zodiac_sign}")
    else:
        day = day.replace("-", "")
        res = requests.get(
            f"https://www.horoscope.com/us/horoscopes/general/horoscope-archive.aspx?sign={zodiac_sign}&laDate={day}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text

def get_horoscope_by_month(zodiac_sign: int):
    res = requests.get(
        f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-monthly.aspx?sign={zodiac_sign}")
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.find('div', attrs={'class': 'main-horoscope'})
    return data.p.text

def display_forecast():
        # Zodiac sign dropdown
        signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        selected_sign = st.selectbox("Choose Your Zodiac Sign", signs)
        zodiac_sign = signs.index(selected_sign) + 1

        # Horoscope period radio
        horoscope_period = st.radio("Choose the Horoscope Period", ["Daily", "Monthly", "Yearly"])

        # Horoscope result
        horoscope = ""
        if horoscope_period == "Daily":
            day = st.date_input("Choose the date for daily horoscope")
            if day:
                try:
                    horoscope = get_horoscope_by_day(zodiac_sign, day.strftime("%Y-%m-%d"))
                except requests.RequestException as e:
                    st.error(f"Failed to retrieve horoscope: {e}")
        elif horoscope_period == "Yearly":
            selectedd = st.selectbox("Confirm your Zodiac", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
            selected_year = st.selectbox("Choose year", list(range(2016, 2024)))

            url = f"https://www.horoscope.com/us/horoscopes/yearly/{selected_year}-horoscope-{selectedd.lower()}.aspx"

            res = requests.get(url)

            content = BeautifulSoup(res.content, 'html.parser')

            sections = content.find_all(['h2', 'p'])

            displayed_text = ""
            for section in sections:
                if section.name == 'h2':
                    displayed_text += f"<h3>{section.text}</h2>"
                elif section.name == 'p':
                    displayed_text += f"<p>{section.text}</p>"

            st.markdown(displayed_text, unsafe_allow_html=True) 

        elif horoscope_period == "Monthly":
            horoscope = get_horoscope_by_month(zodiac_sign)

        if horoscope:
            st.success(f"{selected_sign} Horoscope for {horoscope_period.lower()} period:\n{horoscope}")
