import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class Result:
    dimensions = {'E/I': 0, 'S/N': 0, 'T/F': 0, 'J/P': 0}
    @staticmethod
    def calculate_result():
        
        for dimension, score in st.session_state['answers'].items():
            Result.dimensions[dimension] += score
        
        mbti_type = (
            ('E' if Result.dimensions['E/I'] >= 0 else 'I') +
            ('S' if Result.dimensions['S/N'] >= 0 else 'N') +
            ('T' if Result.dimensions['T/F'] >= 0 else 'F') +
            ('J' if Result.dimensions['J/P'] >= 0 else 'P')
        )
        
        st.session_state['mbti_type'] = mbti_type
        st.session_state.stage = 3
    @staticmethod
    @st.cache_data
    def display_result():
        Result.calculate_result()
        st.write(f"Your personality type is: **{st.session_state['mbti_type']}**")
        st.markdown(f'[Click here to learn more about your personality type](https://www.16personalities.com/{st.session_state['mbti_type']}-personality)', unsafe_allow_html=True) 
        s
        # Result.save_responses()
"""
    @staticmethod
    @st.cache_data
    def save_responses():
        responses_df = pd.DataFrame(st.session_state['answers'].items(), columns=['Dimension', 'Score'])
        st.download_button(
            label="Download CSV",
            data=responses_df.to_csv(index=False),
            file_name = f"{st.session_state['name']}_responses.csv",
            mime="text/csv"
        )
"""