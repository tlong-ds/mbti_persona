import streamlit as st

def display_about_info():
    st.title("About Us - Stellar")
    st.write("Welcome to Stellar, your celestial companion on the journey through the cosmic tapestry. At Stellar, we believe in the profound connection between individuals and the celestial forces that shape their destinies. As a leading Daily Horoscope Web Service, we empower users to navigate life's twists and turns with insights drawn from the stars themselves.")
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image("https://scontent-hkg4-1.xx.fbcdn.net/v/t1.15752-9/376576294_1024187448862555_8898121516945095085_n.png?_nc_cat=109&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeHbeyz6QuAy7_XXvSPgEx_YGWPE2KxmrbIZY8TYrGatskiOlVn3cqtoyze9DpoZrPs2LYmt7qogJ_56fo933Bzo&_nc_ohc=it9hmFoSwAkAX_zWQCJ&_nc_ht=scontent-hkg4-1.xx&oh=03_AdR7G3ILyHR2O7_I8qXh-BlX1msgY7Aj98rjnJcXf_ltAQ&oe=6593F35D", caption='Stellar Logo')

    with col2:
        st.header("Our Offerings:")
        
        offerings = {
            "Daily Horoscope Readings": "Find your zodiac sign, and let the universe unfold its secrets. Our daily horoscope readings provide personalized guidance tailored to your unique cosmic imprint, helping you seize the opportunities and overcome challenges that each day presents.",
            "Timeless Insights": "Delve deeper into the cosmic currents with our weekly, monthly, and yearly forecasts. Uncover the patterns that shape your life over extended periods, allowing you to make informed decisions and align with the cosmic energies surrounding you.",
            "Tarot Readings": "Unlock the mystical realm with our Tarot Reading feature. Explore the ancient art of divination and gain profound insights into your past, present, and future. Our Tarot readings offer a captivating glimpse into the unseen forces that influence your journey.",
            "Astrology Zodiac Sign Exploration": "Dive into the rich tapestry of astrology by exploring the characteristics and traits associated with your zodiac sign. Discover the nuances that make you uniquely you and gain a deeper understanding of the cosmic energies that shape your personality."
        }
        
        for offering, description in offerings.items():
            st.subheader(offering)
            st.write(description)
        
        st.header("Our Slogan:")
        st.write('"Apocalypse | Tarot | Astrology"')
        st.write("This powerful mantra embodies the essence of Stellar. We believe in empowering individuals to face life's challenges with strength and grace, drawing inspiration from the apocalypse, seeking guidance through the wisdom of tarot, and understanding the cosmic dance through astrology.")
    
        st.write("At Stellar, we are not just a Daily Horoscope Web Service; we are your cosmic confidants, guiding you through the celestial wonders that surround you. Join us on this extraordinary journey as we explore the mysteries of the universe together.")
