package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class Time(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player
    if (player == null) {
      return Future { Array.emptyByteArray }
    }

    val writer = new PacketWriter(0x7E)
    //pak.WriteInt(WorldMgr.GetCurrentGameTime(m_gameClient.Player));
    writer.writeInt(0x02dc9708)
    //pak.WriteInt(WorldMgr.GetDayIncrement(m_gameClient.Player));
    writer.writeInt(24)
    Future {
      writer.getFinalPacket()
    }
  }
}
