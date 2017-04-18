from ..packets.packet_in import *

def player_command_handler(packet,gameclient):
    cursor = 0
    cursor = skip(cursor, 8)
    cmdline, cursor = read_string(packet, 255, cursor)
    print "COMMAND LINE: " + str(cmdline)

    # return door_state_pak(None, door, gameclient) #TODO pass the region
