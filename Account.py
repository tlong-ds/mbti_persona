import streamlit as st
import os
import bcrypt
import re
from datetime import date
from streamlit_extras.switch_page_button import switch_page
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure, DuplicateKeyError
from dotenv import load_dotenv

class User:
    client = None
    db = None
    users = None

    @classmethod
    def initialize_db(cls):
        if not cls.client:
            try:
                # Load environment variables
                load_dotenv()
                uri = st.secrets['MONGODB_URI'].path
                
                if not uri:
                    st.error("MongoDB URI not found")
                    return
                    
                # Add retry logic and timeout
                cls.client = MongoClient(
                    uri,
                    server_api=ServerApi('1'),
                    serverSelectionTimeoutMS=5000,
                    retryWrites=True
                )
                
                # Test connection
                cls.client.admin.command('ping')
                
                cls.db = cls.client['user_database']
                cls.users = cls.db['users']
                cls.users.create_index("username", unique=True)
                
            except ServerSelectionTimeoutError:
                st.error("Could not connect to MongoDB server")
            except OperationFailure as e:
                st.error(f"Authentication failed: {str(e)}")
            except Exception as e:
                st.error(f"Database error: {str(e)}")

    @classmethod
    def create_user_table(cls):
        cls.initialize_db()
        try:
            validator = {
                '$jsonSchema': {
                    'bsonType': 'object',
                    'required': ['username', 'password'],
                    'properties': {
                        'name': {'bsonType': 'string'},
                        'dob': {'bsonType': 'string'},
                        'gender': {'bsonType': 'string'},
                        'username': {'bsonType': 'string'},
                        'password': {'bsonType': 'string'},
                        'phone': {'bsonType': 'string'},
                        'email': {'bsonType': 'string'},
                        'ptype': {'bsonType': 'string'},
                        'status': {'bsonType': 'string'},
                        'avt': {'bsonType': 'string'}
                    }
                }
            }
            if 'users' in cls.db.list_collection_names():
                # Modify existing collection's validator
                cls.db.command({
                    'collMod': 'users',
                    'validator': validator
                })
            else:
                # Create new collection with validator
                cls.db.create_collection('users', validator=validator)

            # Create index after collection creation
            cls.users.create_index("username", unique=True)
        except Exception as e:
            st.error(f"Error creating collection: {str(e)}")
            return False
    @classmethod
    def valid_info(cls, username, phone, email):
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9]{5,}$', username):
            st.error('Invalid username format')
            return False
        if not re.match(r'^\d{10}$', phone):
            st.error('Invalid phone number format!')
            return False
        if not re.match(r'^\S+@\S+\.\S+$', email):
            st.error('Invalid email format!')
            return False
        return True
    
    @classmethod
    def valid_pass(cls, password):
        # Validate password length: at least 12 characters
        if len(password) < 8:
            st.error('Password must be at least 8 characters long!')
            return False
        # Validate password complexity
        if not re.search(r'[A-Z]', password):
            st.error('Password must contain at least one uppercase letter!')
            return False
        if not re.search(r'[a-z]', password):
            st.error('Password must contain at least one lowercase letter!')
            return False
        if not re.search(r'\d', password):
            st.error('Password must contain at least one number!')
            return False
        if not re.search(r'[^\w\s]', password):
            st.error('Password must contain at least one symbol!')
            return False
        # Validate against dictionary words and common names (simplified example)
        common_words = ['password', 'admin', 'user', 'login']
        if any(word in password.lower() for word in common_words):
            st.error('Password should not contain common words or names!')
            return False
        return True

    @classmethod
    def add_user(cls, name, dob, gender, username, password, phone, email, 
             ptype=None, status="std", 
             avt="https://static.vecteezy.com/system/resources/previews/009/292/244/non_2x/default-avatar-icon-of-social-media-user-vector.jpg"):
        cls.initialize_db()
        try:
            if User.valid_info(username, phone, email) and User.valid_pass(password):
                dob_str = dob.strftime("%Y-%m-%d") if dob else "None"
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                # Convert binary password to string
                password_str = hashed_password.decode('utf-8')
                # Ensure ptype is string if not None
                ptype_str = str(ptype) if ptype is not None else "None"
                
                user_doc = {
                    "name": name,
                    "dob": dob_str,
                    "gender": gender,
                    "username": username,
                    "password": password_str,
                    "phone": phone,
                    "email": email,
                    "ptype": ptype_str,
                    "status": status,
                    "avt": avt
                }
                cls.users.insert_one(user_doc)
                return True
            else: 
                raise Exception("Invalid information")
                return False
        except DuplicateKeyError:
            st.error("Username already exists. Please choose a different username.")
            return False
        except Exception as e:
            st.error(f"Error adding user: {str(e)}")
            return False

    @classmethod
    def change_password(cls, username, new_password):
        cls.initialize_db()
        try:
            if User.valid_pass(new_password):
                hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                password_str = hashed_password.decode('utf-8')
                cls.users.update_one(
                    {"username": username},
                    {"$set": {"password": password_str}}
                )
                return True
            else: return False
        except Exception as e:
            st.error(f"Error changing password: {str(e)}")

    @classmethod
    def change_info(cls, username, name, dob, gender, phone, email):
        cls.initialize_db()
        try:
            if User.valid_info(username, phone, email):
                dob_str = dob.strftime("%Y-%m-%d") if dob else "None"
                update_data = {
                    "name": name, "dob": dob_str, "gender": gender,
                    "phone": phone, "email": email
                }
                cls.users.update_one(
                    {"username": username},
                    {"$set": update_data}
                )
                for key, value in update_data.items():
                    st.session_state[key] = value
                return True
            else:
                return False
        except Exception as e:
            print(f"Exception occurred: {e}")
            st.error(f"Error updating info: {str(e)}")
            return False

    @classmethod
    def update_ptype(cls, username, ptype):
        cls.initialize_db()
        try:
            cls.users.update_one(
                {"username": username},
                {"$set": {"ptype": ptype}}
            )
        except Exception as e:
            st.error(f"Error updating ptype: {str(e)}")

    @classmethod
    def update_status(cls, username, status):
        cls.initialize_db()
        try:
            cls.users.update_one(
                {"username": username},
                {"$set": {"status": status}}
            )
        except Exception as e:
            st.error(f"Error updating status: {str(e)}")

    @classmethod
    def login(cls, username, password):
        cls.initialize_db()
        try:
            user = cls.users.find_one({"username": username})
            if user:
                stored_password = user['password']
                if isinstance(stored_password, str):
                    stored_password = stored_password.encode('utf-8')
                return bcrypt.checkpw(password.encode(), stored_password)
            return False
        except Exception as e:
            st.error(f"Login error: {str(e)}")
            return False

    @classmethod
    def get_user_info(cls, username):
        cls.initialize_db()
        try:
            return cls.users.find_one({"username": username})
        except Exception as e:
            st.error(f"Error fetching user info: {str(e)}")
            return None

    @classmethod
    def user_management(cls):
        cls.initialize_db()
        if "login" not in st.session_state:
            st.session_state.login = False
        
        with st.sidebar:
            if not st.session_state.get("login", False):  # Check if user is logged in
                choice = st.selectbox("Log In", ["Login", "Sign Up"])
                
                if choice == "Login":
                    username = st.text_input("Username")
                    password = st.text_input("Password", type="password")
                    if st.button("Login"):
                        if cls.login(username, password):
                            st.success("Login successful")
                            user_info = cls.get_user_info(username)
                            if user_info:  # Check if user_info is valid
                                st.session_state['name'] = user_info.get('name')
                                st.session_state['dob'] = user_info.get('dob')
                                st.session_state['gender'] = user_info.get('gender')
                                st.session_state['username'] = user_info.get('username')
                                st.session_state['phone'] = user_info.get('phone')
                                st.session_state['email'] = user_info.get('email')
                                st.session_state['ptype'] = user_info.get('ptype')
                                st.session_state['status'] = user_info.get('status')
                                st.session_state['avt'] = user_info.get('avt')
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
                        if cls.add_user(name, dob, gender, username, password, phone, email):
                            st.success("Sign up successful")
                        else:
                            st.error("Unable to sign up")
            else:
                st.markdown(f"Hello, {st.session_state['name']}.", unsafe_allow_html=True)
                st.markdown(f"Welcome to MBTI Persona!", unsafe_allow_html=True)
                if st.button("View your account"):
                    switch_page("Account")
                if st.button("Logout"):
                    # Reset session state
                    for key in ['login', 'name', 'dob', 'gender', 'username', 
                                'phone', 'email', 'ptype', 'status', 'avt']:
                        st.session_state[key] = None
                    st.session_state['login'] = False  # Explicitly set login to False
                    st.rerun()