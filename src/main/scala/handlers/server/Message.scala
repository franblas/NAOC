package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class Message(msg: String, chatType: Int, chatLoc: Int, gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player

    player match {
      case null => Future { Array.emptyByteArray }
      case _ => compute()
    }
  }

  private def compute(): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.message)
    //// pak.WriteShort(0xFFFF);
    //ins = write_short(0xFFFF)
    writer.writeShort(0xFFFF.toShort)
    //// pak.WriteShort((ushort)m_gameClient.SessionID);
    //ins += write_short(gameclient.session_id)
    writer.writeShort(gameClient.sessionId.toShort)
    //// pak.WriteByte((byte)type);
    //ins += write_byte(msg_type)
    writer.writeByte(chatType.toByte)
    //// pak.Fill(0x0, 3);
    //ins += fill_pak(0x00, 3)
    writer.fill(0x00, 3)
    //// string str;
    //// if (loc == eChatLoc.CL_ChatWindow)
    //// 	str = "@@";
    //// else if (loc == eChatLoc.CL_PopupWindow)
    //// 	str = "////";
    //// else
    //// 	str = "";
    //st = ""
    //ins += write_string(st + msg)
    writer.writeString(msg)
    writer.toFinalFuture()
  }
}
