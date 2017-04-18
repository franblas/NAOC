from ..packets.packet_out import *

def player_free_level_update_pak():
  # pak.WriteShort((ushort)player.ObjectID);
  ins = write_short(7)
  # pak.WriteByte(0x09); # subcode
  ins += write_byte(0x09)
  # byte flag = player.FreeLevelState;
  # TimeSpan t = new TimeSpan((long)(DateTime.Now.Ticks - player.LastFreeLeveled.Ticks));
  # ushort time = 0;
  # #time is in minutes
  # switch (player.Realm)
  # {
  # 	case eRealm.Albion:
  # 		time = (ushort)((ServerProperties.Properties.FREELEVEL_DAYS_ALBION * 24 * 60) - t.TotalMinutes);
  # 		break;
  # 	case eRealm.Midgard:
  # 		time = (ushort)((ServerProperties.Properties.FREELEVEL_DAYS_MIDGARD * 24 * 60) - t.TotalMinutes);
  # 		break;
  # 	case eRealm.Hibernia:
  # 		time = (ushort)((ServerProperties.Properties.FREELEVEL_DAYS_HIBERNIA * 24 * 60) - t.TotalMinutes);
  # 		break;
  # }
  # #flag 1 = above level, 2 = elligable, 3= time until, 4 = level and time until, 5 = level until
  # pak.WriteByte(flag); #flag
  ins += write_byte(0x04)
  # pak.WriteShort(0); #unknown
  ins += write_short(0x00)
  # pak.WriteShort(time); #time
  time = 0x275f
  ins += write_short(time)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x4C)
  pak += ins
  return pak
