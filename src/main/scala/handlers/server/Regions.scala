package handlers.server

import handlers.GameClient
import handlers.packets.PacketWriter

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 09/04/17.
  */
class Regions(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player
    if (player == null) {
      return Future { Array.emptyByteArray }
    }

    if (player.currentRegion == null) return Future { Array.emptyByteArray }

    val regionId: Int = player.currentRegion.getInteger("region_id", -100)
    if (regionId == -100) return Future { Array.emptyByteArray }

    val writer = new PacketWriter(0xB1)
    writer.writeByte(0x0)
    //writer.writeByte(0x1B.toByte) // region_id = 27 (tutorial)
    writer.writeByte(regionId.toByte)
    writer.fill(0x0, 20)
    writer.fillString("10300", 5)
    writer.fillString("10300", 5)
    writer.fillString("127.0.0.1", 20)
    Future {
      writer.getFinalPacket()
    }
  }
}
