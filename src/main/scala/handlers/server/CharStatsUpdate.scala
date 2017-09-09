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
    gameClient.player.map(player => compute(player)).getOrElse(Future { Array.emptyByteArray })
  }

  private def compute(player: GamePlayer): Future[Array[Byte]] = {
    val character = player.dbCharacter
    val updateStats: Seq[Int] = Seq(
      character.strength,
      character.dexterity,
      character.constitution,
      character.quickness,
      character.intelligence,
      character.piety,
      character.empathy,
      character.charisma
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
