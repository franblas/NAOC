import json
from ..packets.packet_in import read_data
from character_create_request_handler import character_create_request_handler
from character_overview_request_handler import character_overview_request_handler
from character_select_request_handler import character_select_request_handler
from crypt_key_request_handler import crypt_key_request_handler
from duplicate_name_check_request_handler import duplicate_name_check_request_handler
from login_request_handler import login_request_handler
from ping_request_handler import ping_request_handler

CODE_POSITION = 9

with open('handlers/client/client_handler_mapping.json', 'r') as f:
    client_handler_mapping = json.load(f)

def call_handler(handler, packet):
    return eval(handler + '(packet[CODE_POSITION+1:])')

def client_handler(raw_data, request_counter):
    with open('request_counter', "w") as f:
        f.write(str(request_counter))
    packet = read_data(raw_data)
    map_val = '0x%02X' % int(packet[CODE_POSITION])
    handler = client_handler_mapping.get(map_val)
    if not handler: return
    return call_handler(handler, packet)
