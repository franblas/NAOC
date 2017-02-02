from ..packets.packet_out import *

def started_help_pak():
  ins = write_short(0x01)

  ins += write_short(0x00)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xF7)
  pak += ins
  return pak

  # public virtual void SendStarterHelp()
  # {
  # 	//* 0:00:57.984 S=>C 0xF7 show help window (topicIndex:1 houseLot?:0)
  # 	using (var pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.HelpWindow)))
  # 	{
  # 		pak.WriteShort(1); //short index
  # 		pak.WriteShort(0); //short lot
  # 		SendTCP(pak);
  # 	}
  # }
