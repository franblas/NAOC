package handlers.client

import handlers.GameClient
import handlers.server.{GameOpen, StatusUpdate, UpdatePoints}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class GameOpenRequest(gameClient: GameClient) extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    gameClient.sendPacket(new GameOpen().process())
    gameClient.sendPacket(new StatusUpdate(0, gameClient).process())
    gameClient.sendPacket(new UpdatePoints().process())
    Future { Array.emptyByteArray }
  }
}
