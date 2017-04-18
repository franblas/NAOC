package handlers.server

import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class DoorState(doorId: Int, doorState: Byte) {
  def process(): Future[Array[Byte]] = {
    val zone = doorId / 1000000
    val doorType = doorId / 100000000
    val flag = 0x01

    val writer = new PacketWriter(0x99)
    writer.writeInt(doorId)
    writer.writeByte(doorState)
    writer.writeByte(flag.toByte)
    writer.writeByte(0xFF.toByte)
    writer.writeByte(0x00)
    Future {
      writer.getFinalPacket()
    }
  }
}