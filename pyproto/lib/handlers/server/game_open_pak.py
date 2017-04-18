from ..packets.packet_out import *

def game_open_pak():
  ins = write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x2D)
  pak += ins
  return pak

# client.Out.SendStatusUpdate(); # based on 1.74 logs
# client.Out.SendUpdatePoints(); # based on 1.74 logs
# if (client.Player != null)
# 	client.Player.UpdateDisabledSkills(); # based on 1.74 logs
