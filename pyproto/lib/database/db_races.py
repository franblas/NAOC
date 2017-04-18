import sqlite3
import json

from db_utils import connect_db, int_or_none

def deserialize_race(res):
    if not res: return dict()
    return {
        'id': res[0],
        'name': res[1],
        'race_id': res[2],
        'resist_crush': res[3],
        'resist_natural': res[4],
        'resist_thrust': res[5],
        'resist_slash': res[6],
        'resist_spirit': res[7],
        'resist_matter': res[8],
        'resist_body': res[9],
        'resist_heat': res[10],
        'resist_energy': res[11],
        'resist_cold': res[12]
    }

def create_races_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS RACES (
        ID INTEGER PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        RACE_ID TEXT NOT NULL,
        RESIST_CRUSH INTEGER NULL,
        RESIST_NATURAL INTEGER NULL,
        RESIST_THRUST INTEGER NULL,
        RESIST_SLASH INTEGER NULL,
        RESIST_SPIRIT INTEGER NULL,
        RESIST_MATTER INTEGER NULL,
        RESIST_BODY INTEGER NULL,
        RESIST_HEAT INTEGER NULL,
        RESIST_ENERGY INTEGER NULL,
        RESIST_COLD INTEGER NULL,
        UNIQUE(ID)
       );''')
    conn.close()

def insert_all_races():
    conn = connect_db()
    with open('data/races.json', 'r') as f:
        races = json.load(f)
    for race in races:
        conn.execute('''
            INSERT INTO RACES (ID,NAME,RACE_ID,RESIST_CRUSH,RESIST_NATURAL,RESIST_THRUST,\
            RESIST_SLASH,RESIST_SPIRIT,RESIST_MATTER,RESIST_BODY,RESIST_HEAT,RESIST_ENERGY,RESIST_COLD) \
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)''', (int(race['ID']),race['Name'],race['Race_ID'],
              int_or_none(race['ResistCrush']),int_or_none(race['ResistNatural']),int_or_none(race['ResistThrust']),
              int_or_none(race['ResistSlash']),int_or_none(race['ResistSpirit']),int_or_none(race['ResistMatter']),
              int_or_none(race['ResistBody']),int_or_none(race['ResistHeat']),int_or_none(race['ResistEnergy']),int_or_none(race['ResistCold'])))
        conn.commit()
    conn.close()

def init_races_data():
    create_races_table()
    insert_all_races()

def get_race(idd):
    res = list()
    conn = connect_db()
    cursor = conn.execute('''
        SELECT * FROM RACES WHERE ID=?''', (idd,))
    rep = cursor.fetchone()
    if rep: res = rep
    conn.close()
    return deserialize_race(res)
