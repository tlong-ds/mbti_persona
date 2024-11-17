import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Account import User
def draw_figure():
    percentages = st.session_state['percentages']
    dimensions = ['E/I', 'S/N', 'T/F', 'J/P']
    
    # Map dimensions to trait names
    trait_names = {
        'E/I': ('Extraverted', 'Introverted'),
        'S/N': ('Observant', 'Intuitive'),
        'T/F': ('Thinking', 'Feeling'),
        'J/P': ('Judging', 'Prospecting')
    }
    
    scores = []
    left_labels = []
    right_labels = []
    
    for dim in dimensions:
        percentage = percentages.get(dim, 0)
        scores.append(percentage)
        left_label, right_label = trait_names[dim]
        left_labels.append(left_label)
        right_labels.append(right_label)
    
    colors = ['#5DADE2', '#F4D03F', '#58D68D', '#AF7AC5']  # Custom colors
    
    fig, ax = plt.subplots(figsize=(6, 6))
    for i, (score, color) in enumerate(zip(scores, colors)):
        # Draw the bar representing the score
        ax.barh(i, score, color=color, height=0.5)
        # Draw the remaining part
        ax.barh(i, 100 - score, left=score, color='#e0e0e0', height=0.5)
        
        # Move percentage text next to the bar
        ax.text(score + 2, i, f"{int(score)}%", va='center', ha='left', color='black', fontweight='bold')
        
        # Trait labels
        ax.text(-2, i, left_labels[i], va='center', ha='right', color='black', fontweight='bold')
        ax.text(102, i, right_labels[i], va='center', ha='left', color='black', fontweight='bold')
        
    # Customize plot appearance
    ax.set_xlim(0, 110)
    ax.set_ylim(-0.5, len(scores) - 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.invert_yaxis()  # Highest trait on top
    plt.box(False)
    
    st.pyplot(fig)


questions = pd.read_csv("./p_test/qsets.tsv", sep = '\t')
type_dict = pd.read_csv("./p_test/personality_types.csv", index_col = "type")

def calculate_result():
    dimensions = {'E/I': 0, 'S/N': 0, 'T/F': 0, 'J/P': 0}
    for dimension, score in st.session_state['answers']. items ():
        dimensions[dimension] += score
        ptype = (
        ('E' if dimensions['E/I'] >= 0 else 'I') +
        ('S' if dimensions ['S/N'] >= 0 else 'N') +
        ('T' if dimensions ['T/F'] >= 0 else 'F') +
        ('J' if  dimensions ['J/P'] >= 0 else 'P')
        )
        st.session_state['ptype'] = ptype
        st.session_state.stage = 3
def display_results():
    if 'percentages' not in st.session_state:
        st.error("No results to display. Please complete the test first.")
        return
    calculate_result()
    if st.session_state.login:
        User.update_ptype(st.session_state['username'], st.session_state['ptype'])
    
    st.markdown(f"<font size = '4'>**{st.session_state["name"]}'s personality type is**</font>", unsafe_allow_html = True)
    st.markdown(F"<font size = '8'>**{st.session_state['ptype']}: {type_dict.loc[st.session_state['ptype'],"title"]}**</font>", unsafe_allow_html = True)
    st.markdown(f"<font size = '5'>{type_dict.loc[st.session_state['ptype'],"description"]} </font>", unsafe_allow_html = True)
    st.markdown(f"<font size = '4'>{type_dict.loc[st.session_state['ptype'],"percentage"]} of the population</font>", unsafe_allow_html = True)
    draw_figure()