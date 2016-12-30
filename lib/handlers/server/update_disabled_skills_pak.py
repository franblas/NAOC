from ..packets.packet_out import *

def update_disabled_skills_pak(gameclient):
  data = gameclient.selected_character
  if not data: return

  #TODO

  pak = write_short(packet_length(ins))
  pak += write_byte(0xD6)
  pak += ins
  return pak
		#
		#
		# public virtual void SendDisableSkill(ICollection<Tuple<Skill, int>> skills)
		# {
		# 	if (m_gameClient.Player == null)
		# 		return;
		#
		# 	var disabledSpells = new List<Tuple<byte, byte, ushort>>();
		# 	var disabledSkills = new List<Tuple<ushort, ushort>>();
		#
		# 	var listspells = m_gameClient.Player.GetAllUsableListSpells();
		# 	var listskills = m_gameClient.Player.GetAllUsableSkills();
		# 	int specCount = listskills.Where(sk => sk.Item1 is Specialization).Count();
		#
		# 	// Get through all disabled skills
		# 	foreach (Tuple<Skill, int> disabled in skills)
		# 	{
		#
		# 		// Check if spell
		# 		byte lsIndex = 0;
		# 		foreach (var ls in listspells)
		# 		{
		# 			int index = ls.Item2.FindIndex(sk => sk.SkillType == disabled.Item1.SkillType && sk.ID == disabled.Item1.ID);
		#
		# 			if (index > -1)
		# 			{
		# 				disabledSpells.Add(new Tuple<byte, byte, ushort>(lsIndex, (byte)index, (ushort)(disabled.Item2 > 0 ? disabled.Item2 / 1000 + 1 : 0) ));
		# 				break;
		# 			}
		#
		# 			lsIndex++;
		# 		}
		#
		# 		int skIndex = listskills.FindIndex(skt => disabled.Item1.SkillType == skt.Item1.SkillType && disabled.Item1.ID == skt.Item1.ID) - specCount;
		#
		# 		if (skIndex > -1)
		# 			disabledSkills.Add(new Tuple<ushort, ushort>((ushort)skIndex, (ushort)(disabled.Item2 > 0 ? disabled.Item2 / 1000 + 1 : 0) ));
		# 	}
		#
		# 	if (disabledSkills.Count > 0)
		# 	{
		# 		// Send matching hybrid spell match
		# 		using (var pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.DisableSkills)))
		# 		{
		# 			byte countskill = (byte)Math.Min(disabledSkills.Count, 255);
		# 			if (countskill > 0)
		# 			{
		# 				pak.WriteShort(0); // duration unused
		# 				pak.WriteByte(countskill); // count...
		# 				pak.WriteByte(1); // code for hybrid skill
		#
		# 				for (int i = 0 ; i < countskill ; i++)
		# 				{
		# 					pak.WriteShort(disabledSkills[i].Item1); // index
		# 					pak.WriteShort(disabledSkills[i].Item2); // duration
		# 				}
		#
		# 				SendTCP(pak);
		# 			}
		# 		}
		# 	}
		#
		# 	if (disabledSpells.Count > 0)
		# 	{
		# 		var groupedDuration = disabledSpells.GroupBy(sp => sp.Item3);
		# 		foreach (var groups in groupedDuration)
		# 		{
		# 			// Send matching list spell match
		# 			using (var pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.DisableSkills)))
		# 			{
		# 				byte total = (byte)Math.Min(groups.Count(), 255);
		# 				if (total > 0)
		# 				{
		# 					pak.WriteShort(groups.Key); // duration
		# 					pak.WriteByte(total); // count...
		# 					pak.WriteByte(2); // code for list spells
		#
		# 					for (int i = 0 ; i < total ; i++)
		# 					{
		# 						pak.WriteByte(groups.ElementAt(i).Item1); // line index
		# 						pak.WriteByte(groups.ElementAt(i).Item2); // spell index
		# 					}
		#
		# 					SendTCP(pak);
		# 				}
		# 			}
		# 		}
		# 	}
		# }
