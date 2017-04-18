package handlers.client

import database.Accounts
import handlers.GameClient
import handlers.packets.{PacketReader, PacketsUtils}
import handlers.server.{LoginDenied, LoginGranted}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 26/03/17.
  */
class LoginRequest(gameClient: GameClient) extends HandlerProcessor {

  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    reader.skip(2)
    val major = reader.readByte // TODO check validity of this one
    val minor = reader.readByte // TODO check validity of this one
    val build = reader.readByte // TODO check validity of this one
    val password = PacketsUtils.printableString(reader.readString(20))
    reader.skip(7)
    val c2 = reader.readInt()
    val c3 = reader.readInt()
    val c4 = reader.readInt()
    reader.skip(31)
    val username = PacketsUtils.printableString(reader.readString(20))

    // check the account into the db
    new Accounts().getAccount(username, password).flatMap(result => {
      val loginGranted = result.nonEmpty
      val version = PacketsUtils.versionBuilder(major, minor, build)
      if (loginGranted) {
        gameClient.loginName = username
        new LoginGranted(version, username).process()
      } else {
        new LoginDenied(version, 0x07).process() // 0x07, error code account not found
      }
    })
  }
}
