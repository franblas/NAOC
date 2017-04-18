from ..packets.packet_out import *

def weather_pak():
  # pak.WriteInt(x);
  ins = write_int(0x00)
  # pak.WriteInt(width);
  ins += write_int(0x00)
  # pak.WriteShort(fogdiffusion);
  ins += write_short(0x00)
  # pak.WriteShort(speed);
  ins += write_short(0x00)
  # pak.WriteShort(intensity);
  ins += write_short(0x00)
  # pak.WriteShort(0); # 0x0508, 0xEB51, 0xFFBF
  ins += write_short(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x92)
  pak += ins
  return pak
