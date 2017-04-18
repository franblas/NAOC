from ..database.db_regions import get_region
from ..database.db_startup_locations import get_startup_location
from ..database.db_zones import get_zones_from_region

class GamePlayer(object):

    entered_game = False
    db_character = dict()
    race = ""
    ability_bonus = list()
    item_bonus = list()
    total_constitution_lost_at_death = -1
    # CharacterClass.ManaStat
    # CharacterClass.Name
    # CharacterClass.Profession
    level = 1
    max_health = -1
    concentration_effects = list()
    max_encumberance = -1
    encumberance = -1
    object_id = 1
    current_position = dict()
    current_zone = dict()
    current_region = dict()
    is_underwater = False
    guild = dict()
    has_horse, active_horse = False, dict()
    crafting_skills = list()
    is_turning_disabled = False
    max_speed = -1
    current_speed = -1
    money = dict()
    is_mezzed = False
    is_stunned = False
    is_strafing = False
    last_position_update_tick = -1
    last_position_update_point = {
        'X': -1,
        'Y': -1,
        'Z': -1
    }

    def __init__(self, db_character):
        self.db_character = db_character
        self.help_flag = self.db_character.get('no_help', True)
        self.init_current_region()
        self.init_current_position()
        self.init_current_zone()
        self.init_money()

    def init_current_region(self):
        db_region = self.db_character['region']
        self.current_region = get_region(db_region)
        print self.current_region

    def init_current_position(self):
        self.current_position = {
            'X': self.db_character['x_pos'],
            'Y': self.db_character['y_pos'],
            'Z': self.db_character['z_pos'],
            'heading': 0
        }

        if self.current_position['X'] == 0 and self.current_position['Y'] == 0 and self.current_position['Z'] == 0:
            startup_location = get_startup_location(self.current_region['region_id'], self.db_character['realm'])
            if startup_location:
                self.current_position['X'] = startup_location['x_pos']
                self.current_position['Y'] = startup_location['y_pos']
                self.current_position['Z'] = startup_location['z_pos']
                self.current_position['heading'] = startup_location['heading']
        print self.current_position

    def in_zone(self, x, y, zone):
        offset_x, offset_y = zone.get('offset_x'), zone.get('offset_y')
        width, height = zone.get('width'), zone.get('height')
        start_x, start_y = 8192*offset_x, 8192*offset_y
        end_x, end_y = start_x+(height*8192), start_y+(width*8192)
        if (start_x <= x <= end_x) and (start_y <= y <= end_y):
            return zone
        return

    def init_current_zone(self):
        potential_zones = get_zones_from_region(self.current_region['region_id'])
        for pzone in potential_zones:
            if self.in_zone(self.current_position['X'], self.current_position['Y'], pzone):
                self.current_zone = pzone
                break
        print self.current_zone


    def init_money(self):
        self.money = {
            'copper': self.db_character['copper'],
            'silver': self.db_character['silver'],
            'gold': self.db_character['gold'],
            'mithril': self.db_character['mithril'],
            'platinium': self.db_character['platinium']
        }
        print self.money
