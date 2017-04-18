package handlers.server

import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 07/04/17.
  */
class Realm(realm: Int) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0xFE)
    writer.writeByte(realm.toByte)
    Future {
      writer.getFinalPacket()
    }
  }
}
