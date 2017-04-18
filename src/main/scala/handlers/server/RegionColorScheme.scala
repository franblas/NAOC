package handlers.server

import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class RegionColorScheme(color: Int) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0x4C)
    writer.writeShort(0x00)
    writer.writeByte(0x05)
    writer.writeByte(color.toByte)
    writer.writeInt(0x00)
    Future {
      writer.getFinalPacket()
    }
  }
}
