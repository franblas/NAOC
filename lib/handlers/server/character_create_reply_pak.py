from ..packets.packet_out import *

def character_create_reply_pak(character_name):
  ins = fill_string_pak(character_name, 24)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xF0)
  pak += ins
  return pak
