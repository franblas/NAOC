from ..packets.packet_out import *

def non_hybrid_spell_lines_pak(gameclient):
   data = gameclient.selected_character
   if not data: return

   ins = write_byte(0x02)
   ins += write_byte(0x00)
   ins += write_byte(0x63)
   ins += write_byte(0x00)

   pak = write_short(packet_length(ins))
   pak += write_byte(0x16)
   pak += ins
   return pak
