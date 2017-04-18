package handlers.server

import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class PlayerFreeLevelUpdate {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0x4C)

    //// pak.WriteShort((ushort)player.ObjectID);
    //ins = write_short(7)
    writer.writeShort(0x07)
    //// pak.WriteByte(0x09); // subcode
    //ins += write_byte(0x09)
    writer.writeByte(0x09)
    /*
    // byte flag = player.FreeLevelState;
    // TimeSpan t = new TimeSpan((long)(DateTime.Now.Ticks - player.LastFreeLeveled.Ticks));
    // ushort time = 0;
    // //time is in minutes
    // switch (player.Realm)
    // {
      // 	case eRealm.Albion:
      // 		time = (ushort)((ServerProperties.Properties.FREELEVEL_DAYS_ALBION * 24 * 60) - t.TotalMinutes);
      // 		break;
      // 	case eRealm.Midgard:
      // 		time = (ushort)((ServerProperties.Properties.FREELEVEL_DAYS_MIDGARD * 24 * 60) - t.TotalMinutes);
      // 		break;
      // 	case eRealm.Hibernia:
      // 		time = (ushort)((ServerProperties.Properties.FREELEVEL_DAYS_HIBERNIA * 24 * 60) - t.TotalMinutes);
      // 		break;
      // }
    // //flag 1 = above level, 2 = elligable, 3= time until, 4 = level and time until, 5 = level until
    // pak.WriteByte(flag); //flag
    ins += write_byte(0x04)
    */
    writer.writeByte(0x04)
    //// pak.WriteShort(0); //unknown
    //ins += write_short(0x00)
    writer.writeShort(0x00)
    //// pak.WriteShort(time); //time
    //time = 0x275f
    //ins += write_short(time)
    writer.writeShort(0x275F)
    Future {
      writer.getFinalPacket()
    }
  }
}
