from ..packets.packet_out import *

def player_init_finished_pak(mobs):
  ins = write_byte(mobs)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x2B)
  pak += ins
  return pak
