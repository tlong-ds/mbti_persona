import streamlit as st
import os
import sqlite3
import bcrypt

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
            gender TEXT,
            username TEXT PRIMARY KEY,
            password TEXT, -- or BLOB if storing bytes
            phone TEXT,
            email TEXT,
            ptype TEXT,
            status TEXT,
            avt TEXT
        )
        ''')
        conn.commit()
        conn.close()

    """
    user attributes:
    - name
    - dob
    - gender
    - username
    - password
    - phone
    - email
    - ptype = "none", x in ["ISTJ", "ISTP", "ISFJ", "ISFP", "INTJ", "INTP", "INFJ", "INFP", "ESTJ", "ESTP", "ESFJ", "ESFP", "ENTJ", "ENTP", "ENFJ", "ENFP"]
    - status = "std", "pro"
    - avt = "default.jpg"
    """

    
    @staticmethod
    def add_user(name, dob, gender, username, password, phone, email, ptype = None, status = "std", avt = "https://static.vecteezy.com/system/resources/previews/009/292/244/non_2x/default-avatar-icon-of-social-media-user-vector.jpg"):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashed_password_str = hashed_password.decode('utf-8')
        c.execute("INSERT INTO users (name, dob, gender, username, password, phone, email, ptype, status, avt) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, dob, gender, username, hashed_password_str, phone, email, ptype, status, avt))
        conn.commit()
        conn.close()

    
    @staticmethod
    def change_password(username, new_password):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        # Hash the new password
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        # If necessary, decode to string before storing
        hashed_password_str = hashed_password.decode('utf-8')
        c.execute("UPDATE users SET password = ? WHERE username = ?", (hashed_password_str, username))
        conn.commit()
        conn.close()
    
    @staticmethod
    def change_info(username, name, dob, gender, phone, email, avt):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        c.execute("UPDATE users SET name = ?, dob = ?, gender = ?, phone = ?, email = ?, avt = ? WHERE username = ?", (name, dob, gender, phone, email, avt, username))
        st.session_state.name = name
        st.session_state.dob = dob
        st.session_state.gender = gender
        st.session_state.email = email
        st.session_state.phone = phone
        st.session_state.avt = avt
        conn.commit()
        conn.close()
    
    @staticmethod
    def update_ptype(username, ptype):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        c.execute("UPDATE users SET ptype = ? WHERE username = ?", (ptype, username))
        conn.commit()
        conn.close()
    
    @staticmethod
    def update_status(username, status):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        c.execute("UPDATE users SET status = ? WHERE username = ?", (status, username))
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
            if isinstance(stored_password, str):
                stored_password = stored_password.encode('utf-8')
            return bcrypt.checkpw(password.encode(), stored_password)
        return False
    

    @staticmethod
    def get_user_info(username):
        conn = sqlite3.connect(User.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        conn.close()
        return result

    
    @staticmethod
    def user_management():
        if "login" not in st.session_state:
            st.session_state.login = False
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
                            st.session_state['gender'] = user_info[2]
                            st.session_state['username'] = user_info[3]
                            st.session_state['phone'] = user_info[5]
                            st.session_state['email'] = user_info[6]
                            st.session_state['ptype'] = user_info[7]
                            st.session_state['status'] = user_info[8]
                            st.session_state['avt'] = user_info[9]
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
                    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                    email = st.text_input("Email")
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    phone = st.text_input("Phone")
                    if st.button("Sign Up"):
                        User.add_user(name, dob, gender, username, password, phone, email)
                        st.success("Sign up successful")
            else:
                st.markdown(f"Hello, {st.session_state['name']}.", unsafe_allow_html=True)
                st.markdown(f"Welcome to MBTI Persona!", unsafe_allow_html=True)
                if st.button("Logout"):
                    st.session_state.login = False
                    st.session_state['name'] = None
                    st.session_state['dob'] = None
                    st.session_state['gender'] = None
                    st.session_state['username'] = None
                    st.session_state['phone'] = None
                    st.session_state['email'] = None
                    st.session_state['ptype'] = None
                    st.session_state['status'] = None
                    st.session_state['avt'] = None
                    st.rerun()