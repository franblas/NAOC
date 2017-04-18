package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 07/04/17.
  */
class SessionId(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(0x28)
    writer.writeShort(gameClient.sessionId.toShort)
    Future {
      writer.getFinalPacket()
    }
  }
}