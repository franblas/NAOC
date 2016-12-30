from ..packets.packet_out import *

def update_points_pak(gameclient):

  realm_points = 0x00 #TODO
  level_permill = 0x00 #TODO
  skill_speciality_points = 0x00 #TODO
  bounty_points = 0x00 #TODO
  realm_speciality_points = 0x00 #TODO
  champion_level_permill = 0x00 #TODO
  experience = 0x00 #TODO
  experience_for_next_level = 0x32 #TODO
  champ_experience = 0x00
  champ_experience_for_next_level = 0x00

  ins = write_int(realm_points)
  ins += write_short(level_permill)
  ins += write_short(skill_speciality_points)
  ins += write_int(bounty_points)
  ins += write_short(realm_speciality_points)
  ins += write_short(champion_level_permill)
  ins += write_long(experience, endian='little')
  ins += write_long(experience_for_next_level, endian='little')
  ins += write_long(champ_experience, endian='little')
  ins += write_long(champ_experience_for_next_level, endian='little')

  pak = write_short(packet_length(ins))
  pak += write_byte(0x91)
  pak += ins
  return pak
