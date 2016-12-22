from ..packets.packet_out import *

def session_id_pak():
  ins = write_short(0x01, endian='little') #TODO: check SessionID

  pak = write_short(packet_length(ins))
  pak += write_byte(0x28)
  pak += ins
  return pak
