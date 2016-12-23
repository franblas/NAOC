from ..packets.packet_in import *
import arrow
import json

def create_character_data(packet, cursor):
	#if (client.Version >= GameClient.eClientVersion.Version1104)
	#	packet.ReadIntLowEndian();
	plop, cursor = read_int(packet, cursor, endian='little')
	character_name, cursor = read_string(packet, 24, cursor)
	custom_mode, cursor = read_byte(packet, cursor)
	eye_size, cursor = read_byte(packet, cursor)
	lip_size, cursor = read_byte(packet, cursor)
	eye_color, cursor = read_byte(packet, cursor)
	hair_color, cursor = read_byte(packet, cursor)
	face_type, cursor = read_byte(packet, cursor)
	hair_style, cursor = read_byte(packet, cursor)
	cursor = skip(cursor, 3)
	mood_type, cursor = read_byte(packet, cursor)
	cursor = skip(cursor, 8)
	operation, cursor = read_int(packet, cursor)
	unk, cursor = read_byte(packet, cursor)
	cursor = skip(cursor, 24) # Location str
	cursor = skip(cursor, 24) # class name
	cursor = skip(cursor, 24) # race name
	level, cursor = read_byte(packet, cursor)
	char_class, cursor = read_byte(packet, cursor)
	realm, cursor = read_byte(packet, cursor)
	start_race_gender, cursor = read_byte(packet, cursor)
	race = (int(start_race_gender) & 0x0F) + ((int(start_race_gender) & 0x40) >> 2)
	gender = (int(start_race_gender) >> 4) & 0x01
	shrouded_isles_start_location = (int(start_race_gender) >> 7) != 0
	creation_model, cursor = read_short(packet, cursor, endian='little')
	region, cursor = read_byte(packet, cursor)
	cursor = skip(cursor, 1)
	cursor = skip(cursor, 4)
	strength, cursor = read_byte(packet, cursor)
	dexterity, cursor = read_byte(packet, cursor)
	constitution, cursor = read_byte(packet, cursor)
	quickness, cursor = read_byte(packet, cursor)
	intelligence, cursor = read_byte(packet, cursor)
	piety, cursor = read_byte(packet, cursor)
	empathy, cursor = read_byte(packet, cursor)
	charisma, cursor = read_byte(packet, cursor)
	cursor = skip(cursor, 40) #TODO: equipement
	active_right_slot, cursor = read_byte(packet, cursor) # 0x9C
	active_left_slot, cursor = read_byte(packet, cursor) # 0x9D
	shrouded_isles_zone, cursor = read_byte(packet, cursor) # 0x9E
	#// skip 4 bytes added in 1.99
	#if (client.Version >= GameClient.eClientVersion.Version199 && client.Version < GameClient.eClientVersion.Version1104)
	#	packet.Skip(4);
	new_constitution, cursor = read_byte(packet, cursor) # 0x9F

	custom_mode = 2 # if another number, does not work. I don't know why :s

	d = {
		'name': character_name.replace('\x00', ''),
		'custom_mode': custom_mode,
		'eye_size': eye_size,
		'lip_size': lip_size,
		'eye_color': eye_color,
		'hair_color': hair_color,
		'face_type': face_type,
		'hair_style': hair_style,
		'mood_type': mood_type,
		'operation': operation,
		'unk': unk,
		'level': level,
		'char_class': char_class,
		'realm': realm,
		'race': race,
		'gender': gender,
		'shrouded_isles_start_location': shrouded_isles_start_location,
		'creation_model': creation_model,
		'region': region,
		'strength': strength,
		'dexterity': dexterity,
		'constitution': constitution,
		'quickness': quickness,
		'intelligence': intelligence,
		'piety': piety,
		'empathy': empathy,
		'charisma': charisma,
		'active_right_slot': active_right_slot,
		'active_left_slot': active_left_slot,
		'shrouded_isles_zone': shrouded_isles_zone,
		'new_constitution': new_constitution
	}
	return d

def create_character(character_data, account_slot):
	character_data['level'] = 1
	character_data['account_slot'] = account_slot + int(character_data['realm']) * 100
	character_data['creation_date'] = arrow.now().isoformat()
	character_data['endurance'] = 100
	character_data['max_endurance'] = 100
	character_data['concentration'] = 100
	character_data['max_speed'] = 191

	#TODO: insert into db
	try:
		with open('character_test.json', 'r') as f: yo = f
	except Exception as e:
		with open('character_test.json', 'w') as f:
			json.dump(character_data, f, indent=2)
	return character_data
