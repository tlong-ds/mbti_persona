import streamlit as at
import sqlite3
import bcrypt
from Modules import BackgroundHandler

BackgroundHandler.set_background("./home/Background.webp")
class Account:  
    conn = sqlite3.connect('./account/users.db')
    c = conn.cursor()

    @staticmethod
    def create_user_table():
        Account.c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password BLOB)''')
        Account.conn.commit()

    @staticmethod
    def add_user(username, password):
        hashed_password = bcrypt.hashpw(password.encode(), bcrpyt)
    