from ..packets.packet_in import skip, read_string
from ..packets.packet_utils import printable_string
from ..server.session_id_pak import session_id_pak

def character_select_request_handler(packet,gameclient):
    cursor = 0
    cursor = skip(cursor, 4)
    character_name, cursor = read_string(packet, 28, cursor)
    print character_name
    clean_character_name = printable_string(character_name)
    if clean_character_name == '*noname':
      return session_id_pak(gameclient)
    else:
      #TODO
      return session_id_pak(gameclient)
