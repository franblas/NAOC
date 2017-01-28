from ..packets.packet_out import *

def region_color_scheme_pak(color):
  ins = write_short(0x00)
  ins += write_byte(0x05)
  ins += write_byte(color)
  ins += write_int(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x4C)
  pak += ins
  return pak
