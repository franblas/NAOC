import sqlite3
import json

from db_utils import connect_db, int_or_none, progress_bar

def deserialize_path(res):
    if not res: return dict()
    return {
        'path_id': res[1],
        'region_id': res[2],
        'path_type': res[3]
    }

def deserialize_path_points(res):
    if not res: return dict()
    return {
        'path_id': res[1],
        'wait_time': res[2],
        'step': res[3],
        'max_speed': res[4],
        'X': res[5],
        'Y': res[6],
        'Z': res[7]
    }

def create_paths_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS PATHS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        PATH_ID TEXT NOT NULL,
        REGION_ID INTEGER NULL,
        PATH_TYPE INTEGER NOT NULL,
        UNIQUE(PATH_ID)
       );''')
    conn.close()

def create_paths_points_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS PATHS_POINTS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        PATH_ID TEXT NOT NULL,
        WAIT_TIME INTEGER NULL,
        STEP INTEGER NULL,
        MAX_SPEED INTEGER NOT NULL,
        X INTEGER NOT NULL,
        Y INTEGER NOT NULL,
        Z INTEGER NOT NULL,
        UNIQUE(ID)
       );''')
    conn.close()

def insert_all_paths():
    conn = connect_db()
    with open('data/paths.json', 'r') as f:
        paths = json.load(f)
    for p in paths:
        conn.execute('''
            INSERT INTO PATHS (PATH_ID,REGION_ID,PATH_TYPE) \
              VALUES (?,?,?)''', (p['PathID'],int_or_none(p['RegionID']),
              int(p['PathType'])))
        conn.commit()
    conn.close()

def insert_all_paths_points():
    conn = connect_db()
    with open('data/path_points.json', 'r') as f:
        paths_points = json.load(f)
    pb = progress_bar()
    for pp in pb(paths_points):
        conn.execute('''
            INSERT INTO PATHS_POINTS (PATH_ID,WAIT_TIME,STEP, \
            MAX_SPEED,X,Y,Z) \
                VALUES (?,?,?,?,?,?,?)''', (pp['PathID'],int_or_none(pp['WaitTime']),
                int_or_none(pp['Step']),int(pp['MaxSpeed']),int(pp['X']),int(pp['Y']),
                int(pp['Z'])))
        conn.commit()
    conn.close()

def init_paths_and_points_data():
    create_paths_table()
    create_paths_points_table()
    insert_all_paths()
    insert_all_paths_points()
