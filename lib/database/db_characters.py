import sqlite3

from db_utils import connect_db
from db_accounts import get_id

def create_characters_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS CHARACTERS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        CREATION_DATE TIMESTAMP NOT NULL,
        CUSTOM_MODE INTEGER NOT NULL,
        EYE_SIZE INTEGER NOT NULL,
        LIP_SIZE INTEGER NOT NULL,
        EYE_COLOR INTEGER NOT NULL,
        HAIR_COLOR INTEGER NOT NULL,
        FACE_TYPE INTEGER NOT NULL,
        HAIR_STYLE INTEGER NOT NULL,
        MOOD_TYPE INTEGER NOT NULL,
        OPERATION INTEGER NOT NULL,
        UNK INTEGER NOT NULL,
        LEVEL INTEGER NOT NULL,
        CHAR_CLASS INTEGER NOT NULL,
        REALM INTEGER NOT NULL,
        RACE INTEGER NOT NULL,
        GENDER INTEGER NOT NULL,
        SHROUDED_ISLES_START_LOCATION BOOLEAN NOT NULL,
        CREATION_MODEL INTEGER NOT NULL,
        REGION INTEGER NOT NULL,
        STRENGTH INTEGER NOT NULL,
        DEXTERITY INTEGER NOT NULL,
        CONSTITUTION INTEGER NOT NULL,
        QUICKNESS INTEGER NOT NULL,
        INTELLIGENCE INTEGER NOT NULL,
        PIETY INTEGER NOT NULL,
        EMPATHY INTEGER NOT NULL,
        CHARISMA INTEGER NOT NULL,
        ACTIVE_RIGHT_SLOT INTEGER NOT NULL,
        ACTIVE_LEFT_SLOT INTEGER NOT NULL,
        SHROUDED_ISLES_ZONE INTEGER NOT NULL,
        NEW_CONSTITUTION INTEGER NOT NULL,
        ACCOUNT_SLOT INTEGER NOT NULL,
        ENDURANCE INTEGER NOT NULL,
        MAX_ENDURANCE INTEGER NOT NULL,
        CONCENTRATION INTEGER NOT NULL,
        MAX_SPEED INTEGER NOT NULL,
        LOGIN_ID INTEGER NOT NULL,
        UNIQUE(NAME)
       );''')
    conn.close()

def insert_new_character(character_data, login_name):
    login_id = get_id(login_name)

    conn = connect_db()

    dexterity = character_data["dexterity"]
    active_right_slot = character_data["active_right_slot"]
    intelligence = character_data["intelligence"]
    creation_model = character_data["creation_model"]
    custom_mode = character_data["custom_mode"]
    creation_date = character_data["creation_date"]
    account_slot = character_data["account_slot"]
    operation = character_data["operation"]
    active_left_slot = character_data["active_left_slot"]
    strength = character_data["strength"]
    realm = character_data["realm"]
    constitution = character_data["constitution"]
    endurance = character_data["endurance"]
    lip_size = character_data["lip_size"]
    concentration = character_data["concentration"]
    charisma = character_data["charisma"]
    race = character_data["race"]
    char_class = character_data["char_class"]
    mood_type = character_data["mood_type"]
    quickness = character_data["quickness"]
    eye_color = character_data["eye_color"]
    max_speed = character_data["max_speed"]
    hair_style = character_data["hair_style"]
    hair_color = character_data["hair_color"]
    face_type = character_data["face_type"]
    eye_size = character_data["eye_size"]
    empathy = character_data["empathy"]
    new_constitution = character_data["new_constitution"]
    name = character_data["name"]
    piety = character_data["piety"]
    level = character_data["level"]
    gender = character_data["gender"]
    region = character_data["region"]
    shrouded_isles_start_location = character_data["shrouded_isles_start_location"]
    shrouded_isles_zone = character_data["shrouded_isles_zone"]
    unk = character_data["unk"]
    max_endurance = character_data["max_endurance"]

    conn.execute('''
    INSERT INTO CHARACTERS (NAME,CREATION_DATE,CUSTOM_MODE,EYE_SIZE,LIP_SIZE,EYE_COLOR, \
    HAIR_COLOR,FACE_TYPE,HAIR_STYLE,MOOD_TYPE,OPERATION,UNK,LEVEL,CHAR_CLASS,REALM,RACE,GENDER, \
    SHROUDED_ISLES_START_LOCATION,CREATION_MODEL,REGION,STRENGTH,DEXTERITY,CONSTITUTION,QUICKNESS,INTELLIGENCE, \
    PIETY,EMPATHY,CHARISMA,ACTIVE_RIGHT_SLOT,ACTIVE_LEFT_SLOT,SHROUDED_ISLES_ZONE,NEW_CONSTITUTION,ACCOUNT_SLOT, \
    ENDURANCE,MAX_ENDURANCE,CONCENTRATION,MAX_SPEED,LOGIN_ID) \
      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (name,creation_date,custom_mode,eye_size,lip_size,eye_color,
      hair_color,face_type,hair_style,mood_type,operation,unk,level,char_class,realm,race,gender,
      shrouded_isles_start_location,creation_model,region,strength,dexterity,constitution,quickness,intelligence,
      piety,empathy,charisma,active_right_slot,active_left_slot,shrouded_isles_zone,new_constitution,account_slot,
      endurance,max_endurance,concentration,max_speed,login_id))
    conn.commit()
    conn.close()


