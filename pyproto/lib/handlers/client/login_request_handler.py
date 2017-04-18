from ..packets.packet_in import skip, read_byte, read_string, read_int
from ..packets.packet_utils import version_builder, printable_string
from ..server.login_granted_pak import login_granted_pak
from ..server.login_denied_pak import login_denied_pak
from ...database.db_accounts import is_account_and_password_correct

def login_request_handler(packet,gameclient):
    cursor = 0
    cursor = skip(cursor, 2)
    major, cursor = read_byte(packet, cursor) #TODO check validity of this one
    minor, cursor = read_byte(packet, cursor) #TODO check validity of this one
    build, cursor = read_byte(packet, cursor) #TODO check validity of this one
    password_tmp, cursor = read_string(packet, 20, cursor)
    cursor = skip(cursor, 7)
    c2, cursor = read_int(packet, cursor)
    c3,cursor = read_int(packet, cursor)
    c4, cursor = read_int(packet, cursor)
    cursor = skip(cursor, 31)
    username_tmp, cursor = read_string(packet, 20, cursor)
    # check username/password and send back to response (login granted or denied)
    username, password = printable_string(username_tmp), printable_string(password_tmp)
    login_granted = is_account_and_password_correct(username, password)
    version = version_builder(major, minor, build)
    if login_granted:
        gameclient.login_name = username
        return login_granted_pak(version, username)
    else:
        return login_denied_pak(version, 0x07) # 0x07, error code account not found
