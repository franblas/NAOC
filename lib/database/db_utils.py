import sqlite3

DB_NAME = 'pydol.db'

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn
