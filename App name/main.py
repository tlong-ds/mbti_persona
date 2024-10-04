import streamlit as st
from streamlit_option_menu import option_menu as opts
import base64
import webbrowser
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    load_css()
    st.title('Personality')
    st.write("by nong")
    with st.sidebar:
        selected = opts(
            menu_title = None,
            options = ['Home', 'Personality Test', 'Personality Types', 'Languages', 'Contact Us'],
            icons = ['house', 'person', 'star', 'info-circle', 'envelope'],
            default_index=0,
            styles={"container": {"padding": "0!important", "background-color": "#0d0c0c"},
                    "icon": {"color": "white", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "15px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#ffe8e8",
                    },
                "nav-link-selected": {"background-color": "pink"},
            }
        )
if __name__ == "__main__":
    main()