package handlers.client


import handlers.GameClient
import world.WorldUpdate

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 28/04/17.
  */
class ObjectUpdateRequest(gameClient: GameClient) extends HandlerProcessor {

  val worldUpdate = new WorldUpdate()

  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    // TODO
    println("---> ObjectUpdateRequest")
    Future {
      worldUpdate.updateWorldObjects(gameClient)
      Array.emptyByteArray
    }
  }

}
