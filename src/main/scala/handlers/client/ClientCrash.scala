package handlers.client

import handlers.packets.PacketReader

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 08/04/17.
  */
class ClientCrash extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    val dllName = reader.readString(16)
    reader.cursor = 0x50
    val upTime = reader.readInt()
    println("Client crash! :(", dllName, upTime)
    Future {
      Array.emptyByteArray
    }
  }
}
