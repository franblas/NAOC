from ..packets.packet_out import *

def update_crafting_skills_pak(gameclient):
   data = gameclient.selected_character
   if not data: return

   crafting_skills = [
      {
         'points': 0x01,
         'icon': 0x01,
         'name': 'Weaponcraft'
      },
      {
         'points': 0x01,
         'icon': 0x02,
         'name': 'Armorcraft'
      },
      {
         'points': 0x01,
         'icon': 0x03,
         'name': 'Siegecraft'
      },
      {
         'points': 0x01,
         'icon': 0x04,
         'name': 'Alchemy'
      },
      {
         'points': 0x01,
         'icon': 0x06,
         'name': 'Metalworking'
      },
      {
         'points': 0x01,
         'icon': 0x07,
         'name': 'Leathercrafting'
      },
      {
         'points': 0x01,
         'icon': 0x08,
         'name': 'Clothworking'
      },
      {
         'points': 0x01,
         'icon': 0x09,
         'name': 'Gemcutting'
      },
      {
         'points': 0x01,
         'icon': 0x0A,
         'name': 'Herbcraft'
      },
      {
         'points': 0x01,
         'icon': 0x0B,
         'name': 'Tailoring'
      },
      {
         'points': 0x01,
         'icon': 0x0C,
         'name': 'Fletching'
      },
      {
         'points': 0x01,
         'icon': 0x0D,
         'name': 'Spellcrafting'
      },
      {
         'points': 0x01,
         'icon': 0x0E,
         'name': 'Woodworking'
      },
      {
         'points': 0x01,
         'icon': 0x0F,
         'name': 'Basic Crafting'
      }
   ]

   ins = write_byte(0x08)
   ins += write_byte(len(crafting_skills))
   ins += write_byte(0x03)
   ins += write_byte(0x00)

   for c in crafting_skills:
      ins += write_short(c['points'])
      ins += write_byte(c['icon'])
      ins += write_int(1)
      ins += write_pascal_string(c['name'])

   pak = write_short(packet_length(ins))
   pak += write_byte(0x16)
   pak += ins
   return pak


# 		public virtual void SendUpdateCraftingSkills()
# 		{
# 			if (m_gameClient.Player == null)
# 				return;
#
# 			using (var pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.VariousUpdate)))
# 			{
# 				pak.WriteByte(0x08); //subcode
# 				pak.WriteByte((byte) m_gameClient.Player.CraftingSkills.Count); //count
# 				pak.WriteByte(0x03); //subtype
# 				pak.WriteByte(0x00); //unk
#
# 				foreach (KeyValuePair<eCraftingSkill, int> de in m_gameClient.Player.CraftingSkills)
# 				{
# 					AbstractCraftingSkill curentCraftingSkill = CraftingMgr.getSkillbyEnum((eCraftingSkill) de.Key);
# 					pak.WriteShort(Convert.ToUInt16(de.Value)); //points
# 					pak.WriteByte(curentCraftingSkill.Icon); //icon
# 					pak.WriteInt(1);
# 					pak.WritePascalString(curentCraftingSkill.Name); //name
# 				}
# 				SendTCP(pak);
# 			}
# 		}
