package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class UpdateMoney(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player
    if (player == null) {
      return Future { Array.emptyByteArray }
    }

    val money = player.money

    val writer = new PacketWriter(0xFA)
    writer.writeByte(money.getInteger("copper").toByte)
    writer.writeByte(money.getInteger("silver").toByte)
    writer.writeShort(money.getInteger("gold").toShort)
    writer.writeShort(money.getInteger("mithril").toShort)
    writer.writeShort(money.getInteger("platinium").toShort)
    Future {
      writer.getFinalPacket()
    }
  }
}
