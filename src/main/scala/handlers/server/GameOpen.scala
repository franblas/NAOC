package handlers.server

import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class GameOpen {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.gameOpen)
    writer.writeByte(0x00)
    writer.toFinalFuture()
  }
}
