from ..packets.packet_out import *

def player_position_and_objectid_pak(gameclient):
  data = gameclient.selected_character
  if not data: return

  player = gameclient.player

  # pak.WriteShort((ushort)m_gameClient.Player.ObjectID); //This is the player's objectid not Sessionid!!!
  ins = write_short(player.object_id)

  # pak.WriteShort((ushort)m_gameClient.Player.Z);
  ins += write_short(player.current_position.get('Z'))

  # pak.WriteInt((uint)m_gameClient.Player.X);
  ins += write_int(player.current_position.get('X'))

  # pak.WriteInt((uint)m_gameClient.Player.Y);
  ins += write_int(player.current_position.get('Y'))

  # pak.WriteShort(m_gameClient.Player.Heading);
  ins += write_short(player.current_position.get('heading'))

  # int flags = 0;
  flags = 0

  # Zone zone = m_gameClient.Player.CurrentZone;
  # if (zone == null) return;
  zone = '' # data['current_zone']
  # if not zone: return

  # if (m_gameClient.Player.CurrentZone.IsDivingEnabled)
  #     flags = 0x80 | (m_gameClient.Player.IsUnderwater ? 0x01 : 0x00);
  #
  # pak.WriteByte((byte)(flags));
  ins += write_byte(flags)

  # pak.WriteByte(0x00);	//TODO Unknown (Instance ID: 0xB0-0xBA, 0xAA-0xAF)
  ins += write_byte(0x00)

  # if (zone.IsDungeon)
  # {
  #     pak.WriteShort((ushort)(zone.XOffset / 0x2000));
  #     pak.WriteShort((ushort)(zone.YOffset / 0x2000));
  # }
  # else
  # {
  #     pak.WriteShort(0);
  #     pak.WriteShort(0);
  # }
  ins += write_short(0x00)
  ins += write_short(0x00)

  # //Dinberg - Changing to allow instances...
  # pak.WriteShort(m_gameClient.Player.CurrentRegion.Skin);
  ins += write_short(int(player.current_region['region_id']))

  # pak.WritePascalString(GameServer.Instance.Configuration.ServerNameShort); // new in 1.74, same as in SendLoginGranted
  ins += write_pascal_string('NAOC')

  # pak.WriteByte(0x00); //TODO: unknown, new in 1.74
  ins += write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x20)
  pak += ins
  return pak
