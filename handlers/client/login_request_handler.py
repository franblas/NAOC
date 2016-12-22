from ..packets.packet_in import skip, read_byte, read_string, read_int
from ..packets.packet_utils import version_builder
from ..server.login_granted_pak import login_granted_pak

def login_request_handler(packet):
    cursor = 0
    cursor = skip(cursor, 2)
    major, cursor = read_byte(packet, cursor) #TODO check validity of this one
    minor, cursor = read_byte(packet, cursor) #TODO check validity of this one
    build, cursor = read_byte(packet, cursor) #TODO check validity of this one
    password, cursor = read_string(packet, 20, cursor)
    cursor = skip(cursor, 7)
    c2, cursor = read_int(packet, cursor)
    c3,cursor = read_int(packet, cursor)
    c4, cursor = read_int(packet, cursor)
    cursor = skip(cursor, 31)
    username, cursor = read_string(packet, 20, cursor)
    print major, minor, build, password, username, cursor
    #TODO check username/password and send back to response (login granted or denied)
    version = version_builder(major, minor, build)
    return login_granted_pak(version, username)
