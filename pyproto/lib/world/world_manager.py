import time
import ctypes

from ..database.db_mobs import get_all_mobs, get_mobs_from_region
from ..gameobjects.gamenpc import GameNPC

WM_DATA = '.wm_data'

class WorldManager(object):
    """
    gameclients: dictionary of all current game clients
    npcs: list of all current game npcs
    """
    gameclients = dict()
    npcs = list()

    def __init__(self):
        print 'Loading npcs ...'
        i, mobs = 0.0, get_mobs_from_region(200)
        # i, mobs = 0.0, get_all_mobs()
        mobs_l = len(mobs)
        for m in mobs:
            self.npcs.append(GameNPC(m))
            plop = round((i / mobs_l)*100)
            if int(plop) % 5 == 0: print str(plop) + '%'
            i += 1
        # [GameNPC(m) for m in get_all_mobs()]
        time.sleep(2)
        self.register_data()

    def register_data(self):
        with open(WM_DATA, 'w') as f:
            f.write(str(id(self)))

    @staticmethod
    def get_world_manager():
        with open(WM_DATA, 'r') as f:
            wm_object_str = f.read()
        wm = ctypes.cast(int(wm_object_str), ctypes.py_object).value
        return wm
