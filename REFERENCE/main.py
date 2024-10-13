import streamlit as st
from home import display_home
from forecast import display_forecast
from astrology_zodiac_signs import display_zodiac_info
from about_us import display_about_info
from tarot import display_tarot_info
import base64
from streamlit_option_menu import option_menu
import webbrowser 

# Background
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background():
    img = get_img_as_base64("Background.png")
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: 100%;
        background-repeat: no-repeat;
        background-attachment: local;
        }}
        </style>
        """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    set_background()
    
    # Intro 
    st.title("Daily Horoscopes")
    st.text("'Get your free daily, monthly, yearly horoscopes reading!'")

    # Menu
    with st.sidebar:
        selected = option_menu(
            menu_title = None, 
            options = ["Home", "Forecast", "Astrology Zodiac Signs" ,"Contact Us", "About Us", "Tarot"], 
            icons = ['house', 'cloud-sun', 'star', 'envelope', 'info-circle', "gem"],
            menu_icon = "cast", 
            default_index = 0,
            styles = {
                "container": {"padding": "0!important", "background-color": "#0d0c0c"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#808080",
                },
                "nav-link-selected": {"background-color": "grey"},
            },
        )

    if selected == "Home":
        display_home()
    elif selected == "Forecast":
        display_forecast()
    elif selected == "Astrology Zodiac Signs":
        display_zodiac_info()
    elif selected == "Contact Us":
        # Function to open the Facebook page
        def open_facebook_page():
            webbrowser.open_new_tab("https://www.facebook.com/profile.php?id=61553564769648")
            
        # Function to show the feedback form
        def show_feedback_form():
            st.header(":mailbox: Leave your feedback for us!")
            contact_form = """
            <form action="https://formsubmit.co/stellar.fbuser@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here"></textarea>
             <button type="submit">Send</button>
        </form>
        """
            st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        local_css("style/style.css")

        # Create a button to toggle between Facebook page and feedback form
        selected_option = st.radio("Select an option:", ["Contact Us", "Feedback Form"])

        if selected_option == "Contact Us":
            st.button("Go to Facebook Page", on_click=open_facebook_page)
        elif selected_option == "Feedback Form":
            show_feedback_form()

    elif selected == "About Us":
        display_about_info()
    elif selected == "Tarot":
        display_tarot_info()
