from ..packets.packet_out import *

def living_equipment_update_pak(npc, gameclient):
   data = gameclient.selected_character
   if not data: return

   # pak.WriteShort((ushort)living.ObjectID);
   ins = write_short(npc['object_id'])
   # pak.WriteByte((byte)living.VisibleActiveWeaponSlots);
   ins += write_byte(0x00)
   # pak.WriteByte((byte)living.CurrentSpeed); // new in 189b+, speed
   ins += write_byte(0x00)
   # pak.WriteByte((byte)((living.IsCloakInvisible ? 0x01 : 0x00) | (living.IsHelmInvisible ? 0x02 : 0x00))); // new in 189b+, cloack/helm visibility
   ins += write_byte(0x00)
   # pak.WriteByte((byte)((living.IsCloakHoodUp ? 0x01 : 0x00) | (int)living.ActiveQuiverSlot)); //bit0 is hood up bit4 to 7 is active quiver
   ins += write_byte(0x00)

   items = npc['inventory']['visible_items']
   if items:
      print 'Get items'
      #TODO
   else:
      ins += write_byte(0x00)

   pak = write_short(packet_length(ins))
   pak += write_byte(0x15)
   pak += ins
   return pak

   # 				ICollection<InventoryItem> items = null;
   # 				if (living.Inventory != null)
   # 					items = living.Inventory.VisibleItems;
   #
   # 				pak.WriteShort((ushort)living.ObjectID);
   # 				pak.WriteByte((byte)living.VisibleActiveWeaponSlots);
   # 				pak.WriteByte((byte)living.CurrentSpeed); // new in 189b+, speed
   # 				pak.WriteByte((byte)((living.IsCloakInvisible ? 0x01 : 0x00) | (living.IsHelmInvisible ? 0x02 : 0x00))); // new in 189b+, cloack/helm visibility
   # 				pak.WriteByte((byte)((living.IsCloakHoodUp ? 0x01 : 0x00) | (int)living.ActiveQuiverSlot)); //bit0 is hood up bit4 to 7 is active quiver
   #
   # 				if (items != null)
   # 				{
   # 					pak.WriteByte((byte)items.Count);
   # 					foreach (InventoryItem item in items)
   # 					{
   # 						ushort model = (ushort)(item.Model & 0x1FFF);
   # 						int slot = item.SlotPosition;
   # 						//model = GetModifiedModel(model);
   # 						int texture = item.Emblem != 0 ? item.Emblem : item.Color;
   # 						if (item.SlotPosition == Slot.LEFTHAND || item.SlotPosition == Slot.CLOAK) // for test only cloack and shield
   # 							slot = slot | ((texture & 0x010000) >> 9); // slot & 0x80 if new emblem
   # 						pak.WriteByte((byte)slot);
   # 						if ((texture & ~0xFF) != 0)
   # 							model |= 0x8000;
   # 						else if ((texture & 0xFF) != 0)
   # 							model |= 0x4000;
   # 						if (item.Effect != 0)
   # 							model |= 0x2000;
   #
   # 						pak.WriteShort(model);
   #
   # 						if (item.SlotPosition > Slot.RANGED || item.SlotPosition < Slot.RIGHTHAND)
   # 							pak.WriteByte((byte)item.Extension);
   #
   # 						if ((texture & ~0xFF) != 0)
   # 							pak.WriteShort((ushort)texture);
   # 						else if ((texture & 0xFF) != 0)
   # 							pak.WriteByte((byte)texture);
   # 						if (item.Effect != 0)
   # 							pak.WriteByte((byte)item.Effect);
   # 					}
   # 				}
   # 				else
   # 				{
   # 					pak.WriteByte(0x00);
   # 				}
   # 				SendTCP(pak);
