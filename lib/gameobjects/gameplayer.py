import json

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
    current_zone = -1
    current_zone_id = 29
    current_region = -1
    current_region_id = 27
    is_underwater = False
    guild = dict()
    has_horse, active_horse = False, dict()
    crafting_skills = list()
    is_turning_disabled = False
    max_speed = -1
    current_speed = -1
    copper, silver, gold, mithril, platinum = -1, -1, -1, -1, -1 # money = dict()
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
        self.init_current_position()


    def init_current_position(self):
        self.current_position = {
            'X': self.db_character.get('x_pos'),
            'Y': self.db_character.get('y_pos'),
            'Z': self.db_character.get('z_pos'),
            'heading': 0
        }

        if self.current_position.get('X') == 0 and self.current_position.get('Y') == 0 and self.current_position.get('Z') == 0:
            startup_location = dict()
            with open("data/startup_locations.json", "r") as f:
                startup_locations = json.load(f).get('startup_locations')
            for loc in startup_locations:
                if int(loc.get('Region')) == self.current_region_id and int(loc.get('RealmID')) == self.db_character.get('realm'):
                    startup_location = loc
            if startup_location:
                self.current_position['X'] = int(startup_location.get('XPos'))
                self.current_position['Y'] = int(startup_location.get('YPos'))
                self.current_position['Z'] = int(startup_location.get('ZPos'))
                self.current_position['heading'] = int(startup_location.get('Heading'))
        print self.current_position
