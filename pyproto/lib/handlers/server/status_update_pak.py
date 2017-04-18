from ..packets.packet_out import *

def percentage(val, max_val):
  return int((val * 1.0 / max_val) * 100)

def status_update_pak(sitting_flag, gameclient):
  data = gameclient.selected_character
  if not data: return

  health = 0x01 # TODO
  health_max = 0x1E # TODO (30)
  health_percent = percentage(health, health_max)

  mana = 0x00 # TODO
  mana_max = 0x19 #TODO (25)
  mana_percent = percentage(mana, mana_max)

  endurance = 0x64 #TODO (100)
  endurance_max = 0x64 #TODO (100)
  endurance_percent = percentage(endurance, endurance_max)

  concentration = 0x04 #TODO
  concentration_max = 0x04 #TODO
  concentration_percent = percentage(concentration, concentration_max)

  ins = write_byte(health_percent)
  ins += write_byte(mana_percent)
  ins += write_byte(sitting_flag)
  ins += write_byte(endurance_percent)
  ins += write_byte(concentration_percent)
  ins += write_byte(0) # unk
  ins += write_short(mana_max)
  ins += write_short(endurance_max)
  ins += write_short(concentration_max)
  ins += write_short(health_max)
  ins += write_short(health)
  ins += write_short(endurance)
  ins += write_short(mana)
  ins += write_short(concentration)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xAD)
  pak += ins
  return pak
