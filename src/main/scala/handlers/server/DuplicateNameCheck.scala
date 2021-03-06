package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 08/04/17.
  */
class DuplicateNameCheck(characterName: String, alreadyExists: Boolean, gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.duplicateNameCheck)
    val loginName = gameClient.loginName
    writer.fillString(characterName, 30)
    writer.fillString(loginName, 24)
    if (alreadyExists) {
      writer.writeByte(0x01)
    } else {
      writer.writeByte(0x00)
    }
    writer.fill(0x00, 3)
    writer.toFinalFuture()
  }
}

