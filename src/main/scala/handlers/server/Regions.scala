package handlers.server

import handlers.GameClient
import handlers.packets.{PacketWriter, ServerCodes}

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 09/04/17.
  */
class Regions(gameClient: GameClient) {
  def process(): Future[Array[Byte]] = {
    val player = gameClient.player

    player match {
      case null => Future { Array.emptyByteArray }
      case _ if player.currentRegion == null => Future { Array.emptyByteArray }
      case _ if player.currentRegion.getInteger("region_id", -100) == -100 => Future { Array.emptyByteArray }
      case _ => compute(player.currentRegion.getInteger("region_id", -100))
    }
  }

  private def compute(regionId: Int): Future[Array[Byte]] = {
    val writer = new PacketWriter(ServerCodes.regions)
    writer.writeByte(0x0)
    //writer.writeByte(0x1B.toByte) // region_id = 27 (tutorial)
    writer.writeByte(regionId.toByte)
    writer.fill(0x0, 20)
    writer.fillString("10300", 5)
    writer.fillString("10300", 5)
    writer.fillString("127.0.0.1", 20)
    writer.toFinalFuture()
  }
}
