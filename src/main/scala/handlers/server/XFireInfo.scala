package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class XFireInfo(flag: Int, gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player
    if (player == null) {
      return Future { Array.emptyByteArray }
    }

    val writer = new PacketWriter(0x5C)
    //// pak.WriteShort((ushort)m_gameClient.Player.ObjectID);
    //ins = write_short(7)
    writer.writeShort(0x07)
    //// pak.WriteByte(flag);
    //ins += write_byte(flag)
    writer.writeByte(flag.toByte)
    //// pak.WriteByte(0x00);
    //ins += write_byte(0x00)
    writer.writeByte(0x00)
    Future {
      writer.getFinalPacket()
    }
  }
}