package handlers.server

import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class RegionColorScheme(color: Int) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.regionColorScheme)
    writer.writeShort(0x00)
    writer.writeByte(0x05)
    writer.writeByte(color.toByte)
    writer.writeInt(0x00)
    writer.toFinalFuture()
  }
}
