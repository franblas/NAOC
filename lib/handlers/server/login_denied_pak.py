from ..packets.packet_out import *
from ..packets.packet_utils import parse_version

def login_denied_pak(version, error_code):
    ins = write_byte(error_code)
    ins += write_byte(0x01)
    ins += write_byte(parse_version(version, True))
    ins += write_byte(parse_version(version, False))
    ins += write_byte(0x00)

    pak = write_short(packet_length(ins))
    pak += write_byte(0x2C)
    pak += ins
    return pak
