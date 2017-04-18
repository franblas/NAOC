package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class Dialog(code: Int, data1: Int, data2: Int, data3: Int, data4: Int, dialogType: Int, autoWrapText: Boolean, msg: String, gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player
    if (player == null) {
      return Future { Array.emptyByteArray }
    }

    val writer = new PacketWriter(0x81)
    writer.writeByte(0x00)
    writer.writeByte(code.toByte)
    writer.writeShort(data1.toShort)
    writer.writeShort(data2.toShort)
    writer.writeShort(data3.toShort)
    writer.writeShort(data4.toShort)
    writer.writeByte(dialogType.toByte)
    writer.writeByte(if (autoWrapText) 0x01 else 0x00)
    if (msg.length > 0) writer.writeString(msg)
    writer.writeByte(0x00)
    Future {
      writer.getFinalPacket()
    }
  }
}