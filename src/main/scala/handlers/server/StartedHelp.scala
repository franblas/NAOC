package handlers.server

import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class StartedHelp {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0xF7)
    writer.writeShort(0x01)
    writer.writeShort(0x00)
    Future {
      writer.getFinalPacket()
    }
  }
}
