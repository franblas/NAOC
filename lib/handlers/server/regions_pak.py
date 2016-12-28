from ..packets.packet_out import *

def regions_pak():
  ins = write_byte(0)
  ins += write_byte(200) # RegionID, TODO
  ins += fill_pak(0, 20)
  ins += fill_string_pak("10300", 5)
  ins += fill_string_pak("10300", 5)
  ins += fill_string_pak("127.0.0.1", 20)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xB1)
  pak += ins
  return pak


		# public override void SendRegions()
		# {
		# 	if (m_gameClient.Player != null)
		# 	{
		# 		if (!m_gameClient.Socket.Connected)
		# 			return;
		# 		Region region = WorldMgr.GetRegion((ushort)m_gameClient.Player.CurrentRegionID);
		# 		if (region == null)
		# 			return;
		# 		using (GSTCPPacketOut pak = new GSTCPPacketOut(0xB1))
		# 		{
		# 			//				pak.WriteByte((byte)((region.Expansion + 1) << 4)); // Must be expansion
		# 			pak.WriteByte(0); // but this packet sended when client in old region. but this field must show expanstion for jump destanation region
		# 			//Dinberg - trying to get instances to work.
	    #             pak.WriteByte((byte)region.Skin); // This was pak.WriteByte((byte)region.ID);
		# 			pak.Fill(0, 20);
		# 			pak.FillString(region.ServerPort.ToString(), 5);
		# 			pak.FillString(region.ServerPort.ToString(), 5);
		# 			string ip = region.ServerIP;
		# 			if (ip == "any" || ip == "0.0.0.0" || ip == "127.0.0.1" || ip.StartsWith("10.13.") || ip.StartsWith("192.168."))
		# 				ip = ((IPEndPoint)m_gameClient.Socket.LocalEndPoint).Address.ToString();
		# 			pak.FillString(ip, 20);
		# 			SendTCP(pak);
		# 		}
		# 	}
		# 	else
		# 	{
		# 		RegionEntry[] entries = WorldMgr.GetRegionList();
        #
		# 		if (entries == null) return;
		# 		int index = 0;
		# 		int num = 0;
		# 		int count = entries.Length;
		# 		while (entries != null && count > index)
		# 		{
		# 			using (GSTCPPacketOut pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.ClientRegions)))
		# 			{
		# 				for (int i = 0; i < 4; i++)
		# 				{
		# 					while (index < count && (int)m_gameClient.ClientType <= entries[index].expansion)
		# 					{
		# 						index++;
		# 					}
        #
		# 					if (index >= count)
		# 					{	//If we have no more entries
		# 						pak.Fill(0x0, 52);
		# 					}
		# 					else
		# 					{
		# 						pak.WriteByte((byte)(++num));
		# 						pak.WriteByte((byte)entries[index].id);
		# 						pak.FillString(entries[index].name, 20);
		# 						pak.FillString(entries[index].fromPort, 5);
		# 						pak.FillString(entries[index].toPort, 5);
		# 						//Try to fix the region ip so UDP is enabled!
		# 						string ip = entries[index].ip;
		# 						if (ip == "any" || ip == "0.0.0.0" || ip == "127.0.0.1" || ip.StartsWith("10.13.") || ip.StartsWith("192.168."))
		# 							ip = ((IPEndPoint)m_gameClient.Socket.LocalEndPoint).Address.ToString();
		# 						pak.FillString(ip, 20);
        #
		# 						//							DOLConsole.WriteLine(string.Format(" ip={3}; fromPort={1}; toPort={2}; num={4}; id={0}; region name={5}", entries[index].id, entries[index].fromPort, entries[index].toPort, entries[index].ip, num, entries[index].name));
		# 						index++;
		# 					}
		# 				}
		# 				SendTCP(pak);
		# 			}
		# 		}
		# 	}
		# }
