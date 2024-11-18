import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# Specify the path to your CSV file
file_path = './p_types/type_data.csv'

# Read the CSV file
try:
    df = pd.read_csv(file_path, encoding='utf-8', index_col="type")
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding='latin-1', index_col="type")

# Display the DataFrame
text = df.iloc[1][3]

st.markdown(text, unsafe_allow_html=True)