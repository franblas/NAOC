package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class CharResistsUpdate(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    gameClient.player.map(_ => compute()).getOrElse(Future { Array.emptyByteArray })
  }

  private def compute(): Future[Array[Byte]] = {
    val updateResists: Seq[Int] = Seq(
      0, //eResist.Crush,
      0, //eResist.Slash,
      0, //eResist.Thrust,
      0, //eResist.Heat,
      0, //eResist.Cold,
      0, //eResist.Matter,
      0, //eResist.Body,
      0, //eResist.Spirit,
      0 //eResist.Energy,
    )

    val writer = new PacketWriter(ServerCodes.charResistsUpdate)
    updateResists.foreach(_ => {
      writer.writeShort(0x00)
    })
    updateResists.foreach(_ => {
      writer.writeShort(0x00)
    })
    updateResists.foreach(_ => {
      writer.writeShort(0x00)
    })
    updateResists.foreach(_ => {
      writer.writeByte(0x01)
    })
    updateResists.foreach(_ => {
      writer.writeByte(0x00)
    })
    writer.writeByte(0xFF.toByte)
    writer.writeByte(0x00)
    writer.writeShort(0x00)
    writer.writeShort(0x00)
    writer.toFinalFuture()
  }
}
