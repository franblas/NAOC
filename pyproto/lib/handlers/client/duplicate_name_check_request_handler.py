from ..packets.packet_in import read_string
from ..packets.packet_utils import printable_string
from ..server.duplicate_name_check_pak import duplicate_name_check_pak

def duplicate_name_check_request_handler(packet,gameclient):
  cursor = 0
  character_name_tmp, cursor = read_string(packet, 30, cursor)
  character_name = printable_string(character_name_tmp)
  # TODO check if name already exists in the db
  already_exists = False
  return duplicate_name_check_pak(character_name, already_exists, gameclient)
