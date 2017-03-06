import sqlite3
import json

import progressbar

from db_utils import connect_db, str_to_bool, int_or_none

# {
#   # "Strength": 30,
#   # "Constitution": 30,
#   # "PackageID": "Public_DB",
#   # "TranslationId": "",
#   # "Speed": 200,
#   # "Quickness": 30,
#   # "AggroRange": 40,
#   # "Guild": "",
#   # "Level": 5,
#   # "RespawnInterval": null,
#   # "Region": 27,
#   # "Mob_ID": "0010f155-304f-4e5c-abb3-4bbc17cc106f",
#   # "X": 94624,
#   # "Z": 5157,
#   # "Heading": 3353,
#   # "Dexterity": 30,
#   # "BodyType": null,
#   # "Suffix": "",
#   "ClassType": "DOL.GS.GameNPC",
#   # "MessageArticle": "",
#   # "FactionID": null,
#   "HouseNumber": null,
#   # "Size": 48,
#   # "Realm": 1,
#   "ItemsListTemplateID": "",
#   # "Charisma": 30,
#   # "LastTimeRowUpdated": "2000-01-01 00:00:00",
#   "OwnerID": "",
#   # "AggroLevel": 5,
#   # "Empathy": 30,
#   # "Name": "Lumberjack",
#   # "Piety": 30,
#   "Gender": null,
#   # "ExamineArticle": "",
#   "EquipmentTemplateID": "22656309-a1ad-4d59-92e3-cfb64a964250",
#   # "MeleeDamageType": 2,
#   # "Race": null,
#   # "Flags": null,
#   # "VisibleWeaponSlots": null,
#   # "Y": 79130,
#   # "Model": 2017,
#   # "NPCTemplateID": 60163474,
#   # "RoamingRange": null,
#   # "Intelligence": 30,
#   "Brain": "",
#   "PathID": "",
#   # "IsCloakHoodUp": null,
#   # "MaxDistance": null
# }

def deserialize_mob(res):
    if not res: return dict()
    return {
        'object_id': res[0],
        'name': res[1],
        'strength': res[2],
        'quickness': res[3],
        'dexterity': res[4],
        'charisma': res[5],
        'intelligence': res[6],
        'empathy': res[7],
        'piety': res[8],
        'constitution': res[9],
        'speed': res[10],
        'aggro_range': res[11],
        'aggro_level': res[12],
        'guild': res[13],
        'level': res[14],
        'respawn_interval': res[15],
        'region': res[16],
        'X': res[17],
        'Y': res[18],
        'Z': res[19],
        'heading': res[20],
        'size': res[21],
        'realm': res[22],
        'model': res[23],
        'npc_template_id': res[24],
        'flags': res[25],
        'faction_id': res[26],
        'body_type': res[27],
        'melee_damage_type': res[28],
        'race': res[29],
        'visible_weapon_slots': res[30],
        'max_distance': res[31],
        'roaming_range': res[32],
        'is_cloak_hood_up': res[33],
        'suffix': res[34],
        'message_article': res[35],
        'examine_article': res[36],
        'inventory': { 'visible_items': [] },
        'object_type': 'npc',
        'eflags': {
            'ghost': 0x01,
            'stealth': 0x02,
            'dont_show_name': 0x04,
            'cant_target': 0x08,
            'peace': 0x10,
            'flying': 0x20,
            'torch': 0x40,
            'statue': 0x80,
            'swimming': 0x100
        }
    }

