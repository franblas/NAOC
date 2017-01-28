from ..packets.packet_out import *

def encumberance_pak(gameclient):
	data = gameclient.selected_character
	if not data: return

	# pak.WriteShort((ushort) m_gameClient.Player.MaxEncumberance); // encumb total
	ins = write_short(0x0028) #TODO
	# pak.WriteShort((ushort) m_gameClient.Player.Encumberance); // encumb used
	ins += write_short(0x0000) #TODO

  	pak = write_short(packet_length(ins))
  	pak += write_byte(0xBD)
  	pak += ins
  	return pak
