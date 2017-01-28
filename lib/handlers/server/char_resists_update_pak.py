from ..packets.packet_out import *

def char_resists_update_pak(gameclient):
  data = gameclient.selected_character
  if not data: return

  update_resists = [
  0, #eResist.Crush,
  0, #eResist.Slash,
  0, #eResist.Thrust,
  0, #eResist.Heat,
  0, #eResist.Cold,
  0, #eResist.Matter,
  0, #eResist.Body,
  0, #eResist.Spirit,
  0, #eResist.Energy,
  ]
  ins = ''

  # 			// racial resists
  # 			for (int i = 0; i < updateResists.Length; i++)
  # 			{
  # 				racial[i] = SkillBase.GetRaceResist(m_gameClient.Player.Race, updateResists[i]);
  # 				pak.WriteShort((ushort)racial[i]);
  # 			}
  for u in update_resists:
    ins += write_short(0x00)

  # 			// buffs/debuffs only; remove base, item bonus, RA bonus, race bonus
  # 			for (int i = 0; i < updateResists.Length; i++)
  # 			{
  # 				int mod = m_gameClient.Player.GetModified((eProperty)updateResists[i]);
  # 				int buff = mod - racial[i] - m_gameClient.Player.AbilityBonus[(int)updateResists[i]] - Math.Min(caps[i], m_gameClient.Player.ItemBonus[(int)updateResists[i]]);
  # 				pak.WriteShort((ushort)buff);
  # 			}
  for u in update_resists:
    ins += write_short(0x00)

  # 			// item bonuses
  # 			for (int i = 0; i < updateResists.Length; i++)
  # 			{
  # 				pak.WriteShort((ushort)(m_gameClient.Player.ItemBonus[(int)updateResists[i]]));
  # 			}
  for u in update_resists:
    ins += write_short(0x00)

  # 			// item caps
  # 			for (int i = 0; i < updateResists.Length; i++)
  # 			{
  # 				pak.WriteByte((byte)caps[i]);
  # 			}
  for u in update_resists:
    ins += write_byte(0x01)

  # 			// RA bonuses
  # 			for (int i = 0; i < updateResists.Length; i++)
  # 			{
  # 				pak.WriteByte((byte)(m_gameClient.Player.AbilityBonus[(int)updateResists[i]]));
  # 			}
  for u in update_resists:
    ins += write_byte(0x00)

  # 			pak.WriteByte(0xFF); // FF if resists packet
  ins += write_byte(0xFF)

  # 			pak.WriteByte(0);
  ins += write_byte(0x00)

  # 			pak.WriteShort(0);
  # 			pak.WriteShort(0);
  ins += write_short(0x00)
  ins += write_short(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xFB)
  pak += ins
  return pak
