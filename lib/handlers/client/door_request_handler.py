from ..packets.packet_in import *
from ..server.door_state_pak import door_state_pak

def door_request_handler(packet,gameclient):
    cursor = 0
    door_id, cursor = read_int(packet, cursor)
    door_state, cursor = read_byte(packet, cursor)

    door = {
      'door_id': door_id,
      'door_state': door_state
    }

    return door_state_pak(None, door, gameclient) #TODO pass the region
