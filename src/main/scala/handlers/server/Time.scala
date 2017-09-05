package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class Time(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    gameClient.player.map(_ => compute()).getOrElse(Future { Array.emptyByteArray })
  }

  private def compute(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.time)
    //pak.WriteInt(WorldMgr.GetCurrentGameTime(m_gameClient.Player));
    writer.writeInt(0x02dc9708) // TODO: time should be dynamic (day/night cycle)
    //pak.WriteInt(WorldMgr.GetDayIncrement(m_gameClient.Player));
    writer.writeInt(24)
    writer.toFinalFuture()
  }
}
