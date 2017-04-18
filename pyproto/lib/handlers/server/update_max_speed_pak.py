from ..packets.packet_out import *

def update_max_speed_pak(gameclient):
   data = gameclient.selected_character
   if not data: return

   # pak.WriteShort((ushort) (m_gameClient.Player.MaxSpeed*100/GamePlayer.PLAYER_BASE_SPEED));
   ins = write_short(0x007D)

   # pak.WriteByte((byte) (m_gameClient.Player.IsTurningDisabled ? 0x01 : 0x00));
   ins += write_byte(0x00)

   # # water speed in % of land speed if its over 0 i think
   # pak.WriteByte((byte)Math.Min(byte.MaxValue,
   # 	((m_gameClient.Player.MaxSpeed*100/GamePlayer.PLAYER_BASE_SPEED)*(m_gameClient.Player.GetModified(eProperty.WaterSpeed)*.01))));
   ins += write_byte(0x00)

   pak = write_short(packet_length(ins))
   pak += write_byte(0xB6)
   pak += ins
   return pak
