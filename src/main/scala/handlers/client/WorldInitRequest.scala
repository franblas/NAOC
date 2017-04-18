package handlers.client


import handlers.GameClient
import handlers.server._

import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Future

/**
  * Created by franblas on 14/04/17.
  */
class WorldInitRequest(gameClient: GameClient) extends HandlerProcessor{
  override def process(data: Array[Byte]): Future[Array[Byte]] = {
    //gameclient.send_pak(add_friend_pak())
    gameClient.sendPacket(new AddFriend().process())

    //gameclient.send_pak(player_position_and_objectid_pak(gameclient))
    gameClient.sendPacket(new PlayerPositionAndObjectId(gameClient).process())

    // gameclient.send_pak(encumberance_pak(gameclient))
    gameClient.sendPacket(new Encumberance(gameClient).process())

    // gameclient.send_pak(update_max_speed_pak(gameclient))
    gameClient.sendPacket(new UpdateMaxSpeed(gameClient).process())

    // gameclient.send_pak(update_max_speed_pak(gameclient))
    gameClient.sendPacket(new UpdateMaxSpeed(gameClient).process())

    // gameclient.send_pak(status_update_pak(0x00, gameclient))
    gameClient.sendPacket(new StatusUpdate(0, gameClient).process())

    // // player.Out.SendInventoryItemsUpdate(eInventoryWindowType.Equipment, player.Inventory.EquippedItems);
    // // gameclient.send_pak(inventory_items_update_pak(0x01, gameclient))
    // // player.Out.SendInventoryItemsUpdate(eInventoryWindowType.Inventory, player.Inventory.GetItemRange(eInventorySlot.FirstBackpack, eInventorySlot.LastBagHorse));
    // // gameclient.send_pak(inventory_items_update_pak(0x02, gameclient))
    // // player.Out.SendUpdatePlayerSkills();   //TODO Insert 0xBE - 08 Various in SendUpdatePlayerSkills() before send spells
    // gameclient.send_pak(update_player_skills_pak(gameclient))
    gameClient.sendPacket(new UpdatePlayerSkills(gameClient).process())
    // gameclient.send_pak(non_hybrid_spell_lines_pak(gameclient))
    gameClient.sendPacket(new NonHybridSpellLines(gameClient).process())
    // gameclient.send_pak(update_crafting_skills_pak(gameclient))
    gameClient.sendPacket(new UpdateCraftingSkills(gameClient).process())
    // gameclient.send_pak(update_player_pak(gameclient))
    gameClient.sendPacket(new UpdatePlayer(gameClient).process())
    // gameclient.send_pak(update_money_pak(gameclient))
    gameClient.sendPacket(new UpdateMoney(gameClient).process())
    // gameclient.send_pak(char_stats_update_pak(gameclient))
    gameClient.sendPacket(new CharStatsUpdate(gameClient).process())
    // gameclient.send_pak(char_resists_update_pak(gameclient))
    gameClient.sendPacket(new CharResistsUpdate(gameClient).process())
    // gameclient.send_pak(update_weapon_and_armor_stats_pak(gameclient))
    gameClient.sendPacket(new UpdateWeaponAndArmorStats(gameClient).process())

    //TODO
    // quest_list_update_pak(gameclient)

    // gameclient.send_pak(status_update_pak(0x00, gameclient))
    gameClient.sendPacket(new StatusUpdate(0, gameClient).process())
    // gameclient.send_pak(update_points_pak(gameclient))
    gameClient.sendPacket(new UpdatePoints().process())
    // gameclient.send_pak(encumberance_pak(gameclient))
    gameClient.sendPacket(new Encumberance(gameClient).process())
    //gameclient.send_pak(concentration_list_pak(gameclient))
    gameClient.sendPacket(new ConcentrationList(gameClient).process())
    // gameclient.send_pak(status_update_pak(0x00, gameclient))
    gameClient.sendPacket(new StatusUpdate(0, gameClient).process())
    // gameclient.send_pak(object_guild_id_pak())
    gameClient.sendPacket(new ObjectGuildId().process())
    // gameclient.send_pak(debug_mode_pak())
    gameClient.sendPacket(new DebugMode().process())
    // gameclient.send_pak(update_max_speed_pak(gameclient))
    gameClient.sendPacket(new UpdateMaxSpeed(gameClient).process())
    // gameclient.send_pak(set_controlled_horse_pak())
    gameClient.sendPacket(new SetControlledHorse().process())

    Future { Array.emptyByteArray }
  }
}
