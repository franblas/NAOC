from ..packets.packet_out import *

def debug_mode_pak():
  # if (m_gameClient.Account.PrivLevel == 1)
  # {
  #     pak.WriteByte((0x00));
  # }
  # else
  # {
  #     pak.WriteByte((byte) (on ? 0x01 : 0x00));
  # }
  ins = write_byte(0x00)

  ins += write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x21)
  pak += ins
  return pak
