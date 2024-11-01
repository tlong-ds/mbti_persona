import streamlit as st

# Define CSS with two classes for clicked and unclicked buttons
st.markdown(
    """
    <style>
    .default-button {
        background-color: red !important;
        color: white !important;
    }
    .clicked-button {
        background-color: green !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for button click
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

# Choose the CSS class based on the button click state
button_class = "clicked-button" if st.session_state['button_clicked'] else "default-button"

# Display the button with custom styling
if st.button("Click me", key="my_button", help="Click to change color"):
    st.session_state['button_clicked'] = not st.session_state['button_clicked']  # Toggle the state

# Use an HTML button wrapper to apply the class
st.markdown(f'<div class="{button_class}"><button>{ "Clicked" if st.session_state["button_clicked"] else "Click me" }</button></div>', unsafe_allow_html=True)