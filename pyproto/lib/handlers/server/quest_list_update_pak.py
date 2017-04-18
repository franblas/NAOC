from ..packets.packet_out import *

def quest_list_update_pak(gameclient):
  data = gameclient.selected_character
  if not data: return

  gameclient.send_pak(first_quest(gameclient))
  for i in range(1, 20):
    gameclient.send_pak(quest_packet(gameclient, i))


def quest_packet(gameclient, index):
  data = gameclient.selected_character
  if not data: return

  # pak.WriteByte((byte)index);
  ins = write_byte(index)
  # pak.WriteByte((byte)quest.Name.Length);
  ins += write_byte(0x00)
  # pak.WriteShort(0x00); # unknown
  ins += write_byte(0x00)
  # pak.WriteByte((byte)quest.Goals.Count);
  ins += write_byte(0x00)
  # pak.WriteByte((byte)quest.Level);
  ins += write_byte(0x00)
  # pak.WriteStringBytes(quest.Name);
  ins += write_byte(0x00)
  # pak.WritePascalString(quest.Description);
  ins += write_pascal_string('')
  # int goalindex = 0;
  # foreach (RewardQuest.QuestGoal goal in quest.Goals)
  # {
  # 	goalindex++;
  # 	String goalDesc = String.Format("{0}\r", goal.Description);
  # 	pak.WriteShortLowEndian((ushort)goalDesc.Length);
  # 	pak.WriteStringBytes(goalDesc);
  # 	pak.WriteShortLowEndian((ushort)goal.ZoneID2);
  # 	pak.WriteShortLowEndian((ushort)goal.XOffset2);
  # 	pak.WriteShortLowEndian((ushort)goal.YOffset2);
  # 	pak.WriteShortLowEndian(0x00);	# unknown
  # 	pak.WriteShortLowEndian((ushort)goal.Type);
  # 	pak.WriteShortLowEndian(0x00);	# unknown
  # 	pak.WriteShortLowEndian((ushort)goal.ZoneID1);
  # 	pak.WriteShortLowEndian((ushort)goal.XOffset1);
  # 	pak.WriteShortLowEndian((ushort)goal.YOffset1);
  # 	pak.WriteByte((byte)((goal.IsAchieved) ? 0x01 : 0x00));
  # 	if (goal.QuestItem == null)
  # 		pak.WriteByte(0x00);
  # 	else
  # 	{
  # 		pak.WriteByte((byte)goalindex);
  # 		WriteTemplateData(pak, goal.QuestItem, 1);
  #
  pak = write_short(packet_length(ins))
  pak += write_byte(0x83)
  pak += ins
  return pak

def first_quest(gameclient):
  data = gameclient.selected_character
  if not data: return

  # pak.WriteByte((byte)index);
  ins = write_byte(0x00)
  # pak.WriteByte((byte)quest.Name.Length);
  ins += write_byte(23)
  # pak.WriteShort(0x00); # unknown
  ins += write_byte(0x00)
  # pak.WriteByte((byte)quest.Goals.Count);
  ins += write_byte(0x00)
  # pak.WriteByte((byte)quest.Level);
  ins += write_byte(0x00)
  # pak.WriteStringBytes(quest.Name);
  ins += write_byte(0x00)
  # pak.WritePascalString(quest.Description);
  ins += write_pascal_string("You have no current personal task.")
  pak = write_short(packet_length(ins))
  pak += write_byte(0x83)
  pak += ins
  return pak
