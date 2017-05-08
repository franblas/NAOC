package handlers.client

import handlers.packets.PacketReader

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 28/04/17.
  */
class PlayerCommandHandler extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    reader.skip(8)
    val cmdLine = reader.readString(255)
    println(cmdLine)
    Future {
      Array.emptyByteArray
    }
  }
}
