package handlers.server

import handlers.client.HandlerProcessor
import handlers.packets.PacketReader

import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class DoorRequest extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    val doorId = reader.readInt()
    val doorState = reader.readByte()
    new DoorState(doorId, doorState).process()
  }
}
