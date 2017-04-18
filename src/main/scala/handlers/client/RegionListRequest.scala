package handlers.client

import handlers.GameClient
import handlers.server.Regions

import scala.concurrent.Future

/**
  * Created by franblas on 09/04/17.
  */
class RegionListRequest(gameClient: GameClient) extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    new Regions(gameClient).process()
  }
}
