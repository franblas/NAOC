import threading

from ..server.update_points_pak import update_points_pak
from ..server.region_color_scheme_pak import region_color_scheme_pak
from ..server.weather_pak import weather_pak
from ..server.time_pak import time_pak
from ..server.xfire_info_pak import xfire_info_pak
from ..server.message_pak import message_pak
from ..server.dialog_pak import dialog_pak
from ..server.npc_create_pak import npc_create_pak
from ..server.living_equipment_update_pak import living_equipment_update_pak
from ..server.player_init_finished_pak import player_init_finished_pak
from ..server.started_help_pak import started_help_pak
from ..server.player_free_level_update_pak import player_free_level_update_pak

from ...database.db_mobs import get_mobs_from_region

def player_init_request_handler(packet,gameclient):
    t = threading.Thread(name='player_init_' + str(gameclient.session_id), target=player_init, kwargs={'packet': packet, 'gameclient': gameclient})
    t.start()

def player_init(packet,gameclient):
    gameclient.send_pak(update_points_pak(gameclient))
    gameclient.send_pak(region_color_scheme_pak(0x00))

    gameclient.send_pak(weather_pak())
    gameclient.send_pak(time_pak(gameclient))
    gameclient.send_pak(xfire_info_pak(0x00, gameclient))
    gameclient.send_pak(message_pak("Welcome to the NAOC test server!", 0x1C, None, gameclient))
    gameclient.send_pak(dialog_pak(6, 1, 1, 0, 0, 1, True, "Do you want to be teleported to NAOCplayground?", gameclient))
    gameclient.send_pak(message_pak("If you need in-game assistance from server staff (such as stuck character) please use /appeal.", 0x00, None, gameclient))

    t = threading.Thread(name='send_mobs_and_mob_equipment_to_player_' + str(gameclient.session_id), target=send_mobs_and_mob_equipment_to_player, kwargs={'gameclient': gameclient})
    t.start()
    # mobs = send_mobs_and_mob_equipment_to_player(gameclient)
    gameclient.send_pak(player_init_finished_pak(0))
    gameclient.send_pak(started_help_pak())
    gameclient.send_pak(player_free_level_update_pak())

def send_mobs_and_mob_equipment_to_player(gameclient):
    # int mobs = 0;
    mobs = 0
    # if (player.CurrentRegion != null)
    # {
    # 	var npcs = player.GetNPCsInRadius(WorldMgr.VISIBILITY_DISTANCE).Cast<GameNPC>().ToArray();
    # 	foreach (GameNPC npc in npcs)
    # 	{
    # 		player.Out.SendNPCCreate(npc);
    # 		mobs++;
    # 		if (npc.Inventory != null)
    # 			player.Out.SendLivingEquipmentUpdate(npc);
    # 		}
    # }
    # return mobs;

    npcs = get_mobs_from_region(gameclient.player.current_region['region_id'])

    print 'LENGTH NPC, ' + str(len(npcs))

    for npc in npcs:
        if gameclient.player.in_zone(npc.get('X'), npc.get('Y'), gameclient.player.current_zone):
            gameclient.send_pak(npc_create_pak(npc, gameclient))
            if npc.get('inventory'):
                gameclient.send_pak(living_equipment_update_pak(npc, mobs, gameclient))
            mobs += 1
    print 'LENGTH MOBS, ' + str(mobs)
    return mobs

# p
# 				var player = (GamePlayer) m_actionSource;
#
# 				player.Out.SendUpdatePoints();
# 				player.TargetObject = null;
# 				// update the region color scheme which may be wrong due to ALLOW_ALL_REALMS support
# 				player.Out.SendRegionColorScheme();

