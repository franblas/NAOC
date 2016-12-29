from ..packets.packet_in import skip, read_string
from ..packets.packet_utils import printable_string
from ..server.session_id_pak import session_id_pak
from ...database.db_characters import get_character

def character_select_request_handler(packet,gameclient):
    cursor = 0
    cursor = skip(cursor, 4)
    character_name, cursor = read_string(packet, 28, cursor)
    clean_character_name = printable_string(character_name).replace('*', '')
    if clean_character_name != 'noname':
      character_data = get_character(gameclient.login_name, clean_character_name)
      if character_data: gameclient.selected_character = character_data
    return session_id_pak(gameclient)
