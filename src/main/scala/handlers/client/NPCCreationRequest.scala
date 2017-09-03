package handlers.client

import database.Mobs
import handlers.GameClient
import handlers.packets.PacketReader
import handlers.server.NPCCreate

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 22/04/17.
  */
class NPCCreationRequest(gameClient: GameClient) extends HandlerProcessor {

  val mobs = new Mobs()

  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    val player = gameClient.player
    if (player == null || player.currentRegion == null) {
      Future { Array.emptyByteArray }
    } else {
      val reader = new PacketReader(data)
      val objectId = reader.readShort()
      val regionId = player.currentRegion.getInteger("region_id").toInt
      mobs.getSingleMobFromRegion(objectId.toInt, regionId).map(results => {
        val mob = results.head
        if (mob.nonEmpty) gameClient.sendPacket(new NPCCreate(mob, gameClient).process())
        Array.emptyByteArray
      })
    }
  }
}
