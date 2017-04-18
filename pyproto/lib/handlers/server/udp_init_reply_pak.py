from ..packets.packet_out import *

def udp_init_reply_pak(gameclient):
   # data = gameclient.selected_character
   # if not data: return
   # TODO
   return

   pak = write_short(packet_length(ins))
   pak += write_byte(0x2F)
   pak += ins
   return pak

# using (var pak = new GSUDPPacketOut(GetPacketCode(eServerPackets.UDPInitReply)))
# {
# 	Region playerRegion = null;
# 	if (!m_gameClient.Socket.Connected)
# 		return;
# 	if (m_gameClient.Player != null && m_gameClient.Player.CurrentRegion != null)
# 		playerRegion = m_gameClient.Player.CurrentRegion;
# 	if (playerRegion == null)
# 		pak.Fill(0x0, 0x18);
# 	else
# 	{
# 		#Try to fix the region ip so UDP is enabled!
# 		string ip = playerRegion.ServerIP;
# 		if (ip == "any" || ip == "0.0.0.0" || ip == "127.0.0.1" || ip.StartsWith("10.13.") || ip.StartsWith("192.168."))
# 			ip = ((IPEndPoint) m_gameClient.Socket.LocalEndPoint).Address.ToString();
# 		pak.FillString(ip, 22);
# 		pak.WriteShort(playerRegion.ServerPort);
# 	}
# 	SendUDP(pak, true);
# }
