package handlers.server

import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 28/04/17.
  */
class AttackMode(attackState: Byte) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.attackMode)
    writer.writeByte(attackState)
    writer.fill(0x00, 3)
    writer.toFinalFuture()
  }
}
