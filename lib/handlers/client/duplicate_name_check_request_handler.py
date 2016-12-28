from ..packets.packet_in import read_string
from ..server.duplicate_name_check_pak import duplicate_name_check_pak

def duplicate_name_check_request_handler(packet,gameclient):
  cursor = 0
  character_name_tmp, cursor = read_string(packet, 30, cursor)
  character_name = character_name_tmp.replace('\x00', '')
  # TODO check if name already exists in the db
  already_exists = False
  return duplicate_name_check_pak(character_name, already_exists, gameclient)
