from ..packets.packet_in import read_string
from ..packets.packet_utils import printable_string
from character_creation import create_character_data, create_character
from ..server.character_create_reply_pak import character_create_reply_pak
from ..server.character_overview_pak import character_overview_pak
from ...database.db_characters import get_next_account_slot

def character_create_request_handler(packet,gameclient):
  cursor = 0
  account_name_tmp, cursor = read_string(packet, 24, cursor)
  account_name = printable_string(account_name_tmp)
  # print '---> AccountName: ' + account_name
  if '-S' in account_name: # TODO: weird, should be endswith
    print 'Albion'
    current_realm = 0x01
  elif '-N' in account_name: # TODO: weird, should be endswith
    print 'Midgard'
    current_realm = 0x02
  elif '-H' in account_name: # TODO: weird, should be endswith
    print 'Hibernia'
    current_realm = 0x03
  else:
    print 'Unknown realm' # Should throw an error to the client
    return
  for i in range(0, 10):
    character_data, packet, cursor = create_character_data(packet, cursor)
    account_slot = get_next_account_slot(gameclient.login_name, current_realm)
    character = create_character(character_data, account_slot, gameclient)
  # character_create_reply_pak("")
  return character_overview_pak(current_realm, gameclient)
