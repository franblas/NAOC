import sqlite3
import json

from db_utils import connect_db, str_to_bool

def deserialize_region(res):
    if not res: return dict()
    return {
        'name': res[1],
        'ip': res[2],
        'housing_enabled': res[3],
        'region_id': res[4],
        'is_frontier': res[5],
        'expansion': res[6],
        'water_level': res[7],
        'diving_enabled': res[8],
        'port': res[9],
        'description': res[10]
    }

def create_regions_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS REGIONS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        IP TEXT NOT NULL,
        HOUSING_ENABLED BOOLEAN NOT NULL,
        REGION_ID INTEGER NOT NULL,
        IS_FRONTIER BOOLEAN NOT NULL,
        EXPANSION INTEGER NOT NULL,
        WATER_LEVEL INTEGER NOT NULL,
        DIVING_ENABLED BOOLEAN NOT NULL,
        PORT INTEGER NOT NULL,
        DESCRIPTION TEXT NOT NULL,
        UNIQUE(NAME)
       );''')
    conn.close()

def insert_all_regions():
    conn = connect_db()
    with open('data/regions.json', 'r') as f:
        regions = json.load(f).get('regions')
    for region in regions:
        conn.execute('''
            INSERT INTO REGIONS (NAME,IP,HOUSING_ENABLED,REGION_ID,IS_FRONTIER,EXPANSION,\
            WATER_LEVEL,DIVING_ENABLED,PORT,DESCRIPTION) \
              VALUES (?,?,?,?,?,?,?,?,?,?)''', (region['Name'], region['IP'], str_to_bool(region['HousingEnabled']),
              int(region['RegionID']),str_to_bool(region['IsFrontier']),int(region['Expansion']),int(region['WaterLevel']),
              str_to_bool(region['DivingEnabled']),int(region['Port']),region['Description'] ))
        conn.commit()
    conn.close()

def init_regions_data():
    create_regions_table()
    insert_all_regions()

def get_region(region_id):
    res = list()
    conn = connect_db()
    cursor = conn.execute('''
        SELECT * FROM REGIONS WHERE REGION_ID=?''', (region_id,))
    rep = cursor.fetchone()
    if rep: res = rep
    conn.close()
    return deserialize_region(res)
