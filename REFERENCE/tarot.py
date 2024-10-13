import streamlit as st
import pandas as pd  

def display_tarot_info():
    st.title("Free Daily Tarot Card Reading")
    st.write("Discover our free daily tarot card reading and take a glimpse into the future. The perfect way to start your day.")
    user_name = st.text_input("Enter your name:")
    if user_name:
        st.success(f'Welcome to our daily tarot reading. Please select your cards, {user_name}!')
    else:
        st.warning('Enter your name, please!')

    tarot_data = pd.read_csv("Tarot-card-Trang-tính1.csv") 

    col1, col2, col3 = st.columns(3)

    image_url_1 = "https://www.horoscope.com/images-US/tarot/back/daily-tarot-mood.png"
    col1.image(image_url_1, use_column_width=True)

    image_url_2 = "https://www.horoscope.com/images-US/tarot/back/daily-tarot-love.png"
    col2.image(image_url_2, use_column_width=True)

    image_url_3 = "https://www.horoscope.com/images-US/tarot/back/daily-tarot-career.png"
    col3.image(image_url_3, use_column_width=True)

    button_1_clicked = col1.button("Card 1")
    button_2_clicked = col2.button("Card 2")
    button_3_clicked = col3.button("Card 3")

    with col1:
        if button_1_clicked:
            selected_card_1 = get_random_card(tarot_data)
            st.image(selected_card_1['Image file'], caption=f"{selected_card_1['Name']}", use_column_width=True)
            display_random_card(selected_card_1['Meaning'])

    with col2:
        if button_2_clicked:
            selected_card_2 = get_random_card(tarot_data)
            st.image(selected_card_2['Image file'], caption=f"{selected_card_2['Name']}", use_column_width=True)
            display_random_card(selected_card_2['Meaning'])

    with col3:
        if button_3_clicked:
            selected_card_3 = get_random_card(tarot_data)
            st.image(selected_card_3['Image file'], caption=f"{selected_card_3['Name']}", use_column_width=True)
            display_random_card(selected_card_3['Meaning'])

def get_random_card(tarot_data):
    return tarot_data.sample().iloc[0]

def display_random_card(card_meaning):
    st.write(f"{card_meaning}")
