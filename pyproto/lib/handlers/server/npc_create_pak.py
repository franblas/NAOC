from ..packets.packet_out import *

def npc_create_pak(npc, gameclient):
   data = gameclient.selected_character
   if not data: return

   if not npc: return

   # speed = 0
   speed_z = 0
   # pak.WriteShort((ushort)npc.ObjectID);
   ins = write_short(npc.object_id)

   # pak.WriteShort((ushort)(speed));
   speed = npc.speed
   if speed:
      ins += write_short(speed)
   else:
      ins += write_short(0)

   # pak.WriteShort(npc.Heading);
   ins += write_short(npc.heading)
   # pak.WriteShort((ushort)npc.Z);
   ins += write_short(npc.Z)
   # pak.WriteInt((uint)npc.X);
   ins += write_int(npc.X)
   # pak.WriteInt((uint)npc.Y);
   ins += write_int(npc.Y)
   # pak.WriteShort(speedZ);
   ins += write_short(speed_z)
   # pak.WriteShort(npc.Model);
   ins += write_short(npc.model)
   # pak.WriteByte(npc.Size);
   ins += write_byte(npc.size)

   # byte level = npc.GetDisplayLevel(m_gameClient.Player);
   # level = 0x01

   # 	if((npc.Flags&GameNPC.eFlags.STATUE)!=0)
   # 	{
   # 		level |= 0x80;
   # 	}
   # 	pak.WriteByte(level);
   # ins += write_byte(npc.get('level', level))
   level = npc.level
   if level:
      ins += write_byte(level)
   else:
      ins += write_byte(1)

   # 	byte flags = (byte)(GameServer.ServerRules.GetLivingRealm(m_gameClient.Player, npc) << 6);
   # 	if ((npc.Flags & GameNPC.eFlags.GHOST) != 0) flags |= 0x01;
   # 	if (npc.Inventory != null) flags |= 0x02; #If mob has equipment, then only show it after the client gets the 0xBD packet
   # 	if ((npc.Flags & GameNPC.eFlags.PEACE) != 0) flags |= 0x10;
   # 	if ((npc.Flags & GameNPC.eFlags.FLYING) != 0) flags |= 0x20;
   # 	if((npc.Flags & GameNPC.eFlags.TORCH) != 0) flags |= 0x04;
   #
   # 	pak.WriteByte(flags);
   realm = npc.realm
   if not realm: realm = 0

   flags = npc.flags
   eflags = npc.eflags
   if flags:
      new_flags = realm << 6 #flags << 6
      if flags & eflags.get('ghost') != 0: new_flags |= 0x01
      if flags & eflags.get('peace') != 0: new_flags |= 0x10
      if flags & eflags.get('flying') != 0: new_flags |= 0x20
      if flags & eflags.get('torch') != 0: new_flags |= 0x04
      ins += write_byte(new_flags & 0xFF)
   else:
      ins += write_byte(0)

   # 	pak.WriteByte(0x20); #TODO this is the default maxstick distance
   ins += write_byte(0x20)

   # 	string add = "";
   # 	byte flags2 = 0x00;
   # 	IControlledBrain brain = npc.Brain as IControlledBrain;
   # 	if (m_gameClient.Version >= GameClient.eClientVersion.Version187)
   # 	{
   # 		if (brain != null)
   # 		{
   # 			flags2 |= 0x80; # have Owner
   # 		}
   # 	}
   # 	if ((npc.Flags & GameNPC.eFlags.CANTTARGET) != 0)
   # 		if (m_gameClient.Account.PrivLevel > 1) add += "-DOR"; # indicates DOR flag for GMs
   # 	else flags2 |= 0x01;
   # 	if ((npc.Flags & GameNPC.eFlags.DONTSHOWNAME) != 0)
   # 		if (m_gameClient.Account.PrivLevel > 1) add += "-NON"; # indicates NON flag for GMs
   # 	else flags2 |= 0x02;
   #
   # 	if( ( npc.Flags & GameNPC.eFlags.STEALTH ) > 0 )
   # 		flags2 |= 0x04;
   #
   # 	eQuestIndicator questIndicator = npc.GetQuestIndicator(m_gameClient.Player);
   #
   # 	if (questIndicator == eQuestIndicator.Available)
   # 		flags2 |= 0x08;#hex 8 - quest available
   # 	if (questIndicator == eQuestIndicator.Finish)
   # 		flags2 |= 0x10;#hex 16 - quest finish
   # 	#flags2 |= 0x20;#hex 32 - water mob?
   # 	#flags2 |= 0x40;#hex 64 - unknown
   # 	#flags2 |= 0x80;#hex 128 - has owner
   #
   #
   # 	pak.WriteByte(flags2); # flags 2
   flags2 = 0x00
   ins += write_byte(flags2)

   # 	byte flags3 = 0x00;
   # 	if (questIndicator == eQuestIndicator.Lesson)
   # 		flags3 |= 0x01;
   # 	if (questIndicator == eQuestIndicator.Lore)
   # 		flags3 |= 0x02;
   # 	pak.WriteByte(flags3); # new in 1.71 (region instance ID from StoC_0x20) OR flags 3?
   flags3 = 0x00
   ins += write_byte(flags3)

   # 	pak.WriteShort(0x00); # new in 1.71 unknown
   ins += write_short(0x00)

   # 	string name = npc.Name;
   # 	string guildName = npc.GuildName;
   #
   # 	LanguageDataObject translation = LanguageMgr.GetTranslation(m_gameClient, npc);
   # 	if (translation != null)
   # 	{
   # 		if (!Util.IsEmpty(((DBLanguageNPC)translation).Name))
   # 			name = ((DBLanguageNPC)translation).Name;
   #
   # 		if (!Util.IsEmpty(((DBLanguageNPC)translation).GuildName))
   # 			guildName = ((DBLanguageNPC)translation).GuildName;
   # 	}
   #
   # 	if (name.Length + add.Length + 2 > 47) # clients crash with too long names
   # 		name = name.Substring(0, 47 - add.Length - 2);
   # 	if (add.Length > 0)
   # 		name = string.Format("[{0}]{1}", name, add);
   #
   # 	pak.WritePascalString(name);
   name = npc.name
   ins += write_pascal_string(name)

   # 	if (guildName.Length > 47)
   # 		pak.WritePascalString(guildName.Substring(0, 47));
   # 	else pak.WritePascalString(guildName);
   guild_name = npc.guild
   if not guild_name: guild_name = ''
   # guild_name = '' #npc['guild']
   if len(guild_name) > 47: guild_name = guild_name[:47]
   ins += write_pascal_string(guild_name)

   # 	pak.WriteByte(0x00);
   ins += write_byte(0x00)

   pak = write_short(packet_length(ins))
   pak += write_byte(0xDA)
   pak += ins
   return pak

   # 			using (GSTCPPacketOut pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.NPCCreate)))
   # 			{
   # 				int speed = 0;
   # 				ushort speedZ = 0;
   # 				if (npc == null)
   # 					return;
   # 				if (!npc.IsAtTargetPosition)
   # 				{
   # 					speed = npc.CurrentSpeed;
   # 					speedZ = (ushort)npc.TickSpeedZ;
   # 				}
   # 				pak.WriteShort((ushort)npc.ObjectID);
   # 				pak.WriteShort((ushort)(speed));
   # 				pak.WriteShort(npc.Heading);
   # 				pak.WriteShort((ushort)npc.Z);
   # 				pak.WriteInt((uint)npc.X);
   # 				pak.WriteInt((uint)npc.Y);
   # 				pak.WriteShort(speedZ);
   # 				pak.WriteShort(npc.Model);
   # 				pak.WriteByte(npc.Size);
   # 				byte level = npc.GetDisplayLevel(m_gameClient.Player);
   # 				if((npc.Flags&GameNPC.eFlags.STATUE)!=0)
   # 				{
   # 					level |= 0x80;
   # 				}
   # 				pak.WriteByte(level);
   #
   # 				byte flags = (byte)(GameServer.ServerRules.GetLivingRealm(m_gameClient.Player, npc) << 6);
   # 				if ((npc.Flags & GameNPC.eFlags.GHOST) != 0) flags |= 0x01;
   # 				if (npc.Inventory != null) flags |= 0x02; #If mob has equipment, then only show it after the client gets the 0xBD packet
   # 				if ((npc.Flags & GameNPC.eFlags.PEACE) != 0) flags |= 0x10;
   # 				if ((npc.Flags & GameNPC.eFlags.FLYING) != 0) flags |= 0x20;
   # 				if((npc.Flags & GameNPC.eFlags.TORCH) != 0) flags |= 0x04;
   #
   # 				pak.WriteByte(flags);
   # 				pak.WriteByte(0x20); #TODO this is the default maxstick distance
   #
   # 				string add = "";
   # 				byte flags2 = 0x00;
   # 				IControlledBrain brain = npc.Brain as IControlledBrain;
   # 				if (m_gameClient.Version >= GameClient.eClientVersion.Version187)
   # 				{
   # 					if (brain != null)
   # 					{
   # 						flags2 |= 0x80; # have Owner
   # 					}
   # 				}
   # 				if ((npc.Flags & GameNPC.eFlags.CANTTARGET) != 0)
   # 					if (m_gameClient.Account.PrivLevel > 1) add += "-DOR"; # indicates DOR flag for GMs
   # 				else flags2 |= 0x01;
   # 				if ((npc.Flags & GameNPC.eFlags.DONTSHOWNAME) != 0)
   # 					if (m_gameClient.Account.PrivLevel > 1) add += "-NON"; # indicates NON flag for GMs
   # 				else flags2 |= 0x02;
   #
   # 				if( ( npc.Flags & GameNPC.eFlags.STEALTH ) > 0 )
   # 					flags2 |= 0x04;
   #
   # 				eQuestIndicator questIndicator = npc.GetQuestIndicator(m_gameClient.Player);
   #
   # 				if (questIndicator == eQuestIndicator.Available)
   # 					flags2 |= 0x08;#hex 8 - quest available
   # 				if (questIndicator == eQuestIndicator.Finish)
   # 					flags2 |= 0x10;#hex 16 - quest finish
   # 				#flags2 |= 0x20;#hex 32 - water mob?
   # 				#flags2 |= 0x40;#hex 64 - unknown
   # 				#flags2 |= 0x80;#hex 128 - has owner
   #
   #
   # 				pak.WriteByte(flags2); # flags 2
   #
   # 				byte flags3 = 0x00;
   # 				if (questIndicator == eQuestIndicator.Lesson)
   # 					flags3 |= 0x01;
   # 				if (questIndicator == eQuestIndicator.Lore)
   # 					flags3 |= 0x02;
   # 				pak.WriteByte(flags3); # new in 1.71 (region instance ID from StoC_0x20) OR flags 3?
   # 				pak.WriteShort(0x00); # new in 1.71 unknown
   #
   # 				string name = npc.Name;
   # 				string guildName = npc.GuildName;
   #
   # 				LanguageDataObject translation = LanguageMgr.GetTranslation(m_gameClient, npc);
   # 				if (translation != null)
   # 				{
   # 					if (!Util.IsEmpty(((DBLanguageNPC)translation).Name))
   # 						name = ((DBLanguageNPC)translation).Name;
   #
   # 					if (!Util.IsEmpty(((DBLanguageNPC)translation).GuildName))
   # 						guildName = ((DBLanguageNPC)translation).GuildName;
   # 				}
   #
   # 				if (name.Length + add.Length + 2 > 47) # clients crash with too long names
   # 					name = name.Substring(0, 47 - add.Length - 2);
   # 				if (add.Length > 0)
   # 					name = string.Format("[{0}]{1}", name, add);
   #
   # 				pak.WritePascalString(name);
   #
   # 				if (guildName.Length > 47)
   # 					pak.WritePascalString(guildName.Substring(0, 47));
   # 				else pak.WritePascalString(guildName);
   #
   # 				pak.WriteByte(0x00);
   # 				SendTCP(pak);
   # 			}
   #
   # 			# Update Cache
   # 			m_gameClient.GameObjectUpdateArray[new Tuple<ushort, ushort>(npc.CurrentRegionID, (ushort)npc.ObjectID)] = 0;
   # 		}
