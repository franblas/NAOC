from ..packets.packet_out import *

def concentration_list_pak(gameclient):
   data = gameclient.selected_character
   if not data: return

   # 	pak.WriteByte((byte)(m_gameClient.Player.ConcentrationEffects.Count));
   # 	pak.WriteByte(0); // unknown
   # 	pak.WriteByte(0); // unknown
   # 	pak.WriteByte(0); // unknown
   ins = write_byte(0x00)
   ins += write_byte(0x00)
   ins += write_byte(0x00)
   ins += write_byte(0x00)

   pak = write_short(packet_length(ins))
   pak += write_byte(0x75)
   pak += ins
   return pak


   # 				lock (m_gameClient.Player.ConcentrationEffects)
   # 				{
   # 					pak.WriteByte((byte)(m_gameClient.Player.ConcentrationEffects.Count));
   # 					pak.WriteByte(0); // unknown
   # 					pak.WriteByte(0); // unknown
   # 					pak.WriteByte(0); // unknown
   #
   # 					for (int i = 0; i < m_gameClient.Player.ConcentrationEffects.Count; i++)
   # 					{
   # 						IConcentrationEffect effect = m_gameClient.Player.ConcentrationEffects[i];
   # 						pak.WriteByte((byte)i);
   # 						pak.WriteByte(0); // unknown
   # 						pak.WriteByte(effect.Concentration);
   # 						pak.WriteShort(effect.Icon);
   # 						if (effect.Name.Length > 14)
   # 							pak.WritePascalString(effect.Name.Substring(0, 12) + "..");
   # 						else
   # 							pak.WritePascalString(effect.Name);
   # 						if (effect.OwnerName.Length > 14)
   # 							pak.WritePascalString(effect.OwnerName.Substring(0, 12) + "..");
   # 						else
   # 							pak.WritePascalString(effect.OwnerName);
   # 					}
   # 				}
