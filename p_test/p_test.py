import streamlit as st
import pandas as pd
import base64
from datetime import datetime

# Import questions
questions = pd.read_csv('./p_test/qsets.tsv', sep='\t')

# Convert image to base64
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("./p_test/Background.png")

# Set background image
@st.cache_data
def set_background():
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

# Reset the page
def reset_app():
    st.session_state.clear()  # Clear all session state variables

# Greeting based on real-time
def friendly():
    hour = datetime.now().hour
    return 'morning' if 5 <= hour < 12 else 'afternoon' if 12 <= hour < 18 else 'evening'

def save_responses():
    responses_df = pd.DataFrame(st.session_state['answers'].items(), columns=['Dimension', 'Score'])
    file_name = f"{st.session_state['name']}_responses.csv"
    responses_df.to_csv(file_name, index=False)
    st.write(f"Responses saved as {file_name}!")
    st.download_button(
        label="Download CSV",
        data=responses_df.to_csv(index=False),
        file_name=file_name,
        mime="text/csv"
    )
# Test display function with radio buttons
def test():
    for i, q in questions.iterrows():
        st.divider()
        st.markdown(f"Question {i + 1} of {len(questions)}: <b>{q['question']}</b>", unsafe_allow_html=True)
        
        # Radio buttons for each answer option
        response = st.radio(
            label="Select an option:",
            options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
            key=f'question_{i}'
        )
        
        # Mapping response to score
        score_map = {
            "Strongly Disagree": -2,
            "Disagree": -1,
            "Neutral": 0,
            "Agree": 1,
            "Strongly Agree": 2
        }
        st.session_state['answers'][q["dimension"]] = st.session_state['answers'].get(q["dimension"], 0) + score_map[response]
        st.divider()
        
    # Calculate MBTI type if completed
    if st.button('Submit', type='primary'):
        st.session_state['completed'] = True

    if st.session_state['completed']:
        dimensions = {'E/I': 0, 'S/N': 0, 'T/F': 0, 'J/P': 0}
        for dimension, score in st.session_state['answers'].items():
            dimensions[dimension] += score
        
        mbti_type = (
            ('E' if dimensions['E/I'] >= 0 else 'I') +
            ('S' if dimensions['S/N'] >= 0 else 'N') +
            ('T' if dimensions['T/F'] >= 0 else 'F') +
            ('J' if dimensions['J/P'] >= 0 else 'P')
        )
        
        st.session_state['mbti_type'] = mbti_type
        st.session_state.stage = 3
        st.rerun()
        return st.session_state.stage  # Move to final stage

# Main function to display the test
def display_test():
    set_background()
    placeholder = st.empty()
    
    # Initialize session states
    if 'answers' not in st.session_state:
        st.session_state['answers'] = {}
    if 'completed' not in st.session_state:
        st.session_state['completed'] = False
    if 'name' not in st.session_state:
        st.session_state['name'] = ''
    if 'stage' not in st.session_state:
        st.session_state['stage'] = 0
    if 'mbti_type' not in st.session_state:
        st.session_state['mbti_type'] = None
    
    if st.session_state['name'] == '':
        st.markdown(f'<p class="question-text">Good {friendly()}. What\'s your name?</p>', unsafe_allow_html=True)
        name_input = st.text_input(f'Enter your name here: ')
        if name_input and not st.session_state['completed']:
            st.session_state['name'] = name_input  # Save the name
            st.rerun()  # Trigger a rerun to hide the input box
    else:
        placeholder.markdown(f"""Good {friendly()}, {st.session_state['name']}! 
                                 Are you ready to take your personality test? <br> 
                                 There are <b>60 questions</b> in this test, 
                                 and you have to answer all of them to identify your personality type. <br>
                                 If you are ready, click <b>Yes</b>. Otherwise, click <b>No</b>. You can still see the test later!
                              """, unsafe_allow_html=True)
        
        if 'clicked' not in st.session_state:
            st.session_state['clicked'] = False

        if not st.session_state.clicked:
            col1, col2 = st.columns(2)
            with col1:
                if st.button('Yes'):
                    st.session_state.stage = 1
                    st.session_state.clicked = True
                    st.rerun()
            with col2:
                if st.button('No'):
                    st.session_state.stage = 2
                    st.session_state.clicked = True
                    st.rerun()
        
        if st.session_state.stage == 1:
            placeholder.markdown(f"""
                                 Alright, {st.session_state['name']}. Let's start the test! <br>
                                 Note that you cannot go back to previous question, so you have to be careful of your answer!
                                 """, unsafe_allow_html=True)
            test()
            
        
        if st.session_state.stage == 2:
            placeholder.write("If you change your mind, you can reload the page or press this button!")
            st.button('Restart', on_click=reset_app, key="re_entering")
        
        if st.session_state.stage == 3:
            
            placeholder.write(f"Thank you, {st.session_state['name']}!")
            st.write(f"Your MBTI Type is: **{st.session_state['mbti_type']}**")
            st.write(f"Learn more about your personality:")
                
            st.button('Restart', on_click=reset_app, key="retake_the_test")

display_test()