from ..packets.packet_in import skip, read_string
from ..packets.packet_utils import printable_string
from ..server.session_id_pak import session_id_pak
from ...database.db_characters import get_character
from ...gameobjects.gameplayer import GamePlayer

def character_select_request_handler(packet,gameclient):
    cursor = 0
    # int packetVersion;
    # switch (client.Version)
    # {
    # 	case GameClient.eClientVersion.Version168:
    # 	case GameClient.eClientVersion.Version169:
    # 	case GameClient.eClientVersion.Version170:
    # 	case GameClient.eClientVersion.Version171:
    # 	case GameClient.eClientVersion.Version172:
    # 	case GameClient.eClientVersion.Version173:
    # 		packetVersion = 168;
    # 		break;
    # 	default:
    # 		packetVersion = 174;
    # 		break;
    # }
    # packet.Skip(4); //Skip the first 4 bytes
    # if (packetVersion == 174)
    # {
    # 	packet.Skip(1);
    # }
    cursor = skip(cursor, 5)
    character_name, cursor = read_string(packet, 28, cursor)
    clean_character_name = printable_string(character_name).replace('*', '')
    if not clean_character_name: return
    if clean_character_name != 'noname':
      character_data = get_character(gameclient.login_name, clean_character_name)
      if character_data:
          gameclient.selected_character = character_data
          gameclient.player = GamePlayer(character_data)
        #   gameclient.player.db_character = character_data

    return session_id_pak(gameclient)
