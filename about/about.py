import streamlit as st
import base64

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Set background image
img = get_img_as_base64("./about/Background.png")
def set_background():
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        }}
        </style>
        """ 
    st.markdown(page_bg_img, unsafe_allow_html=True)

def display_about(): 
    set_background()
    st.write("""Understanding one's personality and the ways 
    it influences interactions with the world is invaluable for personal development, 
    professional growth, and relationship building. This personality test application 
    provides users with an opportunity for insightful self-reflection 
    through a structured and engaging approach. 
    Each question is carefully crafted to reveal key personality traits, 
    strengths, and preferences, enabling users to gain a clearer 
    perspective on themselves and their unique qualities. 
    With these insights, individuals are empowered to make 
    informed decisions that enhance their personal and professional lives. 
    Embark on this journey of self-discovery today and uncover a deeper understanding of your own character.""")
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image("/Users/apple/Downloads/OIP.jpeg", width=200) 
    with col2:
        st.header("Our Offerings")
        
        offerings = {
        
            "Reliable Personality Tests": 
            "We provide personality tests based on trusted methods like MBTI, Big Five, and DISC, giving you accurate and scientifically supported results",
            "User-Friendly Interface":
            "Our simple and easy-to-navigate interface allows you to complete the test effortlessly and understand the results clearly",
            "Visualized Results Analysis":
            "Results are displayed through clear and easy-to-understand charts, helping you recognize your strengths and weaknesses",
            "Personal Development Suggestions":
            "Based on your results, we offer helpful suggestions for personal growth and career direction",
            "Personal Development Suggestions":
            "Based on your results, we offer helpful suggestions for personal growth and career direction",
            "Information Security":
            "We are committed to protecting your privacy, ensuring that all personal information remains secure and confidential",
        }
        
        for offering, description in offerings.items():
            st.subheader(offering)
            st.write(description)
    st.header("Our Slogan")
    st.write('"Discover Yourself, Empower Your Path"')
    st.write("This powerful mantra embodies the essence of our personality testing platform. We believe in empowering individuals to navigate life’s complexities with clarity and confidence. Through the lens of psychological insight, we help uncover the unique traits, strengths, and motivations that shape each person. Rooted in well-researched personality frameworks, our approach guides users toward a deeper understanding of themselves and the paths that align with their true nature. Let us be your compass on this journey of self-discovery, offering insights that illuminate your personal and professional growth")
    st.write("Here, we are more than just a personality testing platform; we are your companion on the journey of self-discovery. We stand by your side, helping you gain a deeper understanding of your unique identity and approach life with confidence. Join us on this extraordinary journey, where each answer brings you closer to your true self")
# Call the function to display the page
    st.header("Contact Us")
    st.write("""
    - **Email**: mbtipersona@gmail.com
    - **Phone**: +84 123 456 789
    - **Facebook Page**: https://www.facebook.com/itsjkchan
     """)
display_about() 
