package handlers.client

import handlers.GameClient
import handlers.packets.PacketReader
import handlers.server.AttackMode

import scala.concurrent.Future

/**
  * Created by franblas on 28/04/17.
  */
class PlayerAttackRequest(gameClient: GameClient) extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    val mode = reader.readByte()
    val userAction = reader.readByte()

    println("MODE", mode)
    println("userAction", userAction)

    new AttackMode(mode).process()
  }
}
