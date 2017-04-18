package handlers.client

import java.sql.Timestamp
import java.util.Date

import handlers.GameClient
import handlers.packets.PacketReader
import handlers.server.PingReply

import scala.concurrent.Future

/**
  * Created by franblas on 26/03/17.
  */
class PingRequest(gameClient: GameClient) extends HandlerProcessor {
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val reader = new PacketReader(data)
    reader.skip(4)
    val timestamp = reader.readInt()
    new PingReply(new Timestamp(new Date().getTime).getTime.toInt, gameClient.requestCounter).process()
  }
}
