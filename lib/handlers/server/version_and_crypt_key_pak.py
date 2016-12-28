from ..packets.packet_out import *
from ..packets.packet_utils import parse_version

def version_and_crypt_key_pak(version):
  ins = write_byte(0x00)
  ins += write_byte(0x32)
  ins += write_byte(parse_version(version, True))
  ins += write_byte(parse_version(version, False))
  ins += write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x22)
  pak += ins
  return pak
