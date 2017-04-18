package world

import database.Mobs
import handlers.GameClient
import handlers.server.ObjectUpdate

import scala.concurrent.ExecutionContext.Implicits.global

/**
  * Created by franblas on 17/04/17.
  */
class WorldUpdate {

  private val mobs = new Mobs()
  val NPC_UPDATE_INTERVAL: Int = 10 // in secs
  val NPC_UPDATE_KEYWORD: String = "updateNPCs"

  def updateNPCs(gameClient: GameClient): Unit = {
    val player = gameClient.player
    if (player == null) return

    val regionId = player.currentRegion.getInteger("region_id").toInt

    mobs.getMobsFromRegion(regionId).map(results => {
      println("LENGTH MOBS = ", results.length)
      results.foreach(mob => {
        if (player.inZone(mob.getInteger("x").toInt, mob.getInteger("y").toInt, player.currentZone)) {
          gameClient.sendPacket(new ObjectUpdate(mob, gameClient).process())
        }
      })
      println("END OF LOOP")
    })
  }
}
