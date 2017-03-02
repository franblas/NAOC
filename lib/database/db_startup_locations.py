import sqlite3
import json

from db_utils import connect_db

def deserialize_startup_location(res):
    if not res: return dict()
    return {
      'class_id': res[1],
      'client_region_id': res[2],
      'x_pos': res[3],
      "y_pos": res[4],
      "z_pos": res[5],
      "heading": res[6],
      "race_id": res[7],
      "region": res[8],
      "realm_id": res[9],
      "min_version": res[10]
    }


def create_startup_locations_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS STARTUP_LOCATIONS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        CLASS_ID INTEGER NOT NULL,
        CLIENT_REGION_ID INTEGER NOT NULL,
        X_POS INTEGER NOT NULL,
        Y_POS INTEGER NOT NULL,
        Z_POS INTEGER NOT NULL,
        HEADING INTEGER NOT NULL,
        RACE_ID INTEGER NOT NULL,
        REGION INTEGER NOT NULL,
        REALM_ID INTEGER NOT NULL,
        MIN_VERSION INTEGER NOT NULL,
        UNIQUE(ID)
       );''')
    conn.close()

def insert_all_startup_locations():
    conn = connect_db()
    with open('data/startup_locations.json', 'r') as f:
        startup_locations = json.load(f).get('startup_locations')
    for loc in startup_locations:
        conn.execute('''
            INSERT INTO STARTUP_LOCATIONS (CLASS_ID,CLIENT_REGION_ID,X_POS,Y_POS,Z_POS,HEADING,\
            RACE_ID,REGION,REALM_ID,MIN_VERSION) \
              VALUES (?,?,?,?,?,?,?,?,?,?)''', (loc['ClassID'],loc['ClientRegionID'],loc['XPos'],loc['YPos'],
              loc['ZPos'],loc['Heading'],loc['RaceID'],loc['Region'],loc['RealmID'],loc['MinVersion']))
        conn.commit()
    conn.close()

def init_startup_locations_data():
    create_startup_locations_table()
    insert_all_startup_locations()

def get_startup_location(region_id, realm_id):
    res = list()
    conn = connect_db()
    cursor = conn.execute('''
        SELECT * FROM STARTUP_LOCATIONS WHERE REGION=? AND REALM_ID=?''', (region_id,realm_id))
    rep = cursor.fetchone()
    if rep: res = rep
    conn.close()
    return deserialize_startup_location(res)
