from ..packets.packet_out import *

def session_id_pak(gameclient):
  session_id = gameclient.session_id
  ins = write_short(session_id, endian='little')

  pak = write_short(packet_length(ins))
  pak += write_byte(0x28)
  pak += ins
  return pak
