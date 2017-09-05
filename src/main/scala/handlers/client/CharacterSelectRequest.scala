package handlers.client

import database.Characters
import gameobjects.GamePlayer
import handlers.GameClient
import handlers.packets.PacketReader
import handlers.server.SessionId

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 07/04/17.
  */
class CharacterSelectRequest(gameClient: GameClient) extends HandlerProcessor {
  val character = new Characters()

  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    reader.skip(4)
    val charName = reader.readString(28).replace("*", "")
    if (charName == null || charName == "" || charName.length < 3) {
      Future {
        Array.emptyByteArray
      }
    } else {
      (if (charName != "noname") {
        character.getCharacter(gameClient.loginName, charName).flatMap(result => {
          if (result.nonEmpty) {
            gameClient.player = Some(new GamePlayer(result.head))
            gameClient.player.map(gp => gp.init()).getOrElse(Future.successful())
          } else {
            Future.successful()
          }
        })
      } else {
        Future.successful()
      }).flatMap(_ =>
        new SessionId(gameClient).process()
      )
    }
  }

    /*if (charName != "noname") {
      character.getCharacter(gameClient.loginName, charName).map(result => {
        if (result.nonEmpty && gameClient.player == null) {
          println("INIT GAME PLAYER")
          gameClient.player = new GamePlayer(result.head)
          gameClient.player.init()
        }
      })
    }
    new SessionId(gameClient).process()
  }*/
}