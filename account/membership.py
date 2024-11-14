import streamlit as st
from Account import User

def process_payment():
    User.update_status(st.session_state.username, "premium")
    st.session_state.status = "premium"  # Update session state status
    st.session_state.view = "membership"  # Redirect to membership view
    st.success("You have successfully become a premium member!")

def ads_premium():
    with st.form(key = 'premium'):
        st.subheader("Join Premium MBTI Test, Unlock Your Full Potential!")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            st.write("""We believe that everyone has the potential to be great.
            By joining premium, you will unlock the full potential of your MBTI test, 
            and get access to exclusive features.""")
        with col2:
            st.write("""The freemium suite only gives you a glimpse of your personality.
            Meanwhile, the premium suite will give you a detailed analysis of your personality,
            and other aspects beyond the personality.
            """)
        with col3:
            st.write("""With premium, you will also get access to our exclusive community, 
            including experts in psychology to deepen your understanding of your personality.""")
        st.subheader("Pricing: ONLY $10, one-time payment!")
        st.markdown(f"""We believe that good stuff does not need to be expensive.
            But we do believe that good stuff should be widespread to everyone.
        """, unsafe_allow_html=True)
        st.form_submit_button('Sound Good!', on_click=process_payment)

def cancel_membership():
    User.update_status(st.session_state.username, "std")
    st.session_state.status = "std"
    st.success("You have successfully canceled your premium membership!")
    
def display_membership():
    st.header("Membership")
    if st.session_state.view == "membership":
        with st.form(key = 'member'):
            stat = "Freemium ❤️" if st.session_state.status == "std" else "Premium 💛"
            st.write(f"Your plan: {stat} ")
            if st.session_state.status == "std":
                st.write("Unlock more features by becoming a premium member!")
                if st.form_submit_button('Become a member'):
                    st.session_state.view = "premium"
            else:
                st.write("Thank you for being a premium member!")
                st.form_submit_button('Cancel membership', on_click=cancel_membership)
                    
    if st.session_state.view == "premium":
        ads_premium()