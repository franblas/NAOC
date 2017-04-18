package handlers.client

import database.Mobs
import handlers.GameClient
import handlers.server._

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 15/04/17.
  */
class PlayerInitRequest(gameClient: GameClient) extends HandlerProcessor {

  val mobs = new Mobs()

  override def process(data: Array[Byte]): Future[Array[Byte]] = {

    //gameclient.send_pak(update_points_pak(gameclient))
    gameClient.sendPacket(new UpdatePoints().process())
    //gameclient.send_pak(region_color_scheme_pak(0x00))
    gameClient.sendPacket(new RegionColorScheme(0x00).process())
    //gameclient.send_pak(weather_pak())
    gameClient.sendPacket(new Weather().process())
    //gameclient.send_pak(time_pak(gameclient))
    gameClient.sendPacket(new Time(gameClient).process())
    //gameclient.send_pak(xfire_info_pak(0x00, gameclient))
    gameClient.sendPacket(new XFireInfo(0x00, gameClient).process())
    //gameclient.send_pak(message_pak("Welcome to the NAOC test server!", 0x1C, None, gameclient))
    gameClient.sendPacket(new Message("Welcome to the NAOC test server!", 0x1C, -1, gameClient).process())
    //gameclient.send_pak(dialog_pak(6, 1, 1, 0, 0, 1, True, "Do you want to be teleported to NAOCplayground?", gameclient))
    gameClient.sendPacket(new Dialog(6, 1, 1, 0, 0, 1, true, "Do you want to be teleported to NAOC playground?", gameClient).process())
    //gameclient.send_pak(message_pak("If you need in-game assistance from server staff (such as stuck character) please use /appeal.", 0x00, None, gameclient))
    gameClient.sendPacket(new Message("If you need in-game assistance from server staff (such as stuck character) please use /appeal.", 0x00, -1, gameClient).process())


    //send_mobs_and_mob_equipment_to_player(gameclient)
    sendMobsAndEquipmentToPlayer().map(_ => {
      println("INIT PLAYER FINISH")
      //gameclient.send_pak(player_init_finished_pak(0))
      gameClient.sendPacket(new PlayerInitFinished().process())
      //gameclient.send_pak(started_help_pak())
      gameClient.sendPacket(new StartedHelp().process())
      //gameclient.send_pak(player_free_level_update_pak())
      gameClient.sendPacket(new PlayerFreeLevelUpdate().process())
      Array.emptyByteArray
    })
  }

  def sendMobsAndEquipmentToPlayer(): Future[Unit] = {
    val player = gameClient.player
    val regionId = player.currentRegion.getInteger("region_id").toInt

    mobs.getMobsFromRegion(regionId).map(results => {
      println("LENGTH MOBS = ", results.length)
      results.foreach(mob => {
        if (player.inZone(mob.getInteger("x").toInt, mob.getInteger("y").toInt, player.currentZone)) {
          gameClient.sendPacket(new NPCCreate(mob, gameClient).process())
          //gameClient.sendPacket(new LivingEquipmentUpdate(mob, gameClient).process())
          //if npc.inventory:
          //  gameclient.send_pak(living_equipment_update_pak(npc, mobs, gameclient))
        }
      })
      println("END OF LOOP")
    })
  }
}