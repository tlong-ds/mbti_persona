import streamlit as st
import pandas as pd

from datetime import datetime
from format_file import formatting
st.set_page_config(page_title="p test")


def reset_app():
    # Clear any session state variables or reset values
    for key in st.session_state.keys():
        del st.session_state[key]
    
def set_state(i):
    st.session_state.stage = i

questions = [
    {"question": "I feel energized after socializing with people.", "dimension": "E/I"},
    {"question": "I often need time alone to recharge after a busy day.", "dimension": "S/N"},
    {"question": "I trust information that is more concrete and based on real experiences.", "dimension": "T/F"},
    {"question": "I enjoy exploring theoretical ideas and abstract concepts.", "dimension": "J/P"},
    # Add more questions here...
]


def friendly():
    current_time = datetime.now().strftime("%H:%M:%S")
    hms = current_time.split(':')
    hour = int(hms[0])
    if hour >= 5 and hour < 12:
        return 'morning'
    if hour >= 12 and hour < 18:
        return 'afternoon'
    if (hour >= 18 and hour <= 23) or (hour >= 0 and hour < 5):
        return 'evening'


def test():
    
    if st.session_state['current_question'] < len(questions):
        current = st.session_state['current_question']
        q = questions[current]
        st.write(f"Question {current + 1} of {len(questions)}")
        with st.form(key=f"question_form_{current}"):
            response = st.selectbox(q["question"], options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"])
            if st.form_submit_button("Next", type = 'primary'):
                print('clicked')
                score = {"Strongly Disagree": -2, "Disagree": -1, "Neutral": 0, "Agree": 1, "Strongly Agree": 2}[response]
                st.session_state['answers'][q["dimension"]] = st.session_state['answers'].get(q["dimension"], 0) + score
                st.session_state['current_question'] += 1
    else:
        st.session_state['completed'] = True
       
    
    if st.session_state['completed'] == True:
        dimensions = {'E/I': 0, 'S/N': 0, 'T/F': 0,  'J/P': 0}
        for dimension, score in st.session_state['answers'].items():
            dimensions[dimension] += score
        mbti_type = ""
        mbti_type += 'E' if dimensions['E/I'] >= 0 else 'I'
        mbti_type += 'S' if dimensions['S/N'] >= 0 else 'N'
        mbti_type += 'T' if dimensions['T/F'] >= 0 else 'F'
        mbti_type += 'J' if dimensions['J/P'] >= 0 else 'P'

        st.write(f"Thank you, {st.session_state['name']}!")
        st.write(f"Your MBTI Type is: **{mbti_type}**")
        st.button('Restart', on_click = reset_app, key="clear_cache_button")
            

# Main code to show the test
def display_test():
    st.title('PERSONALITY TEST')
    formatting()
    
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
    if 'answers' not in st.session_state:
        st.session_state['answers'] = {}
    if 'current_question' not in st.session_state:
        st.session_state['current_question'] = 0
    if 'completed' not in st.session_state:
        st.session_state['completed'] = False
    if 'name' not in st.session_state:
        st.session_state['name'] = ''

    if st.session_state['name'] == '':
        st.markdown(f'<p class="question-text">Good {friendly()}. What\'s your name?</p>', unsafe_allow_html=True)
        name_input = st.text_input(f'Enter your name here: ')
        if name_input and (st.session_state['completed'] == False):
            st.session_state['name'] = name_input  # Save the name to session state
            st.rerun()  # Trigger a rerun to hide the input box
    else:
        st.write(f"Good {friendly()}, {st.session_state['name']}! Let's start your personality test!")
        set_state(2)
        test()