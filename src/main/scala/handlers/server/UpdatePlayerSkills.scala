package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class UpdatePlayerSkills(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player
    if (player == null) {
      return Future { Array.emptyByteArray }
    }

    val writer = new PacketWriter(0x16)
    writer.writeByte(0x01)
    writer.writeByte(0x00)
    writer.writeByte(0x03)
    writer.writeByte(0x00)
    Future {
      writer.getFinalPacket()
    }
  }
}
