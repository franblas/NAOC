import sqlite3
import arrow

from db_utils import connect_db

def create_accounts_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS ACCOUNTS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        CREATIONDATE TIMESTAMP NOT NULL,
        UNIQUE(NAME)
       );''')
    conn.close()

def insert_new_account(name, password):
    conn = connect_db()
    conn.execute('''
    INSERT INTO ACCOUNTS (NAME,PASSWORD,CREATIONDATE) \
      VALUES (?,?,?)''', (name, password, arrow.now().datetime))
    conn.commit()
    conn.close()

def is_account_and_password_correct(name, password):
    correct_account = False
    conn = connect_db()
    cursor = conn.execute('''
    SELECT ID FROM ACCOUNTS WHERE NAME=? AND PASSWORD=?''', (name, password))
    res = cursor.fetchone()
    if res: correct_account = True
    conn.close()
    return correct_account

def get_id(name):
    res = -1
    conn = connect_db()
    cursor = conn.execute('''
    SELECT ID FROM ACCOUNTS WHERE NAME=?''', (name,))
    rep = cursor.fetchone()
    if rep: res = rep[0]
    conn.close()
    return res
