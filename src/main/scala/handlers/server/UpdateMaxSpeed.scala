package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class UpdateMaxSpeed(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player
    if (player == null) {
      return Future { Array.emptyByteArray }
    }

    val writer = new PacketWriter(0xB6)
    // pak.WriteShort((ushort) (m_gameClient.Player.MaxSpeed*100/GamePlayer.PLAYER_BASE_SPEED));
    // ins = write_short(0x007D)
    writer.writeShort(0x007D)
    // pak.WriteByte((byte) (m_gameClient.Player.IsTurningDisabled ? 0x01 : 0x00));
    // ins += write_byte(0x00)
    writer.writeByte(0x00)
    // // water speed in % of land speed if its over 0 i think
    // pak.WriteByte((byte)Math.Min(byte.MaxValue,
    // 	((m_gameClient.Player.MaxSpeed*100/GamePlayer.PLAYER_BASE_SPEED)*(m_gameClient.Player.GetModified(eProperty.WaterSpeed)*.01))));
    // ins += write_byte(0x00)
    writer.writeByte(0x00)
    Future {
      writer.getFinalPacket()
    }
  }
}
