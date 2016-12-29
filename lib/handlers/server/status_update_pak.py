from ..packets.packet_out import *

def status_update_pak(sitting_flag, gameclient):
  data = gameclient.selected_character
  if not data: return

  health = data.get('constitution') # ??? TODO
  health_max = data.get('constitution')
  health_percent = (health * 1.0 / health_max) * 100

  mana = data.get('concentration') # ??? TODO
  mana_max = data.get('concentration')
  mana_percent = (mana * 1.0 / mana_max) * 100

  endurance = data.get('endurance')
  endurance_max = data.get('max_endurance')
  endurance_percent = (endurance * 1.0 / endurance_max) * 100

  concentration = data.get('concentration')
  concentration_max = data.get('concentration')
  concentration_percent = (concentration * 1.0 / concentration_max) * 100

  ins = write_byte(health_percent) # HealthPercent, TODO
  ins += write_byte(mana_percent) # ManaPercent, TODO
  ins += write_byte(sitting_flag) # sittingFlag, TODO
  ins += write_byte(endurance_percent) # EndurancePercent, TODO
  ins += write_byte(concentration_percent) # ConcentrationPercent, TODO
  ins += write_byte(0) # unk
  ins += write_short(mana_max) # MaxMana, TODO
  ins += write_short(endurance_max) # MaxEndurance, TODO
  ins += write_short(concentration_max) # MaxConcentration, TODO
  ins += write_short(health_max) # MaxHealth, TODO
  ins += write_short(health) # Health, TODO
  ins += write_short(endurance) # Endurance, TODO
  ins += write_short(mana) # Mana, TODO
  ins += write_short(concentration) # Concentration, TODO

  pak = write_short(packet_length(ins))
  pak += write_byte(0xAD)
  pak += ins
  return pak