# 				if (player.CurrentRegion != null)
# 				{
# 					player.CurrentRegion.Notify(RegionEvent.PlayerEnter, player.CurrentRegion, new RegionPlayerEventArgs(player));
# 				}
#
# 				int mobs = SendMobsAndMobEquipmentToPlayer(player);
# 				player.Out.SendTime();
#
# 				bool checkInstanceLogin = false;
#
# 				if (!player.EnteredGame)
# 				{
# 					player.EnteredGame = true;
# 					player.Notify(GamePlayerEvent.GameEntered, player);
# 					player.EffectList.RestoreAllEffects();
# 					checkInstanceLogin = true;
# 				}
# 				else
# 				{
# 					player.Notify(GamePlayerEvent.RegionChanged, player);
# 				}
# 				if (player.TempProperties.getProperty(GamePlayer.RELEASING_PROPERTY, false))
# 				{
# 					player.TempProperties.removeProperty(GamePlayer.RELEASING_PROPERTY);
# 					player.Notify(GamePlayerEvent.Revive, player);
# 					player.Notify(GamePlayerEvent.Released, player);
# 				}
# 				if (player.Group != null)
# 				{
# 					player.Group.UpdateGroupWindow();
# 					player.Group.UpdateAllToMember(player, true, false);
# 					player.Group.UpdateMember(player, true, true);
# 				}
# 				player.Out.SendPlayerInitFinished(0);
# 				player.TargetObject = null;
# 				player.StartHealthRegeneration();
# 				player.StartPowerRegeneration();
# 				player.StartEnduranceRegeneration();
# 				player.StartInvulnerabilityTimer(ServerProperties.Properties.TIMER_PLAYER_INIT * 1000, null);
#
# 				if (player.Guild != null)
# 				{
# 					SendGuildMessagesToPlayer(player);
# 				}
# 				SendHouseRentRemindersToPlayer(player);
# 				if (player.Level > 1 && Properties.MOTD != "")
# 				{
# 					player.Out.SendMessage(Properties.MOTD, eChatType.CT_System, eChatLoc.CL_SystemWindow);
# 				}
# 				else if (player.Level == 1)
# 				{
# 					player.Out.SendStarterHelp();
# 					if (Properties.STARTING_MSG != "")
# 						player.Out.SendMessage(Properties.STARTING_MSG, eChatType.CT_System, eChatLoc.CL_PopupWindow);
# 				}
#
# 				if (Properties.ENABLE_DEBUG)
# 					player.Out.SendMessage("Server is running in DEBUG mode!", eChatType.CT_System, eChatLoc.CL_SystemWindow);
#
# 				player.Out.SendPlayerFreeLevelUpdate();
# 				if (player.FreeLevelState == 2)
# 				{
# 					player.Out.SendDialogBox(eDialogCode.SimpleWarning, 0, 0, 0, 0, eDialogType.Ok, true,
# 					                         LanguageMgr.GetTranslation(player.Client.Account.Language, "PlayerInitRequestHandler.FreeLevel"));
# 				}
# 				player.Out.SendMasterLevelWindow(0);
# 				AssemblyName an = Assembly.GetExecutingAssembly().GetName();
# 				player.Out.SendMessage("Dawn of Light " + an.Name + " Version: " + an.Version, eChatType.CT_System,
# 				                       eChatLoc.CL_SystemWindow);
#
#
# 				if (Properties.TELEPORT_LOGIN_NEAR_ENEMY_KEEP)
# 				{
# 					CheckIfPlayerLogsNearEnemyKeepAndMoveIfNecessary(player);
# 				}
#
# 				if (Properties.TELEPORT_LOGIN_BG_LEVEL_EXCEEDED)
# 				{
# 					CheckBGLevelCapForPlayerAndMoveIfNecessary(player);
# 				}
#
# 				if (checkInstanceLogin)
# 				{
# 					if (WorldMgr.Regions[player.CurrentRegionID] == null || player.CurrentRegion == null || player.CurrentRegion.IsInstance)
# 					{
# 						Log.WarnFormat("{0}:{1} logging into instance or CurrentRegion is null, moving to bind!", player.Name, player.Client.Account.Name);
# 						player.MoveToBind();
# 					}
# 				}
#
# 				if (player.IsUnderwater)
# 				{
# 					player.IsDiving = true;
# 				}
# 				player.Client.ClientState = GameClient.eClientState.Playing;
