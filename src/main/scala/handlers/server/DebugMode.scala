package handlers.server

import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class DebugMode {
  def process(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.debugMode)
    /*
    // if (m_gameClient.Account.PrivLevel == 1)
    // {
      //     pak.WriteByte((0x00));
      // }
    // else
    // {
      //     pak.WriteByte((byte) (on ? 0x01 : 0x00));
      // }
    */
    writer.writeByte(0x00)
    writer.writeByte(0x00)
    writer.toFinalFuture()
  }
}
