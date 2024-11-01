import streamlit as st
import numpy as np
import pandas as pd

def test():
    if 'mbti_type' not in st.session_state:
        st.session_state['mbti_type'] = None
    if 'answers' not in st.session_state:
        st.session_state['answers'] = {}
    if 'completed' not in st.session_state:
        st.session_state['completed'] = False

    questions = pd.read_csv('./p_test/qsets.tsv', sep='\t')
    for i, q in questions.iterrows():
        st.divider()
        st.markdown(f"Question {i + 1} of {len(questions)}: <b>{q['question']}</b>", unsafe_allow_html=True)
        
        # Radio buttons for each answer option
        response = st.radio(
            label="Select an option:",
            options=["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"],
            index = 2,
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
        
    # Calculate MBTI type if completed
    if st.button('Submit', type='primary'):
        st.session_state['completed'] = True
        return
    
    