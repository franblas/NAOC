from ..packets.packet_in import read_string
from ..server.character_overview_pak import character_overview_pak
from ..server.realm_pak import realm_pak

def character_overview_request_handler(packet,gameclient):
    cursor = 0
    account_name_tmp, cursor = read_string(packet, 24, cursor)
    account_name = account_name_tmp.replace('\x00', '')
    if account_name.split('-')[0] + '-X' in account_name:
        return realm_pak(0x00) # No realm (multiple account selection)
    else:
        if account_name.endswith('-S'):
            print 'Albion'
            return character_overview_pak(0x01, gameclient)
        elif account_name.endswith('-N'):
            print 'Midgard'
            return character_overview_pak(0x02, gameclient)
        elif account_name.endswith('-H'):
            print 'Hibernia'
            return character_overview_pak(0x03, gameclient)
        else:
            print 'Unknown realm' # Should throw an error to the client
            return
