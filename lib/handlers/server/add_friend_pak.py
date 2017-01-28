from ..packets.packet_out import *

def add_friend_pak():
  ins = write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xC5)
  pak += ins
  return pak
