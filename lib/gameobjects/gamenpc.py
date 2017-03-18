from ..database.db_zones import get_zones_from_region

from ..world.points import new_coordinates_from_heading, opposite_heading, left_heading

class GameNPC(object):

    eflags = {
        'ghost': 0x01,
        'stealth': 0x02,
        'dont_show_name': 0x04,
        'cant_target': 0x08,
        'peace': 0x10,
        'flying': 0x20,
        'torch': 0x40,
        'statue': 0x80,
        'swimming': 0x100
    }
    inventory = { 'visible_items': [] }
    object_type = 'npc'
    zone = dict()
    mvt_iteration = 0

    def __init__(self, npc_data):
        for key in npc_data.keys(): setattr(self, key, npc_data[key])
        self.init_current_zone()
        self.speed = 0 #HACK: reset speed in order to test paths.
        self.flags = 4 #HACK a lot of wrong flags into the db

    def init_current_zone(self):
        potential_zones = get_zones_from_region(self.region)
        for pzone in potential_zones:
            if self.in_zone(self.X, self.Y, pzone): self.zone = pzone

    def in_zone(self, x, y, zone):
        offset_x, offset_y = zone.get('offset_x'), zone.get('offset_y')
        width, height = zone.get('width'), zone.get('height')
        start_x, start_y = 8192*offset_x, 8192*offset_y
        end_x, end_y = start_x+(height*8192), start_y+(width*8192)
        if (start_x <= x <= end_x) and (start_y <= y <= end_y):
            return zone
        return

    def movement(self, heading_type):
        self.speed = 20
        xx, yy = new_coordinates_from_heading(self.X, self.Y, self.heading, self.speed*10) # distance = speed * npc_update_interval
        self.X, self.Y = xx, yy
        if self.mvt_iteration == 2:
            new_heading = heading_type(self.heading)
            self.heading = new_heading
            self.mvt_iteration = 0
        else:
            self.mvt_iteration += 1

    def update(self):
        # if lname == 'guardian': self.aller_retour()
        if self.name.strip().lower() == 'guardian':
            self.movement(opposite_heading)
        if self.name.strip().lower() == 'ambient stag':
            self.movement(left_heading)
