package handlers.server

import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 07/04/17.
  */
class Realm(realm: Int) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.realm)
    writer.writeByte(realm.toByte)
    writer.toFinalFuture()
  }
}
