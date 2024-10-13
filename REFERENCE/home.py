import streamlit as st
import requests  
from PIL import Image
from io import BytesIO
import os

def display_home():
    st.subheader("Daily Horoscopes - Home")

    zodiac_images = {
    "Aries": "style/aries.png",
    "Taurus": "style/taurus.png",
    "Gemini": "style/gemini.png",
    "Cancer": "style/cancer.png",
    "Leo": "style/leo.png",
    "Virgo": "style/virgo.png",
    "Libra": "style/libra.png",
    "Scorpio": "style/scorpio.png",
    "Sagittarius": "style/sagittarius.png",
    "Capricorn": "style/capricorn.png",
    "Aquarius": "style/aquarius.png",
    "Pisces": "style/pisces.png"
}

    def get_zodiac_sign(day, month):
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Capricorn"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Aquarius"
        else:
            return "Pisces"

    st.subheader("What is your Zodiac?")
    birthday = st.date_input("Your birthday:")

    if st.button("Let's Find"):
        day = birthday.day
        month = birthday.month
        zodiac_sign = get_zodiac_sign(day, month)

        if zodiac_sign in zodiac_images:
            st.write(f"{zodiac_sign}:")
            file_path = os.path.join(os.getcwd(), zodiac_images[zodiac_sign])  
            image = Image.open(file_path)
            st.image(image, caption=zodiac_sign, use_column_width=True)
            st.balloons()
