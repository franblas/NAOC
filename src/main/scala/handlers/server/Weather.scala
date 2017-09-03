package handlers.server

import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class Weather {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.weather)
    writer.writeInt(0x00)
    writer.writeInt(0x00)
    writer.writeShort(0x00)
    writer.writeShort(0x00)
    writer.writeShort(0x00)
    writer.writeShort(0x00)
    writer.toFinalFuture()
  }
}
