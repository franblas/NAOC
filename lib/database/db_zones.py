import sqlite3
import json

from db_utils import connect_db, str_to_bool

def deserialize_zone(res):
    if not res: return dict()
    return {
        'name': res[1],
        'is_lava': res[2],
        'coin': res[3],
        'region_id': res[4],
        'realm_pts': res[5],
        'offset_x': res[6],
        'offset_y': res[7],
        'diving_flag': res[8],
        'experience': res[9],
        'width': res[10],
        'height': res[11],
        'water_level': res[12],
        'bounty_pts': res[13],
        'realm': res[14],
        'zone_id': res[15]
    }

def create_zones_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS ZONES (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        IS_LAVA BOOLEAN NOT NULL,
        COIN INTEGER NOT NULL,
        REGION_ID INTEGER NOT NULL,
        REALM_PTS INTEGER NOT NULL,
        OFFSET_X INTEGER NOT NULL,
        OFFSET_Y INTEGER NOT NULL,
        DIVING_FLAG INTEGER NOT NULL,
        EXPERIENCE INTEGER NOT NULL,
        WIDTH INTEGER NOT NULL,
        HEIGHT INTEGER NOT NULL,
        WATER_LEVEL INTEGER NOT NULL,
        BOUNTY_PTS INTEGER NOT NULL,
        REALM INTEGER NOT NULL,
        ZONE_ID INTEGER NOT NULL,
        UNIQUE(ID)
       );''')
    conn.close()

def insert_all_zones():
    conn = connect_db()
    with open('data/zones.json', 'r') as f:
        zones = json.load(f).get('zones')
    for zone in zones:
        conn.execute('''
            INSERT INTO ZONES (NAME,IS_LAVA,COIN,REGION_ID,REALM_PTS,OFFSET_X,\
            OFFSET_Y,DIVING_FLAG,EXPERIENCE,WIDTH,HEIGHT,WATER_LEVEL,BOUNTY_PTS,REALM,ZONE_ID) \
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (zone['Name'],str_to_bool(zone['IsLava']),
              int(zone['Coin']),int(zone['RegionID']),int(zone['Realmpoints']),int(zone['OffsetX']),
              int(zone['OffsetY']),int(zone['DivingFlag']),int(zone['Experience']),int(zone['Width']),
              int(zone['Height']),int(zone['WaterLevel']),int(zone['Bountypoints']),int(zone['Realm']),
              int(zone['ZoneID'])))
        conn.commit()
    conn.close()

def init_zones_data():
    create_zones_table()
    insert_all_zones()

def get_zone(zone_id):
    res = list()
    conn = connect_db()
    cursor = conn.execute('''
        SELECT * FROM ZONES WHERE ZONE_ID=?''', (zone_id,))
    rep = cursor.fetchone()
    if rep: res = rep
    conn.close()
    return deserialize_zone(res)
