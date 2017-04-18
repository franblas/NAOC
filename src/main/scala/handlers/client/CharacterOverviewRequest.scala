package handlers.client

import handlers.GameClient
import handlers.packets.PacketReader
import handlers.server.{CharacterOverview, Realm}

import scala.concurrent.Future

/**
  * Created by franblas on 07/04/17.
  */
class CharacterOverviewRequest(gameClient: GameClient) extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    val accountName = reader.readString(24)
    if (accountName.contains(accountName.split("-")(0) + "-X")) {
      println("No realm (multiple account selection)")
      return new Realm(0x00).process() // No realm (multiple account selection)
    }

    if (accountName.endsWith("-S")) {
      println("Albion")
      new CharacterOverview(0x01, gameClient).process()
    } else if (accountName.endsWith("-N")) {
      println("Midgard")
      new CharacterOverview(0x02, gameClient).process()
    } else if (accountName.endsWith("-H")) {
      println("Hibernia")
      new CharacterOverview(0x03, gameClient).process()
    } else {
      println("Unknown realm")
      Future.failed(new Exception("Unknown realm"))
    }
  }
}
