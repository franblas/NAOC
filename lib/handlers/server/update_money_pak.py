from ..packets.packet_out import *

def update_money_pak(gameclient):
  data = gameclient.selected_character
  if not data: return

  # pak.WriteByte((byte) m_gameClient.Player.Copper);
  ins = write_byte(0x00)

  # pak.WriteByte((byte) m_gameClient.Player.Silver);
  ins += write_byte(0x00)

  # pak.WriteShort((ushort) m_gameClient.Player.Gold);
  ins += write_short(0x00)

  # pak.WriteShort((ushort) m_gameClient.Player.Mithril);
  ins += write_short(0x00)

  # pak.WriteShort((ushort) m_gameClient.Player.Platinum);
  ins += write_short(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xFA)
  pak += ins
  return pak


# 		public virtual void SendUpdateMoney()
# 		{
# 			if (m_gameClient.Player == null)
# 				return;
# 			using (var pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.MoneyUpdate)))
# 			{
# 				pak.WriteByte((byte) m_gameClient.Player.Copper);
# 				pak.WriteByte((byte) m_gameClient.Player.Silver);
# 				pak.WriteShort((ushort) m_gameClient.Player.Gold);
# 				pak.WriteShort((ushort) m_gameClient.Player.Mithril);
# 				pak.WriteShort((ushort) m_gameClient.Player.Platinum);
# 				SendTCP(pak);
# 			}
# 		}
