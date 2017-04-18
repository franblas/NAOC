import sqlite3
import json

from db_utils import connect_db

def deserialize_class(res):
    if not res: return dict()
    return {
        'char_class': res[1],
        'char_class_name': res[2],
        'base': res[3],
        'profession': res[4]
    }

def create_classes_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS CLASSES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        CHAR_CLASS INTEGER NOT NULL,
        CHAR_CLASS_NAME TEXT NOT NULL,
        BASE TEXT NOT NULL,
        PROFESSION TEXT NOT NULL,
        UNIQUE(CHAR_CLASS)
       );''')
    conn.close()

def insert_all_classes():
    conn = connect_db()
    with open('data/classes.json', 'r') as f:
        classes = json.load(f)
    for c in classes:
        conn.execute('''
            INSERT INTO CLASSES (CHAR_CLASS,CHAR_CLASS_NAME,BASE,PROFESSION) \
              VALUES (?,?,?,?)''', (int(c['CharClass']),c['CharClassName'],
              c['Base'],c['Profession']))
        conn.commit()
    conn.close()

def init_classes_data():
    create_classes_table()
    insert_all_classes()

def get_class(char_class):
    res = list()
    conn = connect_db()
    cursor = conn.execute('''
        SELECT * FROM CLASSES WHERE CHAR_CLASS=?''', (char_class,))
    rep = cursor.fetchone()
    if rep: res = rep
    conn.close()
    return deserialize_class(res)
