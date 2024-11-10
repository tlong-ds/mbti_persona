import streamlit as st
import os
import sqlite3
import bcrypt
from datetime import date

class User:  
    db_path = os.path.join(os.path.dirname(__file__), 'users.db')
    """
        This module is used to manage user accounts.
        It provides methods to create a user table, add a user, change a user's password, and login.
        It also provides methods to get user information and manage user accounts.
    """

    @staticmethod
    def create_user_table():
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            dob TEXT,
            username TEXT PRIMARY KEY,
            password BLOB,
            phone TEXT,
            email TEXT,
            ptype TEXT
        )
        ''')
        conn.commit()
        conn.close()

    @staticmethod
    def add_user(name, dob, username, password, phone, email, ptype = None):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        c.execute("INSERT INTO users (name, dob, username, password, phone, email, ptype) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, dob, username, hashed_password, phone, email, ptype))
        conn.commit()
        conn.close()
        
    
    @staticmethod
    def change_password(username, new_password):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        hashed_password = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt())
        c.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password, username))
        conn.commit()
        conn.close()

    @staticmethod
    def login(username, password):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        conn.close()
        if result:
            stored_password = result[0]
            return bcrypt.checkpw(password.encode(), stored_password)
        return False
    
    @staticmethod
    def get_user_info(username):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        c.execute("SELECT name, dob, phone, email, ptype FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        conn.close()
        return result

    
    @staticmethod
    def user_management():
        with st.sidebar:
            if not st.session_state.login:
                choice = st.selectbox("Log In", ["Login", "Sign Up"])
                if choice == "Login":
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    if st.button("Login"):
                        if User.login(username, password):
                            st.success("Login successful")
                            user_info = User.get_user_info(username)
                            st.session_state['name'] = user_info[0]
                            st.session_state['dob'] = user_info[1]
                            st.session_state['phone'] = user_info[2]
                            st.session_state['email'] = user_info[3]
                            st.session_state['ptype'] = user_info[4]
                            st.session_state.login = True
                            st.rerun()
                        else:
                            st.error("Login failed")
                elif choice == "Sign Up":
                    name = st.text_input("Name")
                    dob = st.date_input(
                        "Date of Birth",
                        min_value=date(1900, 1, 1),
                        max_value=date.today(),         
                        value=date(2000, 1, 1)
                    )
                    email = st.text_input("Email")
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    phone = st.text_input("Phone")
                    if st.button("Sign Up"):
                        User.add_user(name, dob, username, password, phone, email)
                        st.success("Sign up successful")
            else:
                st.markdown(f"Welcome, {st.session_state['name']}", unsafe_allow_html=True)

                
                if st.button("Logout"):
                    st.session_state.login = False
                    st.rerun()