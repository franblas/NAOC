from ..packets.packet_out import *
from ...database.db_classes import get_class
from ...database.db_races import get_race

def update_player_pak(gameclient):
   loaded_character = gameclient.selected_character
   if not loaded_character: return

   data = gameclient.player.db_character

   ins = write_byte(0x03)
   ins += write_byte(0x0F)
   ins += write_byte(0x00)
   ins += write_byte(0x00)

   # 	pak.WriteByte(player.GetDisplayLevel(m_gameClient.Player)); //level
   ins += write_byte(data['level'])

   # 	pak.WritePascalString(player.Name); // player name
   ins += write_pascal_string(data['name'])

   # 	pak.WriteByte((byte) (player.MaxHealth >> 8)); // maxhealth high byte ?
   ins += write_byte(0x00)

   char_class = get_class(data['char_class'])

   # 	pak.WritePascalString(player.CharacterClass.Name); // class name
   ins += write_pascal_string(char_class['char_class_name'])

   # 	pak.WriteByte((byte) (player.MaxHealth & 0xFF)); // maxhealth low byte ?
   ins += write_byte(0x1E)

   # 	pak.WritePascalString( /*"The "+*/player.CharacterClass.Profession); // Profession
   ins += write_pascal_string(char_class['profession'])

   # 	pak.WriteByte(0x00); //unk
   ins += write_byte(0x00)

   #  pak.WritePascalString(player.CharacterClass.GetTitle(player, player.Level)); // player level
   ins += write_pascal_string('none')

   # 	//todo make function to calcule realm rank
   # 	//client.Player.RealmPoints
   # 	//todo i think it s realmpoint percent not realrank
   # 	pak.WriteByte((byte) player.RealmLevel); //urealm rank
   ins += write_byte(0x00)

   # 	pak.WritePascalString(player.RealmRankTitle(player.Client.Account.Language)); // Realm title
   ins += write_pascal_string('Defender')

   # 	pak.WriteByte((byte) player.RealmSpecialtyPoints); // realm skill points
   ins += write_byte(0x00)

   # 	pak.WritePascalString(player.CharacterClass.BaseName); // base class
   ins += write_pascal_string(char_class['base'])

   # 	pak.WriteByte((byte)(HouseMgr.GetHouseNumberByPlayer(player) >> 8)); // personal house high byte
   ins += write_byte(0x00)

   # 	pak.WritePascalString(player.GuildName); // Guild name
   ins += write_pascal_string('')

   # 	pak.WriteByte((byte)(HouseMgr.GetHouseNumberByPlayer(player) & 0xFF)); // personal house low byte
   ins += write_byte(0x00)

   # 	pak.WritePascalString(player.LastName); // Last name
   ins += write_pascal_string('')

   # 	pak.WriteByte((byte)(player.MLLevel+1)); // ML Level (+1)
   ins += write_byte(0x01)

   char_race = get_class(data['race'])

   # 	pak.WritePascalString(player.RaceName); // Race name
   ins += write_pascal_string(char_race['name'])

   # 	pak.WriteByte(0x0);
   ins += write_byte(0x00)

   # 	if (player.GuildRank != null)
   # 		pak.WritePascalString(player.GuildRank.Title); // Guild title
   # 	else
   # 		pak.WritePascalString("");
   ins += write_pascal_string('')

   # 	pak.WriteByte(0x0);
   ins += write_byte(0x00)

   # 	AbstractCraftingSkill skill = CraftingMgr.getSkillbyEnum(player.CraftingPrimarySkill);
   # 	if (skill != null)
   # 		pak.WritePascalString(skill.Name); //crafter guilde: alchemist
   # 	else
   # 		pak.WritePascalString("None"); //no craft skill at start
   ins += write_pascal_string('Basic Crafting')

   # 	pak.WriteByte(0x0);
   ins += write_byte(0x00)

   # 	pak.WritePascalString(player.CraftTitle.GetValue(player, player)); //crafter title: legendary alchemist
   ins += write_pascal_string('Basic crafter\'s Helper')

   # 	pak.WriteByte(0x0);
   ins += write_byte(0x00)

   # 	pak.WritePascalString(player.MLTitle.GetValue(player, player)); //ML title
   ins += write_pascal_string('')

   # 	// new in 1.75
   # 	pak.WriteByte(0x0);
   ins += write_byte(0x00)

   # 	if (player.CurrentTitle != PlayerTitleMgr.ClearTitle)
   # 		pak.WritePascalString(player.CurrentTitle.GetValue(player, player)); // new in 1.74 - Custom title
   # 	else
   # 		pak.WritePascalString("None");
   write_pascal_string('None')

   # 	// new in 1.79
   # 	if(player.Champion)
   # 		pak.WriteByte((byte)(player.ChampionLevel+1)); // Champion Level (+1)
   # 	else
   # 		pak.WriteByte(0x0);
   ins += write_byte(0x00)

   # 	pak.WritePascalString(player.CLTitle.GetValue(player, player)); // Champion Title
   ins += write_pascal_string('')

   pak = write_short(packet_length(ins))
   pak += write_byte(0x16)
   pak += ins
   return pak



