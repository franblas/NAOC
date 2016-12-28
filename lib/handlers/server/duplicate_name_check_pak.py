from ..packets.packet_out import *

def duplicate_name_check_pak(character_name, already_exists, gameclient):
  login_name = gameclient.login_name
  ins = fill_string_pak(character_name, 30)
  ins += fill_string_pak(login_name, 24)
  ins += write_byte(0x01) if already_exists else write_byte(0x00)
  ins += fill_pak(0x00, 3)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xCC)
  pak += ins
  return pak
