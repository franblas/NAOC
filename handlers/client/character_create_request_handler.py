from ..packets.packet_in import read_string
from character_creation import create_character_data, create_character
from ..server.character_overview_pak import character_overview_pak

def character_create_request_handler(packet):
  cursor = 0
  account_name_tmp, cursor = read_string(packet, 24, cursor)
  account_name = account_name_tmp.replace('\x00', '').strip()
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
  character_data = create_character_data(packet, cursor)
  character = create_character(character_data, account_slot=0) #TODO check account slot
  ############################
  import time
  print 'BEFORE SLEEP, character has been created'
  time.sleep(2)
  print 'AFTER SLEEP, send the character overview pak'
  ############################
  return character_overview_pak(current_realm)
