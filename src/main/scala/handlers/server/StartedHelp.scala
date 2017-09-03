package handlers.server

import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class StartedHelp {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.startedHelp)
    writer.writeShort(0x01)
    writer.writeShort(0x00)
    writer.toFinalFuture()
  }
}
