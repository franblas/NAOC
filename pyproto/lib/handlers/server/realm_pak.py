from ..packets.packet_out import *

# 0x00 = No Realm
# 0x01 = Albion
# 0x02 = Midgard
# 0x03 = Hibernia
def realm_pak(realm):
  ins = write_byte(realm)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xFE)
  pak += ins
  return pak
