import threading

from ..handlers.server.object_update_pak import object_update_pak
from ..database.db_mobs import get_mobs_from_region

class WorldUpdate(object):

    # game_clients_list = list()
    GLOBAL_NPC_UPDATE_INTERVAL = 10.0 # 10secs
    gameclient = None
    update_player_NPCs_timer = None

    def __init__(self, gameclient):
        self.gameclient = gameclient

    # def get_all_game_clients(self):
    #     return [t for t in threading.enumerate() if t.startswith('client_')] or list()

    def update_player_NPCs(self):
        self.update_player_NPCs_timer = threading.Timer(self.GLOBAL_NPC_UPDATE_INTERVAL, self.update_player_NPCs)
        self.update_player_NPCs_timer.name = 'update_player_NPCs_timer_client_' + str(self.gameclient.session_id)
        self.update_player_NPCs_timer.start()

        if not self.gameclient.player: return

        npcs = get_mobs_from_region(self.gameclient.player.current_region['region_id'])
        print 'LENGTH NPC, ' + str(len(npcs))
        mobs = 0

        for npc in npcs:
            if self.gameclient.player.in_zone(npc.get('X'), npc.get('Y'), self.gameclient.player.current_zone):
                self.gameclient.send_pak(object_update_pak(self.gameclient, npc))
                #if npc.get('inventory'):
                #    gameclient.send_pak(living_equipment_update_pak(npc, mobs, gameclient))
                mobs += 1
        print 'LENGTH MOBS, ' + str(mobs)

    def stop_world_updates(self):
        self.update_player_NPCs_timer.cancel()
