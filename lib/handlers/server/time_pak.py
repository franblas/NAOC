from ..packets.packet_out import *

def time_pak(gameclient):
   data = gameclient.selected_character
   if not data: return

   ins = write_int(77760000)
   ins += write_int(100)

   pak = write_short(packet_length(ins))
   pak += write_byte(0x7E)
   pak += ins
   return pak



# p
# 				if (m_gameClient != null && m_gameClient.Player != null)
# 				{
# 					pak.WriteInt(WorldMgr.GetCurrentGameTime(m_gameClient.Player));
# 					pak.WriteInt(WorldMgr.GetDayIncrement(m_gameClient.Player));
# 				}
# 				else
# 				{
# 					pak.WriteInt(WorldMgr.GetCurrentGameTime());
# 					pak.WriteInt(WorldMgr.GetDayIncrement());
# 				}
# 				SendTCP(pak);
