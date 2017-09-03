package handlers.server

import gameobjects.GamePlayer
import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class CharStatsUpdate(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player

    player match {
      case null => Future { Array.emptyByteArray }
      case _ => compute(player)
    }
  }

  private def compute(player: GamePlayer): Future[Array[Byte]] = {
    val character = player.dbCharacter
    val updateStats: Seq[Int] = Seq(
      character.getInteger("strength"),
      character.getInteger("dexterity"),
      character.getInteger("constitution"),
      character.getInteger("quickness"),
      character.getInteger("intelligence"),
      character.getInteger("piety"),
      character.getInteger("empathy"),
      character.getInteger("charisma")
    )

    val writer = new PacketWriter(ServerCodes.charStatsUpdate)
    updateStats.foreach(stat => {
      writer.writeShort(stat.toShort)
    })
    writer.writeShort(0x00)
    updateStats.foreach(_ => {
      writer.writeShort(0x00)
    })
    writer.writeShort(0x00)
    updateStats.foreach(_ => {
      writer.writeShort(0x00)
    })
    writer.writeShort(0x00)
    updateStats.foreach(_ => {
      writer.writeByte(0x01)
    })
    writer.writeByte(0x00)
    updateStats.foreach(_ => {
      writer.writeByte(0x00)
    })
    writer.writeByte(0x00)
    writer.writeByte(0x00)
    writer.writeByte(0x00)
    writer.writeShort(0x1E)
    writer.writeShort(0x00)
    writer.toFinalFuture()
  }
}
