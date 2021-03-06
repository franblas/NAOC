package world

import database.{Mobs, WorldObjects}
import handlers.GameClient
import handlers.server.{ObjectCreate, ObjectUpdate}

import scala.concurrent.ExecutionContext.Implicits.global

/**
  * Created by franblas on 17/04/17.
  */
class WorldUpdate {

  private val mobs = new Mobs()
  private val worldObjects = new WorldObjects()

  val NPC_UPDATE_INTERVAL: Int = 10 // in secs
  val NPC_UPDATE_KEYWORD: String = "updateNPCs"

  val OBJ_UPDATE_INTERVAL: Int = 30 // in secs
  val OBJ_UPDATE_KEYWORD: String = "updateWorldObjects"

  val VISIBILITY_DISTANCE = 3600
  val OBJ_UPDATE_DISTANCE = 4096

  def updateNPCs(gameClient: GameClient): Unit = {
    gameClient.player.map(player => {
      if (player.enteredGame) {
        val regionId = player.currentRegion.regionId
        val t1 = System.nanoTime()
        mobs.getMobsFromRegion(regionId).map(results => {
          println("update LENGTH MOBS = ", results.length)
          var plop = 0
          results.foreach(mob => {
            //val mobX = mob.getInteger("x")
            //val mobY = mob.getInteger("y")
            if (player.inZone(mob.x, mob.y, player.currentZone)) {
              val mobPosition = new Point(mob.x, mob.y)
              if (mobPosition.inRadius(player.currentPosition.x, player.currentPosition.y, VISIBILITY_DISTANCE)) {
                gameClient.sendPacket(new ObjectUpdate(mob, gameClient).process())
                plop += 1
              }
            }
          })
          println("update LENGTH MOBS IN RADIUS = ", plop)
          println("update END OF LOOP")
          val t2 = System.nanoTime()
          println("Elapsed time MOBS: " + (t2 - t1) + "ns")
        })
      }
    })
  }

  def updateWorldObjects(gameClient: GameClient): Unit = {
    gameClient.player.map(player => {
      if (player.enteredGame) {
        val regionId = player.currentRegion.regionId

        val t1 = System.nanoTime()
        worldObjects.getWorldObjectsFromRegion(regionId).map(results => {
          println("update LENGTH WO = ", results.length)
          var plop = 0
          results.foreach(obj => {
            if (player.inZone(obj.x, obj.y, player.currentZone)) {
              val objPosition = new Point(obj.x, obj.y)
              if (objPosition.inRadius(player.currentPosition.x, player.currentPosition.y, OBJ_UPDATE_DISTANCE)) {
                gameClient.sendPacket(new ObjectCreate(obj).process())
                plop += 1
              }
            }
          })
          println("update LENGTH WO IN RADIUS = ", plop)
          println("update END OF LOOP")
          val t2 = System.nanoTime()
          println("Elapsed time WO: " + (t2 - t1) + "ns")
        })
      }
    })
  }
}
