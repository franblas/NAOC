package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class StatusUpdate(sittingFlag: Int, gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player
    if (player == null) {
      return Future { Array.emptyByteArray }
    }

    val health = 0x01 // TODO
    val healthMax = 0x1E // TODO (30)
    val healthPercent = percentage(health, healthMax)

    val mana = 0x00 // TODO
    val manaMax = 0x19 // TODO (25)
    val manaPercent = percentage(mana, manaMax)

    val endurance = 0x64 // TODO (100)
    val enduranceMax = 0x64  // TODO (100)
    val endurancePercent = percentage(endurance, enduranceMax)

    val concentration = 0x04 // TODO
    val concentrationMax = 0x04 // TODO
    val concentrationPercent = percentage(concentration, concentrationMax)

    val writer = new PacketWriter(0xAD)
    writer.writeByte(healthPercent.toByte)
    writer.writeByte(manaPercent.toByte)
    writer.writeByte(sittingFlag.toByte)
    writer.writeByte(endurancePercent.toByte)
    writer.writeByte(concentrationPercent.toByte)
    writer.writeByte(0x00) // unk
    writer.writeShort(manaMax.toShort)
    writer.writeShort(enduranceMax.toShort)
    writer.writeShort(concentrationMax.toShort)
    writer.writeShort(healthMax.toShort)
    writer.writeShort(health.toShort)
    writer.writeShort(endurance.toShort)
    writer.writeShort(mana.toShort)
    writer.writeShort(concentration.toShort)
    Future {
      writer.getFinalPacket()
    }
  }

  private def percentage(v: Int, maxV: Int): Int = {
    (v / maxV) * 100
  }

}
