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
    
    st.markdown("""
    <style>
    .stButton > button {
        padding: 20px 20px !important;
        border-radius: 8px !important;
    }
    .stButton > button:hover {
        background-color: #ffb8e2 !important; /* Darker green on hover */
    }
    </style>
""", unsafe_allow_html=True)

    if st.session_state['current_question'] < len(questions):
        current = st.session_state['current_question']
        if 'bonus' not in st.session_state:
            st.session_state['bonus'] = 0
        q = questions[current]
        st.write(f"Question {current + 1} of {len(questions)}: {q['question']}")
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            if st.button(' ', key = 'strongly disagree'):
                st.write('Strongly Disagree')
                st.session_state['bonus'] = -2
        with col2:
            if st.button(' ', key = 'disagree'):
                st.write('Disagree')
                st.session_state['bonus'] = -1
        with col3:
            if st.button(' ', key = 'neutral'):
                st.write('Neutral')
                st.session_state['bonus'] = 0
        with col4:
            if st.button(' ', key = 'agree'):
                st.write('Agree')
                st.session_state['bonus'] = 1
        with col5:
            if st.button(' ', key = 'strongly agree'):
                st.write('Strongly Agree')
                st.session_state['bonus'] = 2
                
        st.divider()
        if st.button('Next', type = 'primary'):
            print('In progress')
            st.session_state['answers'][q["dimension"]] = st.session_state['answers'].get(q["dimension"], 0) + st.session_state['bonus']
            print(st.session_state['answers'])
            st.session_state['current_question'] += 1
            st.session_state['bonus'] = 0
            st.rerun()
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
    placeholder = st.empty()
    
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

def main():
    display_test()

if __name__ == "__main__":
    main()