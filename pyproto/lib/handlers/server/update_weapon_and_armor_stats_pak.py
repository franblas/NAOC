from ..packets.packet_out import *

def update_weapon_and_armor_stats_pak(gameclient):
  data = gameclient.selected_character
  if not data: return

  # pak.WriteByte(0x05); #subcode
  ins = write_byte(0x05)

  # pak.WriteByte(6); #number of entries
  ins += write_byte(0x06)

  # pak.WriteByte(0x00); #subtype
  ins += write_byte(0x00)

  # pak.WriteByte(0x00); #unk
  ins += write_byte(0x00)

  # # weapondamage
  # var wd = (int) (m_gameClient.Player.WeaponDamage(m_gameClient.Player.AttackWeapon)*100.0);
  # pak.WriteByte((byte) (wd/100));
  ins += write_byte(0x00)

  # pak.WritePascalString(" ");
  ins += write_pascal_string(" ")

  # pak.WriteByte((byte) (wd%100));
  ins += write_byte(0x00)

  # pak.WritePascalString(" ");
  ins += write_pascal_string(" ")

  # # weaponskill
  # int ws = m_gameClient.Player.DisplayedWeaponSkill;
  # pak.WriteByte((byte) (ws >> 8));
  ins += write_byte(0x00)

  # pak.WritePascalString(" ");
  ins += write_pascal_string(" ")

  # pak.WriteByte((byte) (ws & 0xff));
  ins += write_byte(0x00)

  # pak.WritePascalString(" ");
  ins += write_pascal_string(" ")

  # # overall EAF
  # int eaf = m_gameClient.Player.EffectiveOverallAF;
  # pak.WriteByte((byte) (eaf >> 8));
  ins += write_byte(0x00)

  # pak.WritePascalString(" ");
  ins += write_pascal_string(" ")

  # pak.WriteByte((byte) (eaf & 0xff));
  ins += write_byte(0x00)

  # pak.WritePascalString(" ");
  ins += write_pascal_string(" ")

  pak = write_short(packet_length(ins))
  pak += write_byte(0x16)
  pak += ins
  return pak
