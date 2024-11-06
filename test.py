import streamlit as st
import sqlite3
import bcrypt

# Initialize database connection
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create a table for storing users (if not already created)
def create_user_table():
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password BLOB)''')
    conn.commit()

# Add a new user to the database with a hashed password
def add_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

# Verify if the username exists and if the password matches
def verify_user(username, password):
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result:
        stored_password = result[0]  # This is a BLOB (bytes), no need to encode
        return bcrypt.checkpw(password.encode(), stored_password)
    return False

# Display login and sign-up forms and handle authentication
def user_management():
    st.sidebar.title("User Management")

    # Display login and sign-up options
    choice = st.sidebar.selectbox("Login or Sign Up", ["Login", "Sign Up"])

    # Registration (Sign Up) Option
    if choice == "Sign Up":
        st.sidebar.subheader("Create a New Account")
        new_username = st.sidebar.text_input("Username")
        new_password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Sign Up"):
            create_user_table()
            add_user(new_username, new_password)
            st.sidebar.success("Account created successfully! You can now log in.")
    
    # Login Option
    elif choice == "Login":
        st.sidebar.subheader("Login to Your Account")
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"):
            if verify_user(username, password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.sidebar.success(f"Welcome, {username}!")
            else:
                st.sidebar.error("Username or password is incorrect")

    # Logout Option
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        if st.sidebar.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = ""
            st.sidebar.info("Logged out successfully.")

# Run user management interface
if __name__ == "__main__":
    user_management()

    # Display content only if logged in
    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        st.write(f"Welcome, {st.session_state['username']}!")
        st.write("This is a secure page accessible only to logged-in users.")
    else:
        st.write("Please log in to access this content.")