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
    gameClient.player.map(player => compute(player)).getOrElse(Future { Array.emptyByteArray })
  }

  private def compute(player: GamePlayer): Future[Array[Byte]] = {
    val money = player.money

    val writer = new PacketWriter(ServerCodes.updateMoney)
    writer.writeByte(money.copper.toByte)
    writer.writeByte(money.silver.toByte)
    writer.writeShort(money.gold.toShort)
    writer.writeShort(money.mithril.toShort)
    writer.writeShort(money.platinium.toShort)
    writer.toFinalFuture()
  }
}