def create_mobs_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS MOBS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        NAME TEXT NOT NULL,
        STRENGTH INTEGER NULL,
        QUICKNESS INTEGER NULL,
        DEXTERITY INTEGER NULL,
        CHARISMA INTEGER NULL,
        INTELLIGENCE INTEGER NULL,
        EMPATHY INTEGER NULL,
        PIETY INTEGER NULL,
        CONSTITUTION INTEGER NULL,
        SPEED INTEGER NULL,
        AGGRO_RANGE INTEGER NULL,
        AGGRO_LEVEL INTEGER NULL,
        GUILD TEXT NOT NULL,
        LEVEL INTEGER NULL,
        RESPAWN_INTERVAL INTEGER NULL,
        REGION INTEGER NOT NULL,
        X INTEGER NULL,
        Y INTEGER NULL,
        Z INTEGER NULL,
        HEADING INTEGER NULL,
        SIZE INTEGER NULL,
        REALM INTEGER NULL,
        MODEL INTEGER NULL,
        NPC_TEMPLATE_ID INTEGER NULL,
        FLAGS INTEGER NULL,
        FACTION_ID INTEGER NULL,
        BODY_TYPE INTEGER NULL,
        MELEE_DAMAGE_TYPE INTEGER NULL,
        RACE INTEGER NULL,
        VISIBLE_WEAPON_SLOTS INTEGER NULL,
        MAX_DISTANCE INTEGER NULL,
        ROAMING_RANGE INTEGER NULL,
        IS_CLOAK_HOOD_UP INTEGER NULL,
        SUFFIX TEXT NOT NULL,
        MESSAGE_ARTICLE TEXT NOT NULL,
        EXAMINE_ARTICLE TEXT NOT NULL,
        UNIQUE(ID)
       );''')
    conn.close()

def insert_all_mobs():
    conn = connect_db()
    mobs = list()
    for path in ['data/mobs.json', 'data/mobs_2.json']:
        with open(path, 'r') as f:
            mobs += json.load(f)
    progress = progressbar.ProgressBar()
    for mob in progress(mobs):
        conn.execute('''
            INSERT INTO MOBS (NAME,STRENGTH,QUICKNESS,DEXTERITY,CHARISMA,INTELLIGENCE,EMPATHY,PIETY,CONSTITUTION, \
            SPEED,AGGRO_RANGE,AGGRO_LEVEL,GUILD,LEVEL,RESPAWN_INTERVAL,REGION, \
            X,Y,Z,HEADING,SIZE,REALM,MODEL,NPC_TEMPLATE_ID,FLAGS,FACTION_ID,BODY_TYPE, \
            MELEE_DAMAGE_TYPE,RACE,VISIBLE_WEAPON_SLOTS,MAX_DISTANCE,ROAMING_RANGE,IS_CLOAK_HOOD_UP, \
            SUFFIX,MESSAGE_ARTICLE,EXAMINE_ARTICLE) \
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (mob['Name'],
              int_or_none(mob['Strength']),int_or_none(mob['Quickness']),int_or_none(mob['Dexterity']),int_or_none(mob['Charisma']),int_or_none(mob['Intelligence']),int_or_none(mob['Empathy']),int_or_none(mob['Piety']),int_or_none(mob['Constitution']),
              int_or_none(mob['Speed']),int_or_none(mob['AggroRange']),int_or_none(mob['AggroLevel']),mob['Guild'],int_or_none(mob['Level']),int_or_none(mob['RespawnInterval']),int(mob['Region']),int_or_none(mob['X']),
              int_or_none(mob['Y']),int_or_none(mob['Z']),int_or_none(mob['Heading']),int_or_none(mob['Size']),int_or_none(mob['Realm']),int_or_none(mob['Model']),int_or_none(mob['NPCTemplateID']),int_or_none(mob['Flags']),
              int_or_none(mob['FactionID']),int_or_none(mob['BodyType']),int_or_none(mob['MeleeDamageType']),int_or_none(mob['Race']),int_or_none(mob['VisibleWeaponSlots']),int_or_none(mob['MaxDistance']),int_or_none(mob['RoamingRange']),int_or_none(mob['IsCloakHoodUp']),
              mob['Suffix'],mob['MessageArticle'],mob['ExamineArticle']))
        conn.commit()
    conn.close()

def init_mobs_data():
    create_mobs_table()
    insert_all_mobs()

def get_mobs_from_region(region_id):
    res = list()
    conn = connect_db()
    cursor = conn.execute('''
        SELECT * FROM MOBS WHERE X IS NOT NULL AND Y IS NOT NULL AND Z IS NOT NULL AND HEADING IS NOT NULL AND MODEL IS NOT NULL AND SIZE IS NOT NULL AND REGION=?''', (region_id,))
    rep = cursor.fetchall()
    if rep: res = [a for a in rep]
    conn.close()
    return [deserialize_mob(r) for r in res]
