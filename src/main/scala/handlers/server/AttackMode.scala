package handlers.server

import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 28/04/17.
  */
class AttackMode(attackState: Byte) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0x74)
    writer.writeByte(attackState)
    writer.fill(0x00, 3)
    Future {
      writer.getFinalPacket()
    }
  }
}
