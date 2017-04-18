from ..packets.packet_in import read_byte
from ..server.player_position_and_objectid_pak import player_position_and_objectid_pak
from ..server.encumberance_pak import encumberance_pak
from ..server.update_max_speed_pak import update_max_speed_pak
from ..server.status_update_pak import status_update_pak
from ..server.inventory_items_update_pak import inventory_items_update_pak
from ..server.add_friend_pak import add_friend_pak
from ..server.update_player_skills_pak import update_player_skills_pak
from ..server.update_crafting_skills_pak import update_crafting_skills_pak
from ..server.non_hybrid_spell_lines_pak import non_hybrid_spell_lines_pak
from ..server.update_player_pak import update_player_pak
from ..server.update_money_pak import update_money_pak
from ..server.char_stats_update_pak import char_stats_update_pak
from ..server.char_resists_update_pak import char_resists_update_pak
from ..server.update_weapon_and_armor_stats_pak import update_weapon_and_armor_stats_pak
from ..server.quest_list_update_pak import quest_list_update_pak
from ..server.update_points_pak import update_points_pak
from ..server.concentration_list_pak import concentration_list_pak
from ..server.object_guild_id_pak import object_guild_id_pak
from ..server.debug_mode_pak import debug_mode_pak
from ..server.set_controlled_horse_pak import set_controlled_horse_pak

def world_init_request_handler(packet,gameclient):
    cursor = 0
    # addfriend
    gameclient.send_pak(add_friend_pak())
    # player.Out.SendPlayerPositionAndObjectID();
    gameclient.send_pak(player_position_and_objectid_pak(gameclient))
    # player.Out.SendEncumberance(); # Send only max encumberance without used
    gameclient.send_pak(encumberance_pak(gameclient))
    # player.Out.SendUpdateMaxSpeed();
    gameclient.send_pak(update_max_speed_pak(gameclient))
    # #TODO 0xDD - Conc Buffs # 0 0 0 0
    # #Now find the friends that are online
    # player.Out.SendUpdateMaxSpeed(); # Speed after conc buffs
    gameclient.send_pak(update_max_speed_pak(gameclient))
    # player.Out.SendStatusUpdate();
    gameclient.send_pak(status_update_pak(0x00, gameclient))
    # player.Out.SendInventoryItemsUpdate(eInventoryWindowType.Equipment, player.Inventory.EquippedItems);
    # gameclient.send_pak(inventory_items_update_pak(0x01, gameclient))
    # player.Out.SendInventoryItemsUpdate(eInventoryWindowType.Inventory, player.Inventory.GetItemRange(eInventorySlot.FirstBackpack, eInventorySlot.LastBagHorse));
    # gameclient.send_pak(inventory_items_update_pak(0x02, gameclient))
    # player.Out.SendUpdatePlayerSkills();   #TODO Insert 0xBE - 08 Various in SendUpdatePlayerSkills() before send spells
    gameclient.send_pak(update_player_skills_pak(gameclient))
    gameclient.send_pak(non_hybrid_spell_lines_pak(gameclient))
    # player.Out.SendUpdateCraftingSkills(); # ^
    gameclient.send_pak(update_crafting_skills_pak(gameclient))
    # player.Out.SendUpdatePlayer();
    gameclient.send_pak(update_player_pak(gameclient))
    # player.Out.SendUpdateMoney();
    gameclient.send_pak(update_money_pak(gameclient))
    # player.Out.SendCharStatsUpdate();
    gameclient.send_pak(char_stats_update_pak(gameclient))
    # player.Out.SendCharResistsUpdate();
    gameclient.send_pak(char_resists_update_pak(gameclient))
    # player.Out.SendUpdateWeaponAndArmorStats();
    gameclient.send_pak(update_weapon_and_armor_stats_pak(gameclient))
    # player.Out.SendQuestListUpdate();
    quest_list_update_pak(gameclient)
    # player.Out.SendStatusUpdate();
    gameclient.send_pak(status_update_pak(0x00, gameclient))
    # player.Out.SendUpdatePoints();
    gameclient.send_pak(update_points_pak(gameclient))
    # player.Out.SendEncumberance();
    gameclient.send_pak(encumberance_pak(gameclient))
    # player.Out.SendConcentrationList();
    gameclient.send_pak(concentration_list_pak(gameclient))
    gameclient.send_pak(status_update_pak(0x00, gameclient))
    # player.Out.SendObjectGuildID(player, player.Guild);
    gameclient.send_pak(object_guild_id_pak())
    # player.Out.SendDebugMode(player.TempProperties.getProperty<object>(GamePlayer.DEBUG_MODE_PROPERTY, null) != null);
    gameclient.send_pak(debug_mode_pak())
    # player.Out.SendUpdateMaxSpeed(); # Speed in debug mode ?
    gameclient.send_pak(update_max_speed_pak(gameclient))
    # player.Out.SendSetControlledHorse(player);
    gameclient.send_pak(set_controlled_horse_pak())

