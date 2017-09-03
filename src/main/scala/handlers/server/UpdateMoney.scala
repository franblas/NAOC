package handlers.server

import gameobjects.GamePlayer
import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class UpdateMoney(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player

    player match {
      case null => Future { Array.emptyByteArray }
      case _ => compute(player)
    }
  }

  private def compute(player: GamePlayer): Future[Array[Byte]] = {
    val money = player.money

    val writer = new PacketWriter(ServerCodes.updateMoney)
    writer.writeByte(money.getInteger("copper").toByte)
    writer.writeByte(money.getInteger("silver").toByte)
    writer.writeShort(money.getInteger("gold").toShort)
    writer.writeShort(money.getInteger("mithril").toShort)
    writer.writeShort(money.getInteger("platinium").toShort)
    writer.toFinalFuture()
  }
}
