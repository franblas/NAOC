import json
from ..packets.packet_in import read_data
from void_handler import void_handler
from character_create_request_handler import character_create_request_handler
from character_overview_request_handler import character_overview_request_handler
from character_select_request_handler import character_select_request_handler
from crypt_key_request_handler import crypt_key_request_handler
from duplicate_name_check_request_handler import duplicate_name_check_request_handler
from login_request_handler import login_request_handler
from ping_request_handler import ping_request_handler
from region_list_request_handler import region_list_request_handler
from game_open_request_handler import game_open_request_handler
from client_crash_handler import client_crash_handler
from world_init_request_handler import world_init_request_handler
from player_init_request_handler import player_init_request_handler

CODE_POSITION = 9

with open('lib/handlers/client/client_handler_mapping.json', 'r') as f:
    client_handler_mapping = json.load(f)

def call_handler(handler, packet, gameclient):
    return eval(handler + '(packet[CODE_POSITION+1:],gameclient)')

def client_handler(raw_data, request_counter, gameclient):
    packet = read_data(raw_data)
    print '--------> 0x%02X' % int(packet[CODE_POSITION])
    map_val = '0x%02X' % int(packet[CODE_POSITION])
    handler = client_handler_mapping.get(map_val)
    if not handler: return
    return call_handler(handler, packet, gameclient)
