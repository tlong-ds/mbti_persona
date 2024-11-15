import streamlit as st
import streamlit.components.v1 as components

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


load_css("./style/style.css")
# HTML and JavaScript code for the button
html_code = """
<div class="stButton">
    <button id="animatedButton">Click Me
        <span></span>
        <span></span>
        <span></span>
        <span></span>
    </button>
</div>
<style>
.stButton > button {
    width: 100%;
    height: 50px;
    margin: 5px 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    border-radius: 5px;
    color: white;
    overflow: hidden;
    position: relative;
    border: 5px solid white;
    background: transparent;
    transition: all 2s ease;
}

.stButton > button span {
    position: absolute;
    content: '';
    top: calc(2em - 0.5px);
    left: 50%;
    width: 20em;
    height: 20em;
    opacity: 0.5;
    background: white;
    margin-left: -10em;
    border-radius: 42.5%;
    transform-origin: 50% 50%;
    animation: wave 5s infinite linear;
    transition: all 2s ease, top 1.5s ease;
}

.stButton > button:hover {
    color: black;
    border-color: black;
    transition: all 2s ease;
}

.stButton > button:hover span {
    opacity: 1;
    top: 0.5em;
    background-color: black;
    transition: all 2s ease, top 1.5s ease;
}

@keyframes wave {
    0% {
        transform: rotate(0deg) scale(1);
    }
    50% {
        transform: rotate(180deg) scale(0.975);
    }
    100% {
        transform: rotate(360deg) scale(1);
    }
}
</style>
<script>
document.addEventListener('DOMContentLoaded', (event) => {
    const buttons = document.querySelectorAll('.stButton > button');
    buttons.forEach(button => {
        for (let i = 0; i < 1; i++) {
            const span = document.createElement('span');
            button.appendChild(span);
        }
    });
});
</script>
"""

# Embed the HTML and JavaScript in the Streamlit app
components.html(html_code)
st.button("HI")