from ..packets.packet_out import *
from ..packets.packet_utils import parse_version

def login_granted_pak(version, username):
  ins = write_byte(0x01)
  ins += write_byte(parse_version(version, True))
  ins += write_byte(parse_version(version, False))
  ins += write_byte(0x00)
  ins += write_pascal_string(username)
  ins += write_pascal_string('pyDOL') # Server name
  ins += write_byte(0x0C)
  ins += write_byte(0x00)
  ins += write_byte(0x00)
  ins += write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x2A)
  pak += ins
  return pak
