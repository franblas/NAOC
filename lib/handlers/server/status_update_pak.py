from ..packets.packet_out import *

def status_update_pak(sittingFlag):
  ins = write_byte(0) # HealthPercent, TODO
  ins += write_byte(0) # ManaPercent, TODO
  ins += write_byte(0) # sittingFlag, TODO
  ins += write_byte(0) # EndurancePercent, TODO
  ins += write_byte(0) # ConcentrationPercent, TODO
  ins += write_byte(0) # unk
  ins += write_short(0) # MaxMana, TODO
  ins += write_short(0) # MaxEndurance, TODO
  ins += write_short(0) # MaxConcentration, TODO
  ins += write_short(0) # MaxHealth, TODO
  ins += write_short(0) # Health, TODO
  ins += write_short(0) # Endurance, TODO
  ins += write_short(0) # Mana, TODO
  ins += write_short(0) # Concentration, TODO

  pak = write_short(packet_length(ins))
  pak += write_byte(0xAD)
  pak += ins
  return pak


# public override void SendStatusUpdate(byte sittingFlag)
# 		{
# 			if (m_gameClient.Player == null)
# 				return;
# 			using (GSTCPPacketOut pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.CharacterStatusUpdate)))
# 			{
# 				pak.WriteByte(m_gameClient.Player.HealthPercent);
# 				pak.WriteByte(m_gameClient.Player.ManaPercent);
# 				pak.WriteByte(sittingFlag);
# 				pak.WriteByte(m_gameClient.Player.EndurancePercent);
# 				pak.WriteByte(m_gameClient.Player.ConcentrationPercent);
# 				//			pak.WriteShort((byte) (m_gameClient.Player.IsAlive ? 0x00 : 0x0f)); // 0x0F if dead ??? where it now ?
# 				pak.WriteByte(0);// unk
# 				pak.WriteShort((ushort)m_gameClient.Player.MaxMana);
# 				pak.WriteShort((ushort)m_gameClient.Player.MaxEndurance);
# 				pak.WriteShort((ushort)m_gameClient.Player.MaxConcentration);
# 				pak.WriteShort((ushort)m_gameClient.Player.MaxHealth);
# 				pak.WriteShort((ushort)m_gameClient.Player.Health);
# 				pak.WriteShort((ushort)m_gameClient.Player.Endurance);
# 				pak.WriteShort((ushort)m_gameClient.Player.Mana);
# 				pak.WriteShort((ushort)m_gameClient.Player.Concentration);
# 				SendTCP(pak);
# 			}
# 		}
