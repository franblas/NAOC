package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class Encumberance(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player

    player match {
      case null => Future { Array.emptyByteArray }
      case _ => compute()
    }
  }

  private def compute(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.encumberance)
    // pak.WriteShort((ushort) m_gameClient.Player.MaxEncumberance); // encumb total
    // ins = write_short(0x0028) //TODO
    writer.writeShort(0x0028)
    //  pak.WriteShort((ushort) m_gameClient.Player.Encumberance); // encumb used
    // ins += write_short(0x0000) //TODO
    writer.writeShort(0x0000)
    writer.toFinalFuture()
  }
}
