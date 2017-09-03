package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 07/04/17.
  */
class SessionId(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.sessionId)
    writer.writeShort(gameClient.sessionId.toShort)
    writer.toFinalFuture()
  }
}