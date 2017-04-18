package handlers.client

import handlers.GameClient
import handlers.packets.PacketReader
import handlers.server.DuplicateNameCheck

import scala.concurrent.Future

/**
  * Created by franblas on 08/04/17.
  */
class DuplicateNameCheckRequest(gameClient: GameClient) extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    val characterName = reader.readString(30)
    // TODO check if name already exists in the db
    val alreadyExists = false
    new DuplicateNameCheck(characterName, alreadyExists, gameClient).process()
  }
}
