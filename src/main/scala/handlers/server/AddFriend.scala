package handlers.server

import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class AddFriend {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0xC5)
    writer.writeByte(0x00)
    Future {
      writer.getFinalPacket()
    }
  }
}
