from ..packets.packet_out import *

def char_stats_update_pak(gameclient):
  loaded_character = gameclient.selected_character
  if not loaded_character: return

  data = gameclient.player.db_character

  update_stats = [
    data['strength'], # eStat.STR,
    data['dexterity'], # eStat.DEX,
    data['constitution'], # eStat.CON,
    data['quickness'], # eStat.QUI,
    data['intelligence'], # eStat.INT,
    data['piety'], # eStat.PIE,
    data['empathy'], # eStat.EMP,
    data['charisma'], # eStat.CHR
  ]
  ins = ''

  # 			# base
  # 			for (int i = 0; i < updateStats.Length; i++)
  # 			{
  # 				baseStats[i] = m_gameClient.Player.GetBaseStat(updateStats[i]);
  # 				if (updateStats[i] == eStat.CON)
  # 					baseStats[i] -= m_gameClient.Player.TotalConstitutionLostAtDeath;
  # 				pak.WriteShort((ushort)baseStats[i]);
  # 			}
  for u in update_stats:
    ins += write_short(u) #TODO

  # 			pak.WriteShort(0);
  ins += write_short(0x00)

  # 			# buffs/debuffs only; remove base, item bonus, RA bonus, class bonus
  # 			for (int i = 0; i < updateStats.Length; i++)
  # 			{
  # 				modStats[i] = m_gameClient.Player.GetModified((eProperty)updateStats[i]);
  # 				int abilityBonus = m_gameClient.Player.AbilityBonus[(int)updateStats[i]];
  # 				int acuityItemBonus = 0;
  # 				if ( updateStats[i] ==  m_gameClient.Player.CharacterClass.ManaStat )
  # 				{
  # 					if (m_gameClient.Player.CharacterClass.ID != (int)eCharacterClass.Scout && m_gameClient.Player.CharacterClass.ID != (int)eCharacterClass.Hunter && m_gameClient.Player.CharacterClass.ID != (int)eCharacterClass.Ranger)
  # 					{
  # 						abilityBonus += m_gameClient.Player.AbilityBonus[(int)eProperty.Acuity];
  # 						if (m_gameClient.Player.CharacterClass.ClassType != eClassType.PureTank)
  # 							acuityItemBonus = m_gameClient.Player.ItemBonus[(int)eProperty.Acuity];
  # 					}
  # 				}

  # 				int buff = modStats[i] - baseStats[i];
  # 				buff -= abilityBonus;
  # 				buff -= Math.Min( itemCaps[i], m_gameClient.Player.ItemBonus[(int)updateStats[i]] + acuityItemBonus );
  # 				pak.WriteShort((ushort)buff);
  # 			}
  for u in update_stats:
    ins += write_short(0x00)

  # 			pak.WriteShort(0);
  ins += write_short(0x00)

  # 			# item bonuses
  # 			for (int i = 0; i < updateStats.Length; i++)
  # 			{
  # 				int acuityItemBonus = 0;
  # 				if( updateStats[i] == m_gameClient.Player.CharacterClass.ManaStat )
  # 				{
  # 					if (m_gameClient.Player.CharacterClass.ID != (int)eCharacterClass.Scout && m_gameClient.Player.CharacterClass.ID != (int)eCharacterClass.Hunter && m_gameClient.Player.CharacterClass.ID != (int)eCharacterClass.Ranger)
  # 					{
  # 						if (m_gameClient.Player.CharacterClass.ClassType != eClassType.PureTank)
  # 							acuityItemBonus = m_gameClient.Player.ItemBonus[(int)eProperty.Acuity];
  # 					}
  # 				}
  # 				pak.WriteShort( (ushort)(m_gameClient.Player.ItemBonus[(int)updateStats[i]] + acuityItemBonus) );
  # 			}
  for u in update_stats:
    ins += write_short(0x00)

  # 			pak.WriteShort(0);
  ins += write_short(0x00)

  # 			# item caps
  # 			for (int i = 0; i < updateStats.Length; i++)
  # 			{
  # 				pak.WriteByte((byte)itemCaps[i]);
  # 			}
  for u in update_stats:
    ins += write_byte(0x01)

  # 			pak.WriteByte(0);
  ins += write_byte(0x00)

  # 			# RA bonuses
  # 			for (int i = 0; i < updateStats.Length; i++)
  # 			{
  # 				int acuityItemBonus = 0;
  # 				if (m_gameClient.Player.CharacterClass.ClassType != eClassType.PureTank && (int)updateStats[i] == (int)m_gameClient.Player.CharacterClass.ManaStat)
  # 				{
  # 					if (m_gameClient.Player.CharacterClass.ID != (int)eCharacterClass.Scout && m_gameClient.Player.CharacterClass.ID != (int)eCharacterClass.Hunter && m_gameClient.Player.CharacterClass.ID != (int)eCharacterClass.Ranger)
  # 					{
  # 						acuityItemBonus = m_gameClient.Player.AbilityBonus[(int)eProperty.Acuity];
  # 					}
  # 				}
  # 				pak.WriteByte((byte)(m_gameClient.Player.AbilityBonus[(int)updateStats[i]] + acuityItemBonus));
  # 			}
  for u in update_stats:
    ins += write_byte(0x00)

  # 			pak.WriteByte(0);
  ins += write_byte(0x00)

  # 			#Why don't we and mythic use this class bonus byte?
  # 			#pak.Fill(0, 9);
  # 			#if (m_gameClient.Player.CharacterClass.ID == (int)eCharacterClass.Vampiir)
  # 			#	pak.WriteByte((byte)(m_gameClient.Player.Level - 5)); # Vampire bonuses
  # 			#else
  # 			pak.WriteByte(0x00); # FF if resists packet
  ins +=write_byte(0x00)

  # 			pak.WriteByte((byte) m_gameClient.Player.TotalConstitutionLostAtDeath);
  ins += write_byte(0x00)

  # 			pak.WriteShort((ushort) m_gameClient.Player.MaxHealth);
  ins += write_short(0x1E)

  # 			pak.WriteShort(0);
  ins += write_short(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xFB)
  pak += ins
  return pak
