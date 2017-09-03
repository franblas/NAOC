package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class PlayerInitFinished(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.playerInitFinished)
    writer.writeByte(0x00)
    gameClient.player.enteredGame = true
    writer.toFinalFuture()
  }
}
