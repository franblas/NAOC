import sqlite3
import arrow

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
		GUILD_ID TEXT NOT NULL,
		REALM_LEVEL INTEGER NOT NULL,
		IS_CLOAK_HOOD_UP BOOLEAN NOT NULL,
		IS_CLOAK_INSISIBLE BOOLEAN NOT NULL,
        IS_HELM_INVISIBLE BOOLEAN NOT NULL,
        SPELL_QUEUE BOOLEAN NOT NULL,
        COPPER INTEGER NOT NULL,
        SILVER INTEGER NOT NULL,
        GOLD INTEGER NOT NULL,
        PLATINIUM INTEGER NOT NULL,
        MITHRIL INTEGER NOT NULL,
        X_POS INTEGER NOT NULL,
        Y_POS INTEGER NOT NULL,
        Z_POS INTEGER NOT NULL,
        BIND_X_POS INTEGER NOT NULL,
        BIND_Y_POS INTEGER NOT NULL,
        BIND_Z_POS INTEGER NOT NULL,
        BIND_REGION INTEGER NOT NULL,
        BIND_HEADING INTEGER NOT NULL,
        BIND_HOUSE_X_POS INTEGER NOT NULL,
        BIND_HOUSE_Y_POS INTEGER NOT NULL,
        BIND_HOUSE_Z_POS INTEGER NOT NULL,
        BIND_HOUSE_REGION INTEGER NOT NULL,
        BIND_HOUSE_HEADING INTEGER NOT NULL,
        DEATH_COUNT INTEGER NOT NULL,
        CONSTITUTION_LOST_AT_DEATH INTEGER NOT NULL,
        HAS_GRAVESTONE BOOLEAN NOT NULL,
        GRAVESTONE_REGION INTEGER NOT NULL,
        DIRECTION INTEGER NOT NULL,
        IS_LEVEL_SECOND_STAGE BOOLEAN NOT NULL,
        USED_LEVEL_COMMAND BOOLEAN NOT NULL,
        ABILITIES TEXT NOT NULL,
        SPECS TEXT NOT NULL,
        REALM_ABILITIES TEXT NOT NULL,
        CRAFTING_SKILLS TEXT NOT NULL,
        DISABLED_SPELLS TEXT NOT NULL,
        DISABLED_ABILITIES TEXT NOT NULL,
        FRIEND_LIST TEXT NOT NULL,
        IGNORE_LIST TEXT NOT NULL,
        PLAYER_TITLE_TYPE TEXT NOT NULL,
        FLAG_CLASS_NAME BOOLEAN NOT NULL,
        GUILD_RANK INTEGER NOT NULL,
        RESPEC_AMOUNT_ALL_SKILL INTEGER NOT NULL,
        RESPEC_AMOUNT_SINGLE_SKILL INTEGER NOT NULL,
        RESPEC_AMOUNT_REALM_SKILL INTEGER NOT NULL,
        RESPEC_AMOUNT_DOL INTEGER NOT NULL,
        RESPEC_AMOUNT_CHAMPION_SKILL INTEGER NOT NULL,
        IS_LEVEL_RESPEC_USED BOOLEAN NOT NULL,
        RESPEC_BOUGHT INTEGER NOT NULL,
        SAFETY_FLAG BOOLEAN NOT NULL,
        CRAFTING_PRIMARY_SKILL INTEGER NOT NULL,
        CANCEL_STYLE BOOLEAN NOT NULL,
        IS_ANONYMOUS BOOLEAN NOT NULL,
        GAIN_XP BOOLEAN NOT NULL,
        GAIN_RP BOOLEAN NOT NULL,
        ROLEPLAY BOOLEAN NOT NULL,
        AUTOLOOT BOOLEAN NOT NULL,
        LAST_FREE_LEVEL INTEGER NOT NULL,
        LAST_FREE_LEVELED TIMESTAMP NOT NULL,
        LAST_PLAYED TIMESTAMP NOT NULL,
        SHOW_XFIRE_INFO BOOLEAN NOT NULL,
        NO_HELP BOOLEAN NOT NULL,
        SHOW_GUILD_LOGIN BOOLEAN NOT NULL,
        GUILD_NOTE TEXT NOT NULL,
        CL BOOLEAN NOT NULL,
        CL_LEVEL INTEGER NOT NULL,
        ML_LEVEL INTEGER NOT NULL,
        ML_GRANTED BOOLEAN NOT NULL,
        IGNORE_STATISTICS BOOLEAN NOT NULL,
        EXP INTEGER NOT NULL,
        BNTY_PTS INTEGER NOT NULL,
        REALM_PTS INTEGER NOT NULL,
        ACTIVE_WEAPON_SLOT INTEGER NOT NULL,
        PLAYED_TIME INTEGER NOT NULL,
        DEATH_TIME INTEGER NOT NULL,
        CUSTOMISATION_STEP INTEGER NOT NULL,
        CL_EXP INTEGER NOT NULL,
        ML INTEGER NOT NULL,
        ML_EXP INTEGER NOT NULL,
        NOT_DISPLAYED_IN_HERALD INTEGER NOT NULL,
        ACTIVE_SADDLE_BAGS INTEGER NOT NULL,
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

    guild_id = '' #TODO
    realm_level = 1
    is_cloak_hood_up = False
    is_cloak_insisible = False
    is_helm_invisible = False
    spell_queue = False
    copper, silver, gold, platinium, mithril = 0,0,0,0,0
    x_pos, y_pos, z_pos = 0,0,0
    bind_x_pos, bind_y_pos, bind_z_pos, bind_region, bind_heading = 0,0,0,0,0
    bind_house_x_pos, bind_house_y_pos, bind_house_z_pos, bind_house_region, bind_house_heading = 0,0,0,0,0
    death_count = 0
    constitution_lost_at_death = 0
    has_gravestone = False
    gravestone_region = 0
    direction = 0
    is_level_second_stage = False
    used_level_command = False
    abilities = ''
    specs = ''
    realm_abilities = ''
    crafting_skills = ''
    disabled_spells = ''
    disabled_abilities = ''
    friend_list = ''
    ignore_list = ''
    player_title_type = ''
    flag_class_name = True
    guild_rank = 1
    respec_amount_all_skill = -1
    respec_amount_single_skill = -1
    respec_amount_realm_skill = -1
    respec_amount_dol = -1
    respec_amount_champion_skill = -1
    is_level_respec_used = False
    respec_bought = -1
    safety_flag = False
    crafting_primary_skill = 0
    cancel_style = False
    is_anonymous = False
    gain_xp = False
    gain_rp = False
    roleplay = False
    autoloot = False
    last_free_level = arrow.now().isoformat()
    last_free_leveled = arrow.now().isoformat()
    last_played = arrow.now().isoformat()
    show_xfire_info = False
    no_help = False
    show_guild_login = False
    guild_note = ''
    cl = True
    cl_level = 1
    ml_level = 1
    ml_granted = False
    ignore_statistics = True
    exp = 1
    bnty_pts = 0
    realm_pts = 0
    active_weapon_slot = 0
    played_time = 0
    death_time = 0
    customisation_step = 1
    cl_exp = 0
    ml = 0
    ml_exp = 0
    not_displayed_in_herald = 0
    active_saddle_bags = 0



    conn.execute('''
    INSERT INTO CHARACTERS (NAME,CREATION_DATE,CUSTOM_MODE,EYE_SIZE,LIP_SIZE,EYE_COLOR, \
    HAIR_COLOR,FACE_TYPE,HAIR_STYLE,MOOD_TYPE,OPERATION,UNK,LEVEL,CHAR_CLASS,REALM,RACE,GENDER, \
    SHROUDED_ISLES_START_LOCATION,CREATION_MODEL,REGION,STRENGTH,DEXTERITY,CONSTITUTION,QUICKNESS,INTELLIGENCE, \
    PIETY,EMPATHY,CHARISMA,ACTIVE_RIGHT_SLOT,ACTIVE_LEFT_SLOT,SHROUDED_ISLES_ZONE,NEW_CONSTITUTION,ACCOUNT_SLOT, \
    ENDURANCE,MAX_ENDURANCE,CONCENTRATION,MAX_SPEED,LOGIN_ID, \
    GUILD_ID,REALM_LEVEL,IS_CLOAK_HOOD_UP,IS_CLOAK_INSISIBLE,IS_HELM_INVISIBLE, \
    SPELL_QUEUE,COPPER,SILVER,GOLD,PLATINIUM,MITHRIL,X_POS,Y_POS,Z_POS,BIND_X_POS, \
    BIND_Y_POS,BIND_Z_POS,BIND_REGION,BIND_HEADING,BIND_HOUSE_X_POS,BIND_HOUSE_Y_POS, \
    BIND_HOUSE_Z_POS,BIND_HOUSE_REGION,BIND_HOUSE_HEADING,DEATH_COUNT,CONSTITUTION_LOST_AT_DEATH, \
    HAS_GRAVESTONE,GRAVESTONE_REGION,DIRECTION,IS_LEVEL_SECOND_STAGE,USED_LEVEL_COMMAND,ABILITIES, \
    SPECS,REALM_ABILITIES,CRAFTING_SKILLS,DISABLED_SPELLS,DISABLED_ABILITIES,FRIEND_LIST, \
    IGNORE_LIST,PLAYER_TITLE_TYPE,FLAG_CLASS_NAME,GUILD_RANK,RESPEC_AMOUNT_ALL_SKILL, \
    RESPEC_AMOUNT_SINGLE_SKILL,RESPEC_AMOUNT_REALM_SKILL,RESPEC_AMOUNT_DOL,RESPEC_AMOUNT_CHAMPION_SKILL, \
    IS_LEVEL_RESPEC_USED,RESPEC_BOUGHT,SAFETY_FLAG,CRAFTING_PRIMARY_SKILL,CANCEL_STYLE, \
    IS_ANONYMOUS,GAIN_XP,GAIN_RP,ROLEPLAY,AUTOLOOT,LAST_FREE_LEVEL,LAST_FREE_LEVELED,LAST_PLAYED, \
    SHOW_XFIRE_INFO,NO_HELP,SHOW_GUILD_LOGIN,GUILD_NOTE,CL,CL_LEVEL,ML_LEVEL,ML_GRANTED,IGNORE_STATISTICS,
    EXP,BNTY_PTS,REALM_PTS,ACTIVE_WEAPON_SLOT,PLAYED_TIME,DEATH_TIME,CUSTOMISATION_STEP,CL_EXP,ML,ML_EXP,
    NOT_DISPLAYED_IN_HERALD,ACTIVE_SADDLE_BAGS) \
      VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, \
      ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, \
      ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (name,creation_date,custom_mode,eye_size,lip_size,eye_color,
      hair_color,face_type,hair_style,mood_type,operation,unk,level,char_class,realm,race,gender,
      shrouded_isles_start_location,creation_model,region,strength,dexterity,constitution,quickness,intelligence,
      piety,empathy,charisma,active_right_slot,active_left_slot,shrouded_isles_zone,new_constitution,account_slot,
      endurance,max_endurance,concentration,max_speed,login_id,guild_id,realm_level,is_cloak_hood_up,is_cloak_insisible,
      is_helm_invisible,spell_queue,copper,silver,gold,platinium,mithril,x_pos,y_pos,z_pos,bind_x_pos,bind_y_pos,bind_z_pos,
      bind_region,bind_heading,bind_house_x_pos,bind_house_y_pos,bind_house_z_pos,bind_house_region,bind_house_heading,
      death_count,constitution_lost_at_death,has_gravestone,gravestone_region,direction,is_level_second_stage,
      used_level_command,abilities,specs,realm_abilities,crafting_skills,disabled_spells,disabled_abilities,friend_list,
      ignore_list,player_title_type,flag_class_name,guild_rank,respec_amount_all_skill,respec_amount_single_skill,
      respec_amount_realm_skill,respec_amount_dol,respec_amount_champion_skill,is_level_respec_used,respec_bought,
      safety_flag,crafting_primary_skill,cancel_style,is_anonymous,gain_xp,gain_rp,
      roleplay,autoloot,last_free_level,last_free_leveled,last_played,show_xfire_info,
      no_help,show_guild_login,guild_note,cl,cl_level,ml_level,ml_granted,ignore_statistics,exp,bnty_pts,realm_pts,
      active_weapon_slot,played_time,death_time,customisation_step,cl_exp,ml,ml_exp,not_displayed_in_herald,active_saddle_bags))
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

def deserialize_character_data(rep):
    if not rep: return dict()
    return {
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
        "max_speed": rep[37],
		"guild_id": rep[39], # ignore login_id
        "realm_level": rep[40],
        "is_cloak_hood_up": rep[41],
        "is_cloak_insisible": rep[42],
        "is_helm_invisible": rep[43],
        "spell_queue": rep[44],
        "copper": rep[45],
        "silver": rep[46],
        "gold": rep[47],
        "platinium": rep[48],
        "mithril": rep[49],
        "x_pos": rep[50],
        "y_pos": rep[51],
        "z_pos": rep[52],
        "bind_x_pos": rep[53],
        "bind_y_pos": rep[54],
        "bind_z_pos": rep[55],
        "bind_region": rep[56],
        "bind_heading": rep[57],
        "bind_house_x_pos": rep[58],
        "bind_house_y_pos": rep[59],
        "bind_house_z_pos": rep[60],
        "bind_house_region": rep[61],
        "bind_house_heading": rep[62],
        "death_count": rep[63],
        "constitution_lost_at_death": rep[64],
        "has_gravestone": rep[65],
        "gravestone_region": rep[66],
        "direction": rep[67],
        "is_level_second_stage": rep[68],
        "used_level_command": rep[69],
        "abilities": rep[70],
        "specs": rep[71],
        "realm_abilities": rep[72],
        "crafting_skills": rep[73],
        "disabled_spells": rep[74],
        "disabled_abilities": rep[75],
        "friend_list": rep[76],
        "ignore_list": rep[77],
        "player_title_type": rep[78],
        "flag_class_name": rep[79],
        "guild_rank": rep[80],
        "respec_amount_all_skill": rep[81],
        "respec_amount_single_skill": rep[82],
        "respec_amount_realm_skill": rep[83],
        "respec_amount_dol": rep[84],
        "respec_amount_champion_skill": rep[85],
        "is_level_respec_used": rep[86],
        "respec_bought": rep[87],
        "safety_flag": rep[88],
        "crafting_primary_skill": rep[89],
        "cancel_style": rep[90],
        "is_anonymous": rep[91],
        "gain_xp": rep[92],
        "gain_rp": rep[93],
        "roleplay": rep[94],
        "autoloot": rep[95],
        "last_free_level": rep[96],
        "last_free_leveled": rep[97],
        "last_played": rep[98],
        "show_xfire_info": rep[99],
        "no_help": rep[100],
        "show_guild_login": rep[101],
        "guild_note": rep[102],
        "cl": rep[103],
        "cl_level": rep[104],
        "ml_level": rep[105],
        "ml_granted": rep[106],
        "ignore_statistics": rep[107],
        "exp": rep[108],
        "bnty_pts": rep[109],
        "realm_pts": rep[110],
        "active_weapon_slot": rep[111],
        "played_time": rep[112],
        "death_time": rep[113],
        "customisation_step": rep[114],
        "cl_exp": rep[115],
        "ml": rep[116],
        "ml_exp": rep[117],
        "not_displayed_in_herald": rep[118],
        "active_saddle_bags": rep[119]
    }

def get_character(login_name, char_name):
    login_id = get_id(login_name)
    conn = connect_db()
    cursor = conn.execute('''
    SELECT * FROM CHARACTERS WHERE LOGIN_ID=? AND NAME=?''', (login_id,char_name))
    rep = cursor.fetchone()
    character_data = deserialize_character_data(rep)
    conn.close()
    return character_data

def get_characters(login_name, realm):
    characters_data = list()
    login_id = get_id(login_name)
    conn = connect_db()
    cursor = conn.execute('''
    SELECT * FROM CHARACTERS WHERE LOGIN_ID=? AND REALM=?''', (login_id,realm))
    reps = cursor.fetchall()
    data_l = [r for r in reps]
    if not data_l: return list()
    for rep in data_l: characters_data.append(deserialize_character_data(rep))
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
