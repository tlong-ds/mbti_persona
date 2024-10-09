import streamlit as st
import pandas as pd

from datetime import datetime

# Import questions
with open('qsets.txt', 'r') as file:
    data = file.readlines()
list_data = [line.split(' -  ') for line in data]
questions = [{'question': line[0], 'dimension': line[1].replace('\n', '')} for line in list_data]
# Reset the page
def reset_app():
    # Clear any session state variables or reset values
    for key in st.session_state.keys():
        del st.session_state[key]
# Greeting based on real-time
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
        if 'bonus' not in st.session_state:
            st.session_state['bonus'] = 0
        q = questions[current]
        st.markdown(f"Question {current + 1} of {len(questions)}: <b>{q['question']}</b>", unsafe_allow_html=True)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.markdown('Strongly <br> Disagree', unsafe_allow_html=True)
            if st.button('', key = 'strongly disagree'):
                st.session_state['bonus'] = -2
        with col2:
            st.markdown('Disagree <br> &nbsp;', unsafe_allow_html=True)
            if st.button('', key = 'disagree'):
                st.session_state['bonus'] = -1
        with col3:
            st.markdown('Neutral <br> &nbsp;', unsafe_allow_html=True)
            if st.button(' ', key = 'neutral'):
                st.session_state['bonus'] = 0
        with col4:
            st.markdown('Agree <br> &nbsp;', unsafe_allow_html=True)
            if st.button(' ', key = 'agree'):
                st.session_state['bonus'] = 1
        with col5:
            st.markdown('Strongly <br> Agree', unsafe_allow_html=True)
            if st.button(' ', key = 'strongly agree'):
                st.session_state['bonus'] = 2
                
        st.divider()
        if st.button('Next', type = 'primary'):
            st.session_state['answers'][q["dimension"]] = st.session_state['answers'].get(q["dimension"], 0) + st.session_state['bonus']
            print(st.session_state['answers'])
            st.session_state['current_question'] += 1
            st.session_state['bonus'] = 0
            st.rerun()
    else:
        st.session_state['completed'] = True
    if st.session_state['completed'] == True:
        dimensions = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0,  'J': 0, 'P': 0}
        for dimension, score in st.session_state['answers'].items():
            dimensions[dimension] += score
        mbti_type = ""
        mbti_type += 'E' if dimensions['E'] >= dimensions['I'] else 'I'
        mbti_type += 'S' if dimensions['S'] >= dimensions['N'] else 'N'
        mbti_type += 'T' if dimensions['T'] >= dimensions['F'] else 'F'
        mbti_type += 'J' if dimensions['J'] >= dimensions['P'] else 'P'
        st.session_state.stage = 3
        return mbti_type

# Main code to show the test
def display_test():
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
    placeholder = st.empty()
    
    if 'answers' not in st.session_state:
        st.session_state['answers'] = {}
    if 'current_question' not in st.session_state:
        st.session_state['current_question'] = 0
    if 'completed' not in st.session_state:
        st.session_state['completed'] = False
    if 'name' not in st.session_state:
        st.session_state['name'] = ''
    if "stage" not in st.session_state:
        st.session_state.stage = 0
    
    if st.session_state['name'] == '':
        st.markdown(f'<p class="question-text">Good {friendly()}. What\'s your name?</p>', unsafe_allow_html=True)
        name_input = st.text_input(f'Enter your name here: ')
        if name_input and (st.session_state['completed'] == False):
            st.session_state['name'] = name_input  # Save the name to session state
            st.rerun()  # Trigger a rerun to hide the input box
    else:
        placeholder.markdown(f"""Good {friendly()}, {st.session_state['name']}! 
                             Are you ready to take your personality test? <br> 
                             There are <b>60 questions</b> in this test, 
                             and you have to answer all of them to identify your personality type. <br>
                             If you are ready, click <b>Yes</b>. Otherwise, click <b>No</b>. You can still see the test later!
                             """, unsafe_allow_html=True)
        if 'clicked' not in st.session_state:
            st.session_state.clicked = False
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
            mbti_type = test()

            if st.session_state.stage == 3:
                placeholder.write(f"Thank you, {st.session_state['name']}!")
                st.write(f"Your MBTI Type is: **{mbti_type}**")
                st.divider()
                st.write(f"Learn more about your personality: ")
                st.button('Restart', on_click = reset_app, key="retake the test")
        elif st.session_state.stage == 2:
            placeholder.write(f"It's okay. If you change your mind, you can reload the page, or press this button!")
            st.button('Restart', on_click = reset_app, key="re_entering")

    