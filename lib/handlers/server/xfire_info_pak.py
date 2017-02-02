from ..packets.packet_out import *

def xfire_info_pak(flag, gameclient):
  data = gameclient.selected_character
  if not data: return

  # pak.WriteShort((ushort)m_gameClient.Player.ObjectID);
  ins = write_short(7)
  # pak.WriteByte(flag);
  ins += write_byte(flag)
  # pak.WriteByte(0x00);
  ins += write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x5C)
  pak += ins
  return pak
