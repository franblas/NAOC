package handlers.server

import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 26/03/17.
  */
class PingReply(timestamp: Int, sequence: Int) {

  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.pingReply)
    writer.writeInt(timestamp)
    writer.fill(0x00, 4)
    writer.writeShort((sequence+1).toShort)
    writer.fill(0x00, 6)
    writer.toFinalFuture()
  }
}

