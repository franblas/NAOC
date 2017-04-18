from ..packets.packet_out import *

def update_money_pak(gameclient):
  data = gameclient.selected_character
  if not data: return

  player_money = gameclient.player.money

  ins = write_byte(player_money.get('copper'))
  ins += write_byte(player_money.get('silver'))
  ins += write_short(player_money.get('gold'))
  ins += write_short(player_money.get('mithril'))
  ins += write_short(player_money.get('platinium'))

  pak = write_short(packet_length(ins))
  pak += write_byte(0xFA)
  pak += ins
  return pak
