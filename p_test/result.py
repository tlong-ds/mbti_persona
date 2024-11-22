import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import matplotlib.pyplot as plt
from Account import User
from fpdf import FPDF
from PIL import Image
import os

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
    
    fig, ax = plt.subplots(figsize=(10, 6))
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
    plt.savefig("./p_test/graph.jpg")

def create_pdf():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", style = "B", size=16)
        pdf.cell(0, 10, "MBTI Persona - Reveal Your Inner Body", ln=True, align='C')  # Title in center

        pdf.set_font("Arial", style = "B", size=13)
        pdf.cell(0, 10, "Your information: ", ln = True, align="L")
        pdf.set_font("Arial", size=11)
        pdf.cell(0, 10,  f"Name: {st.session_state.name}", ln = True, align="L")
        pdf.cell(0, 10,  f"Day of Birth: {st.session_state.dob}", ln = True, align = "L")
        pdf.cell(0, 10,  f"Gender: {st.session_state.gender}", ln = True, align = "L")
        pdf.set_font("Arial", size=15, style = "B")
        pdf.cell(0, 10, f"{st.session_state.ptype}: {data.loc[st.session_state.ptype, 'title']}", ln = True, align="L")
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10,  f"{data.loc[st.session_state.ptype, 'description']}", ln = True, align="L")
        pdf.cell(0, 10,  f"{data.loc[st.session_state.ptype, 'percentage']} of the population", ln = True, align = "L")
        image_path = "./p_test/graph.jpg"
        with Image.open(image_path) as img:
            img_width, img_height = img.size  # Get the original dimensions of the image

        # Calculate dimensions to fit the page while maintaining aspect ratio
        page_width = pdf.w - 20  # Subtracting left and right margins
        page_height = pdf.h - 100  # Subtracting top and bottom margins for text space
        aspect_ratio = img_width / img_height

        if page_width / aspect_ratio <= page_height:
            img_w = page_width
            img_h = page_width / aspect_ratio
        else:
            img_h = page_height
            img_w = page_height * aspect_ratio

        # Center the image on the page
        x = (pdf.w - img_w) / 2
        y = pdf.get_y() # Current Y position plus a small margin

        pdf.image(image_path, x=x, y=y, w=img_w, h=img_h)
        caption = "Graph: Personality Distribution"
        pdf.set_font("Arial", size=10, style="I")  # Italic font for the caption
        pdf.cell(0, 10, caption, ln=True, align="C")
        # Return the PDF as a downloadable object
        return pdf.output(dest="S").encode("latin1")


questions = pd.read_csv("./p_test/qsets.tsv", sep = '\t')
data = pd.read_csv("./p_types/type_data.csv", index_col = "type")

def calculate_result():
    dimensions = {'E/I': 0, 'S/N': 0, 'T/F': 0, 'J/P': 0}
    for dimension, score in st.session_state['answers'].items():
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
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(
        f"<font size='4'>**{st.session_state.name}'s personality type is**</font>",
        unsafe_allow_html=True
        )
        st.markdown(
            f"<font size='8'>**{st.session_state.ptype}: {data.loc[st.session_state.ptype, 'title']}**</font>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<font size='5'>{data.loc[st.session_state.ptype, 'description']}</font>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"<font size='4'>{data.loc[st.session_state.ptype, 'percentage']} of the population</font>",
            unsafe_allow_html=True
        )
    with col2:
        draw_figure()
    if st.session_state.login:
        col_1, col_2, col_3, col_4 = st.columns(4)
        with col_2:
            if st.button("Learn More"):
                switch_page("Personality Types")
        with col_3:
            pdf_data = create_pdf()
            st.download_button(
            label="Download PDF", 
            data=pdf_data, 
            file_name="results.pdf", 
            mime="application/pdf")