# int effectsCount = 0;
# player.Out.SendUpdateIcons(null, ref effectsCount);
# # Visual 0x4C - Color Name style (0 0 5 0 0 0 0 0) for RvR or (0 0 5 1 0 0 0 0) for PvP
# # 0xBE - 0 1 0 0
# #used only on PvP, sets THIS players ID for nearest friend/enemy buttons and "friendly" name colors
# #if (GameServer.ServerRules.GetColorHandling(player.Client) == 1) # PvP
# #WARNING: This would change problems if a scripter changed the values for plvl
# #GSMessages.SendDebugMode(client,client.Account.PrivLevel>1);
# player.Stealth(false);


#############################################################################
#############################################################################
#############################################################################

# player.Client.ClientState = GameClient.eClientState.WorldEnter;
# 				# 0x88 - Position
# 				# 0x6D - FriendList
# 				# 0x15 - Encumberance update
# 				# 0x1E - Speed update
# 				# 0xDD - Shared Buffs update
# 				# 0x1E - Speed update
# 				# 0x05 - Health, Sit update
# 				# 0xAA - Inventory Update
# 				# 0xAA - Inventory Update /Vault ?
# 				# 0xBE - 01 various tabs update (skills/spells...)
# 				# 0xBE - 08 various tabs update (skills/spells...)
# 				# 0xBE - 02 spells
# 				# 0xBE - 03 various tabs update (skills/spells...)
# 				# 0x52 - Money update
# 				# 0x53 - stats update
# 				# 0xD7 - Self Buffs update
# 				# 0xBE - 05, various tabs ...
# 				# 0x2B - Quest list
# 				# 0x05 - health again...?
# 				# 0x39 - XP update?
# 				# 0x15 - Encumberance update
# 				# 0xBE - 06, group
# 				# 0xE4 - ??  (0 0 5 0 0 0 0 0)
# 				# 0xBE - 0 1 0 0
# 				# 0x89 - Debug mode
# 				# 0x1E - Speed again!?
# 				# 0x25 - model change
#
# 				#Get the objectID for this player
# 				#IMPORTANT ... this is needed BEFORE
# 				#sending Packet 0x88!!!
#
# 				if (!player.AddToWorld())
# 				{
# 					log.ErrorFormat("Failed to add player to the region! {0}", player.ToString());
# 					player.Client.Out.SendPlayerQuit(true);
# 					player.Client.Player.SaveIntoDatabase();
# 					player.Client.Player.Quit(true);
# 					player.Client.Disconnect();
#
# 					return;
# 				}
#
# 				# this is bind stuff
# 				# make sure that players doesnt start dead when coming in
# 				# thats important since if client moves the player it requests player creation
# 				if (player.Health <= 0)
# 				{
# 					player.Health = player.MaxHealth;
# 				}
#
# 				player.Out.SendPlayerPositionAndObjectID();
# 				player.Out.SendEncumberance(); # Send only max encumberance without used
# 				player.Out.SendUpdateMaxSpeed();
# 				#TODO 0xDD - Conc Buffs # 0 0 0 0
# 				#Now find the friends that are online
# 				player.Out.SendUpdateMaxSpeed(); # Speed after conc buffs
# 				player.Out.SendStatusUpdate();
# 				player.Out.SendInventoryItemsUpdate(eInventoryWindowType.Equipment, player.Inventory.EquippedItems);
#                 player.Out.SendInventoryItemsUpdate(eInventoryWindowType.Inventory, player.Inventory.GetItemRange(eInventorySlot.FirstBackpack, eInventorySlot.LastBagHorse));
# 				player.Out.SendUpdatePlayerSkills();   #TODO Insert 0xBE - 08 Various in SendUpdatePlayerSkills() before send spells
# 				player.Out.SendUpdateCraftingSkills(); # ^
# 				player.Out.SendUpdatePlayer();
# 				player.Out.SendUpdateMoney();
# 				player.Out.SendCharStatsUpdate();
#
# 				player.Out.SendCharResistsUpdate();
# 				int effectsCount = 0;
# 				player.Out.SendUpdateIcons(null, ref effectsCount);
# 				player.Out.SendUpdateWeaponAndArmorStats();
# 				player.Out.SendQuestListUpdate();
# 				player.Out.SendStatusUpdate();
# 				player.Out.SendUpdatePoints();
# 				player.Out.SendEncumberance();
#                 player.Out.SendConcentrationList();
# 				# Visual 0x4C - Color Name style (0 0 5 0 0 0 0 0) for RvR or (0 0 5 1 0 0 0 0) for PvP
# 				# 0xBE - 0 1 0 0
# 				#used only on PvP, sets THIS players ID for nearest friend/enemy buttons and "friendly" name colors
# 				#if (GameServer.ServerRules.GetColorHandling(player.Client) == 1) # PvP
# 				player.Out.SendObjectGuildID(player, player.Guild);
# 				player.Out.SendDebugMode(player.TempProperties.getProperty<object>(GamePlayer.DEBUG_MODE_PROPERTY, null) != null);
# 				player.Out.SendUpdateMaxSpeed(); # Speed in debug mode ?
# 				#WARNING: This would change problems if a scripter changed the values for plvl
# 				#GSMessages.SendDebugMode(client,client.Account.PrivLevel>1);
# 				player.Stealth(false);
# 				player.Out.SendSetControlledHorse(player);