def is_character_already_existing(char_name):
    already_existing = False
    conn = connect_db()
    cursor = conn.execute('''
    SELECT ID FROM CHARACTERS WHERE NAME=?''', (char_name,))
    rep = cursor.fetchone()
    if rep: already_existing = True
    conn.close()
    return already_existing

def get_characters(login_name, realm):
    characters_data = list()
    login_id = get_id(login_name)
    conn = connect_db()
    cursor = conn.execute('''
    SELECT * FROM CHARACTERS WHERE LOGIN_ID=? AND REALM=?''', (login_id,realm))
    reps = cursor.fetchall()
    data_l = [r for r in reps]
    if data_l:
        for rep in data_l:
            character_data = {
                "name": rep[1],
                "creation_date": rep[2],
                "custom_mode": rep[3],
                "eye_size": rep[4],
                "lip_size": rep[5],
                "eye_color": rep[6],
                "hair_color": rep[7],
                "face_type": rep[8],
                "hair_style": rep[9],
                "mood_type": rep[10],
                "operation": rep[11],
                "unk": rep[12],
                "level": rep[13],
                "char_class": rep[14],
                "realm": rep[15],
                "race": rep[16],
                "gender": rep[17],
                "shrouded_isles_start_location": rep[18],
                "creation_model": rep[19],
                "region": rep[20],
                "strength": rep[21],
                "dexterity": rep[22],
                "constitution": rep[23],
                "quickness": rep[24],
                "intelligence": rep[25],
                "piety": rep[26],
                "empathy": rep[27],
                "charisma": rep[28],
                "active_right_slot": rep[29],
                "active_left_slot": rep[30],
                "shrouded_isles_zone": rep[31],
                "new_constitution": rep[32],
                "account_slot": rep[33],
                "endurance": rep[34],
                "max_endurance": rep[35],
                "concentration": rep[36],
                "max_speed": rep[37]
            }
            characters_data.append(character_data)
    conn.close()
    return characters_data

def get_next_account_slot(login_name, realm):
    res = 0
    login_id = get_id(login_name)
    conn = connect_db()
    cursor = conn.execute('''
    SELECT COUNT(ID) FROM CHARACTERS WHERE LOGIN_ID=? AND REALM=?''', (login_id,realm))
    rep = cursor.fetchone()
    if rep: res = rep[0]
    conn.close()
    return res