# p
# 		public override void SendUpdatePlayer()
# 		{
# 			GamePlayer player = m_gameClient.Player;
# 			if (player == null)
# 				return;
#
# 			using (GSTCPPacketOut pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.VariousUpdate)))
# 			{
# 				pak.WriteByte(0x03); //subcode
# 				pak.WriteByte(0x0f); //number of entry
# 				pak.WriteByte(0x00); //subtype
# 				pak.WriteByte(0x00); //unk
# 				//entry :
#
# 				pak.WriteByte(player.GetDisplayLevel(m_gameClient.Player)); //level
# 				pak.WritePascalString(player.Name); // player name
# 				pak.WriteByte((byte) (player.MaxHealth >> 8)); // maxhealth high byte ?
# 				pak.WritePascalString(player.CharacterClass.Name); // class name
# 				pak.WriteByte((byte) (player.MaxHealth & 0xFF)); // maxhealth low byte ?
# 				pak.WritePascalString( /*"The "+*/player.CharacterClass.Profession); // Profession
# 				pak.WriteByte(0x00); //unk
# 	            pak.WritePascalString(player.CharacterClass.GetTitle(player, player.Level)); // player level
# 				//todo make function to calcule realm rank
# 				//client.Player.RealmPoints
# 				//todo i think it s realmpoint percent not realrank
# 				pak.WriteByte((byte) player.RealmLevel); //urealm rank
# 				pak.WritePascalString(player.RealmRankTitle(player.Client.Account.Language)); // Realm title
# 				pak.WriteByte((byte) player.RealmSpecialtyPoints); // realm skill points
# 				pak.WritePascalString(player.CharacterClass.BaseName); // base class
# 				pak.WriteByte((byte)(HouseMgr.GetHouseNumberByPlayer(player) >> 8)); // personal house high byte
# 				pak.WritePascalString(player.GuildName); // Guild name
# 				pak.WriteByte((byte)(HouseMgr.GetHouseNumberByPlayer(player) & 0xFF)); // personal house low byte
# 				pak.WritePascalString(player.LastName); // Last name
# 				pak.WriteByte((byte)(player.MLLevel+1)); // ML Level (+1)
# 				pak.WritePascalString(player.RaceName); // Race name
# 				pak.WriteByte(0x0);
#
# 				if (player.GuildRank != null)
# 					pak.WritePascalString(player.GuildRank.Title); // Guild title
# 				else
# 					pak.WritePascalString("");
# 				pak.WriteByte(0x0);
#
# 				AbstractCraftingSkill skill = CraftingMgr.getSkillbyEnum(player.CraftingPrimarySkill);
# 				if (skill != null)
# 					pak.WritePascalString(skill.Name); //crafter guilde: alchemist
# 				else
# 					pak.WritePascalString("None"); //no craft skill at start
#
# 				pak.WriteByte(0x0);
# 				pak.WritePascalString(player.CraftTitle.GetValue(player, player)); //crafter title: legendary alchemist
# 				pak.WriteByte(0x0);
# 				pak.WritePascalString(player.MLTitle.GetValue(player, player)); //ML title
#
# 				// new in 1.75
# 				pak.WriteByte(0x0);
# 				if (player.CurrentTitle != PlayerTitleMgr.ClearTitle)
# 					pak.WritePascalString(player.CurrentTitle.GetValue(player, player)); // new in 1.74 - Custom title
# 				else
# 					pak.WritePascalString("None");
#
# 				// new in 1.79
# 				if(player.Champion)
# 					pak.WriteByte((byte)(player.ChampionLevel+1)); // Champion Level (+1)
# 				else
# 					pak.WriteByte(0x0);
# 				pak.WritePascalString(player.CLTitle.GetValue(player, player)); // Champion Title
# 				SendTCP(pak);
# 			}
# 		}
