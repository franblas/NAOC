import sqlite3

DB_NAME = 'naoc.db'

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn

def str_to_bool(s):
    if not s: return s
    formated_s = s.lower()
    if formated_s == 'false': return False
    elif formated_s == 'true': return True
    else: return

def int_or_none(i):
    if not i: return i
    return int(i)
