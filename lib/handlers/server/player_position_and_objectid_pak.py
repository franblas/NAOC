from ..packets.packet_out import *

def player_position_and_objectid_pak(gameclient):
  data = gameclient.selected_character
  if not data: return

  data = {
    'object_id': 0x0007,
    'Z': 0x14DC,
    'X': 0x0005759C,
    'Y': 0x00058BC1,
    'heading': 0x0400,
    'current_zone': '',
    'current_region': {
      'skin': 0x001B
    }
  }

  # pak.WriteShort((ushort)m_gameClient.Player.ObjectID); //This is the player's objectid not Sessionid!!!
  ins = write_short(data['object_id'])

  # pak.WriteShort((ushort)m_gameClient.Player.Z);
  ins += write_short(data['Z'])

  # pak.WriteInt((uint)m_gameClient.Player.X);
  ins += write_int(data['X'])

  # pak.WriteInt((uint)m_gameClient.Player.Y);
  ins += write_int(data['Y'])

  # pak.WriteShort(m_gameClient.Player.Heading);
  ins += write_short(data['heading'])

  # int flags = 0;
  flags = 0

  # Zone zone = m_gameClient.Player.CurrentZone;
  # if (zone == null) return;
  zone = data['current_zone']
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
  ins += write_short(data['current_region']['skin'])

  # pak.WritePascalString(GameServer.Instance.Configuration.ServerNameShort); // new in 1.74, same as in SendLoginGranted
  ins += write_pascal_string('pyDOL')

  # pak.WriteByte(0x00); //TODO: unknown, new in 1.74
  ins += write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x20)
  pak += ins
  return pak
