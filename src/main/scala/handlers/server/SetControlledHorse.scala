package handlers.server

import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class SetControlledHorse {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0x4E)
    /*
    // if (player.HasHorse)
    // {
      // 	pak.WriteShort(0); // for set self horse OID must be zero
      // 	pak.WriteByte(player.ActiveHorse.ID);
      // 	if (player.ActiveHorse.BardingColor == 0 && player.ActiveHorse.Barding != 0 && player.Guild != null)
      // 	{
        // 		int newGuildBitMask = (player.Guild.Emblem & 0x010000) >> 9;
        // 		pak.WriteByte((byte)(player.ActiveHorse.Barding | newGuildBitMask));
        // 		pak.WriteShort((ushort)player.Guild.Emblem);
        // 	}
      // 	else
      // 	{
        // 		pak.WriteByte(player.ActiveHorse.Barding);
        // 		pak.WriteShort(player.ActiveHorse.BardingColor);
        // 	}
      // 	pak.WriteByte(player.ActiveHorse.Saddle);
      // 	pak.WriteByte(player.ActiveHorse.SaddleColor);
      // 	pak.WriteByte(player.ActiveHorse.Slots);
      // 	pak.WriteByte(player.ActiveHorse.Armor);
      // 	pak.WritePascalString(player.ActiveHorse.Name == null ? "" : player.ActiveHorse.Name);
      // }
    // else
    // {
      // 	pak.Fill(0x00, 8);
      // }
    */
    writer.fill(0x00, 8)
    Future {
      writer.getFinalPacket()
    }
  }
}
