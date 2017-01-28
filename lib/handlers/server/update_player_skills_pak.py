from ..packets.packet_out import *

def update_player_skills_pak(gameclient):
   data = gameclient.selected_character
   if not data: return

   ins = write_byte(0x01)
   ins += write_byte(0x00)
   ins += write_byte(0x03)
   ins += write_byte(0x00)

   pak = write_short(packet_length(ins))
   pak += write_byte(0x16)
   pak += ins
   return pak

   # p
   # 			if (m_gameClient.Player == null)
   # 				return;
   #
   # 			// Get Skills as "Usable Skills" which are in network order ! (with forced update)
   # 			List<Tuple<Skill, Skill>> usableSkills = m_gameClient.Player.GetAllUsableSkills(true);
   #
   # 			bool sent = false; // set to true once we can't send packet anymore !
   # 			int index = 0; // index of our position in the list !
   # 			int total = usableSkills.Count; // cache List count.
   # 			int packetCount = 0; // Number of packet sent for the entire list
   # 			while (!sent)
   # 			{
   # 				int packetEntry = 0; // needed to tell client how much skill we send
   # 				// using pak
   # 				using (GSTCPPacketOut pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.VariousUpdate)))
   # 				{
   # 					// Write header
   # 					pak.WriteByte(0x01); //subcode for skill
   # 					pak.WriteByte((byte)0); //packet entries, can't know it for now...
   # 					pak.WriteByte((byte)0x03); //subtype for following pages
   # 					pak.WriteByte((byte)index); // packet first entry
   #
   # 					// getting pak filled
   # 					while(index < total)
   # 					{
   # 						// this item will break the limit, send the packet before, keep index as is to continue !
   # 						if ((index >= byte.MaxValue) || ((pak.Length + 8 + usableSkills[index].Item1.Name.Length) > 1400))
   # 						{
   # 							break;
   # 						}
   #
   # 						// Enter Packet Values !! Format Level - Type - SpecialField - Bonus - Icon - Name
   # 						Skill skill = usableSkills[index].Item1;
   # 						Skill skillrelated = usableSkills[index].Item2;
   #
   # 						if (skill is Specialization)
   # 						{
   # 							Specialization spec = (Specialization)skill;
   # 							pak.WriteByte((byte)Math.Max(1, spec.Level));
   # 							pak.WriteByte((byte)spec.SkillType);
   # 							pak.WriteShort(0);
   # 							pak.WriteByte((byte)(m_gameClient.Player.GetModifiedSpecLevel(spec.KeyName) - spec.Level)); // bonus
   # 							pak.WriteShort((ushort)spec.Icon);
   # 							pak.WritePascalString(spec.Name);
   # 						}
   # 						else if (skill is Ability)
   # 						{
   # 							Ability ab = (Ability)skill;
   #
   # 							pak.WriteByte((byte)0);
   # 							pak.WriteByte((byte)ab.SkillType);
   # 							pak.WriteShort(0);
   # 							pak.WriteByte((byte)0);
   # 							pak.WriteShort((ushort)ab.Icon);
   # 							pak.WritePascalString(ab.Name);
   # 						}
   # 						else if (skill is Spell)
   # 						{
   # 							Spell spell = (Spell)skill;
   # 							pak.WriteByte((byte)spell.Level);
   # 							pak.WriteByte((byte)spell.SkillType);
   #
   # 							// spec index for this Spell - Special for Song and Unknown Indexes...
   # 							int spin = 0;
   # 							if (spell.SkillType == eSkillPage.Songs)
   # 							{
   # 								spin = 0xFF;
   # 							}
   # 							else
   # 							{
   # 								// find this line Specialization index !
   # 								if (skillrelated is SpellLine && !Util.IsEmpty(((SpellLine)skillrelated).Spec))
   # 								{
   # 									spin = usableSkills.FindIndex(sk => (sk.Item1 is Specialization) && ((Specialization)sk.Item1).KeyName == ((SpellLine)skillrelated).Spec);
   #
   # 									if (spin == -1)
   # 										spin = 0xFE;
   # 								}
   # 								else
   # 								{
   # 									spin = 0xFE;
   # 								}
   # 							}
   #
   # 							pak.WriteShort((ushort)spin); // special index for spellline
   # 							pak.WriteByte(0); // bonus
   # 							pak.WriteShort(spell.InternalIconID > 0 ? spell.InternalIconID : spell.Icon); // icon
   # 							pak.WritePascalString(spell.Name);
   # 						}
   # 						else if (skill is Style)
   # 						{
   # 							Style style = (Style)skill;
   # 							pak.WriteByte((byte)style.SpecLevelRequirement);
   # 							pak.WriteByte((byte)style.SkillType);
   #
   # 							// Special pre-requisite (First byte is Pre-requisite Icon / second Byte is prerequisite code...)
   # 							int pre = 0;
   #
   # 							switch (style.OpeningRequirementType)
   # 							{
   # 								case Style.eOpening.Offensive:
   # 									pre = (int)style.AttackResultRequirement; // last result of our attack against enemy hit, miss, target blocked, target parried, ...
   # 									if (style.AttackResultRequirement == Style.eAttackResultRequirement.Style)
   # 									{
   # 										// get style requirement value... find prerequisite style index from specs beginning...
   # 										int styleindex = Math.Max(0, usableSkills.FindIndex(it => (it.Item1 is Style) && it.Item1.ID == style.OpeningRequirementValue));
   # 										int speccount = Math.Max(0, usableSkills.FindIndex(it => (it.Item1 is Specialization) == false));
   # 										pre |= ((byte)(100 + styleindex - speccount)) << 8;
   # 									}
   # 									break;
   # 								case Style.eOpening.Defensive:
   # 									pre = 100 + (int)style.AttackResultRequirement; // last result of enemies attack against us hit, miss, you block, you parry, ...
   # 									break;
   # 								case Style.eOpening.Positional:
   # 									pre = 200 + style.OpeningRequirementValue;
   # 									break;
   # 							}
   #
   # 							// style required?
   # 							if (pre == 0)
   # 								pre = 0x100;
   #
   # 							pak.WriteShort((ushort)pre);
   # 							pak.WriteByte(GlobalConstants.GetSpecToInternalIndex(style.Spec)); // index specialization in bonus...
   # 							pak.WriteShort((ushort)style.Icon);
   # 							pak.WritePascalString(style.Name);
   # 						}
   #
   # 						packetEntry++;
   # 						index++;
   # 					}
   #
   # 					// test if we finished sending packets
   # 					if (index >= total || index >= byte.MaxValue)
   # 						sent = true;
   #
   # 					// rewrite header for count.
   # 					pak.Position = 4;
   # 					pak.WriteByte((byte)packetEntry);
   #
   # 					if (!sent)
   # 						pak.WriteByte((byte)99);
   #
   # 					SendTCP(pak);
   #
   # 				}
   #
   # 				packetCount++;
   # 			}
   #
   # 			// Send List Cast Spells...
   # 			SendNonHybridSpellLines();
   # 			// reset trainer cache
   # 			m_gameClient.TrainerSkillCache = null;
   # 		}
