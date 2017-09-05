package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class NonHybridSpellLines(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    gameClient.player.map(_ => compute()).getOrElse(Future { Array.emptyByteArray })
  }

  private def compute(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.nonHybridSpellLines)
    writer.writeByte(0x02)
    writer.writeByte(0x00)
    writer.writeByte(0x63)
    writer.writeByte(0x00)
    writer.toFinalFuture()
  }
}
