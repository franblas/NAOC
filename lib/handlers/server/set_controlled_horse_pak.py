from ..packets.packet_out import *

def set_controlled_horse_pak():
	# if (player.HasHorse)
	# {
	# 	pak.WriteShort(0); // for set self horse OID must be zero
	# 	pak.WriteByte(player.ActiveHorse.ID);
	# 	if (player.ActiveHorse.BardingColor == 0 && player.ActiveHorse.Barding != 0 && player.Guild != null)
	# 	{
	# 		int newGuildBitMask = (player.Guild.Emblem & 0x010000) >> 9;
	# 		pak.WriteByte((byte)(player.ActiveHorse.Barding | newGuildBitMask));
	# 		pak.WriteShort((ushort)player.Guild.Emblem);
	# 	}
	# 	else
	# 	{
	# 		pak.WriteByte(player.ActiveHorse.Barding);
	# 		pak.WriteShort(player.ActiveHorse.BardingColor);
	# 	}
	# 	pak.WriteByte(player.ActiveHorse.Saddle);
	# 	pak.WriteByte(player.ActiveHorse.SaddleColor);
	# 	pak.WriteByte(player.ActiveHorse.Slots);
	# 	pak.WriteByte(player.ActiveHorse.Armor);
	# 	pak.WritePascalString(player.ActiveHorse.Name == null ? "" : player.ActiveHorse.Name);
	# }
	# else
	# {
	# 	pak.Fill(0x00, 8);
	# }
  ins = fill_pak(0x00, 8)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x4E)
  pak += ins
  return pak
