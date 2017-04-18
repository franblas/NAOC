from ..packets.packet_out import *

def door_state_pak(region, door, gameclient):
  zone = int(float(door['door_id']) / 1000000)
  door_type = int(float(door['door_id'] / 100000000))
  flag = 0x01 #TODO
  door_state = door['door_state']
  print '-----> DOOR STATE: ' + str(door_state)
  # door_state = 0x01 if not bool(int(door_state)) else 0x00 # open = 0 # closed = 1
  door_state = 0x00 if not bool(int(door_state)) else 0x01 # open = 0 # closed = 1
  print 'CONDITIONAL DOOR STATE: ' + str(door_state)

  ins = write_int(door['door_id'])
  ins += write_byte(door_state)
  ins += write_byte(flag)
  ins += write_byte(0xFF)
  ins += write_byte(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x99)
  pak += ins
  return pak


# Door should be closed 10s after automaticaly
def close_door(region, door, gameclient):
  door['door_state'] = 0x00
  gameclient.send_pak(door_state_pak(region, door, gameclient))

  # using (var pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.DoorState)))
  # {
  # 	ushort zone = (ushort)(door.DoorID / 1000000);
  # 	int doorType = door.DoorID / 100000000;
  # 	uint flag = door.Flag;
  # 	# by default give all unflagged above ground non keep doors a default sound (excluding TrialsOfAtlantis zones)
  # 	if (flag == 0 && doorType != 7 && region != null && region.IsDungeon == false && region.Expansion != (int)eClientExpansion.TrialsOfAtlantis)
  # 	{
  # 		flag = 1;
  # 	}
  # 	pak.WriteInt((uint)door.DoorID);
  # 	pak.WriteByte((byte)(door.State == eDoorState.Open ? 0x01 : 0x00));
  # 	pak.WriteByte((byte)flag);
  # 	pak.WriteByte(0xFF);
  # 	pak.WriteByte(0x0);
  # 	SendTCP(pak);
  # }
