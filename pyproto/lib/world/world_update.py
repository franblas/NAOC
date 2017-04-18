import time
import gevent
# from gevent.pool import Pool

from world_manager import WorldManager
from points import new_coordinates_from_heading
from ..handlers.server.object_update_pak import object_update_pak

class WorldUpdate(object):

    GLOBAL_NPC_UPDATE_INTERVAL = 10.0 # 10secs
    update_NPCs_timer = None

    def __init__(self):
        pass
        # self.POOL_PROCESSES_NB = 10
        # self.pool = Pool(self.POOL_PROCESSES_NB)

    def update_NPCs(self):
        gevent.Greenlet.spawn(self.update_NPCs_loop)

    def update_NPCs_loop(self):
        while True:
            gevent.sleep(self.GLOBAL_NPC_UPDATE_INTERVAL)
            self.update_NPCs_callback()

    # test to update all npcs
    def update_NPCs_callback(self):
        wm = WorldManager.get_world_manager()
        if not wm: return

        gameclients = wm.gameclients
        if not gameclients: return

        npcs = wm.npcs
        print 'LENGTH NPC, ' + str(len(npcs))
        mobs = 0

        time1 = time.time()
        region_already_updated = list()
        for gameclient in gameclients.values():
            if not gameclient.player: continue

            player_region = gameclient.player.current_region.get('region_id')
            if player_region not in region_already_updated:
                region_already_updated.append(player_region)
            else:
                continue

            player_zone = gameclient.player.current_zone.get('zone_id')
            for npc in npcs:
                if npc.region == player_region:
                    npc.update()
                    if player_zone == npc.zone.get('zone_id'):
                        gameclient.send_pak(object_update_pak(gameclient, npc))

        # NOTE
        # should be parallelized. Batch npcs by x and then
        # enqueue a job with this batch into task queue
        # chunk_size = len(npcs) / (self.POOL_PROCESSES_NB - 1)
        # split_npcs = [npcs[i:i+chunk_size] for i in xrange(0, len(npcs), chunk_size)]
        # print 'NB OF TASKS: ' + str(len(split_npcs))
        # self.task(npcs, gameclients)
        # for npcs_batch in split_npcs: self.pool.spawn(self.task, npcs_batch, gameclients)
        # self.pool.join()

        time2 = time.time()
        print 'Function took '  + str((time2-time1)*1000.0) + ' ms'

    def task(self, npcs, gameclients):
        for npc in npcs:
            npc.update()
            for gameclient in gameclients.values():
                if not gameclient.player: continue
                if gameclient.player.current_zone.get('zone_id') == npc.zone.get('zone_id'):
                    gameclient.send_pak(object_update_pak(gameclient, npc))

    # def stop_world_updates(self):
    #     self.update_NPCs_timer.cancel()
