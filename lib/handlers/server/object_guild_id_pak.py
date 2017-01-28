from ..packets.packet_out import *

def object_guild_id_pak():
  # pak.WriteShort((ushort) obj.ObjectID);
  ins = write_short(0x07)
  # if (guild == null)
  #   pak.WriteInt(0x00);
  # else
  # {
  #   pak.WriteShort(guild.ID);
  #   pak.WriteShort(guild.ID);
  # }
  ins += write_int(0x00)
  # pak.WriteShort(0x00); //seems random, not used by the client
  ins += write_short(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xDE)
  pak += ins
  return pak
