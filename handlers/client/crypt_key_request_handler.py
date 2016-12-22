from ..packets.packet_in import read_byte
from ..packets.packet_utils import version_builder
from ..server.version_and_crypt_key_pak import version_and_crypt_key_pak

def crypt_key_request_handler(packet):
    cursor = 0
    rc4, cursor = read_byte(packet, cursor) # should bo 0 (if 1 then enrypted requests)
    client_type_tmp, cursor = read_byte(packet, cursor)
    # client_type
    #   unknown = -1
    # 	classic = 1
    # 	shrouded_isles = 2
    # 	trials_of_atlantis = 3
    # 	catacombs = 4
    # 	darkness_rising = 5
    # 	labyrinth_of_the_minotaur = 6
    client_type = hex(int(client_type_tmp) & 0x0F)
    client_addons = hex(int(client_type_tmp) & 0xF0)
    major, cursor = read_byte(packet, cursor)
    minor, cursor = read_byte(packet, cursor)
    build, cursor = read_byte(packet, cursor)
    # print rc4, client_type, client_addons, major, minor, build
    version = version_builder(major, minor, build)
    return version_and_crypt_key_pak(version)
