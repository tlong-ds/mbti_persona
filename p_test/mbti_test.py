import streamlit as st
import pandas as pd

def test():
    if 'answers' not in st.session_state:
        st.session_state['answers'] = {}
    if 'agree_counts' not in st.session_state:
        st.session_state['agree_counts'] = {}
    if 'total_counts' not in st.session_state:
        st.session_state['total_counts'] = {}
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
        dimension = q["dimension"]
        st.session_state['answers'][dimension] = st.session_state['answers'].get(dimension, 0) + score_map[response]

        if response in ["Agree", "Strongly Agree"]:
            st.session_state['agree_counts'][dimension] = st.session_state['agree_counts'].get(dimension, 0) + 1
        
        # Total questions per dimension
        st.session_state['total_counts'][dimension] = st.session_state['total_counts'].get(dimension, 0) + 1

    # Calculate MBTI type if completed
    if st.button('Submit', type='primary'):
        st.session_state['completed'] = True
        st.session_state['percentages'] = {}
        for dim in st.session_state['total_counts']:
            agree_count = st.session_state['agree_counts'].get(dim, 0)
            total_count = st.session_state['total_counts'][dim]
            percentage = (agree_count / total_count) * 100
            st.session_state['percentages'][dim] = percentage
        st.session_state.stage = 3
        return
    
    