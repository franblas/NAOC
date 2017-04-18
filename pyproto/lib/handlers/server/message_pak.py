from ..packets.packet_out import *

def message_pak(msg, msg_type, loc, gameclient):
  data = gameclient.selected_character
  if not data: return

  # pak.WriteShort(0xFFFF);
  ins = write_short(0xFFFF)
  # pak.WriteShort((ushort)m_gameClient.SessionID);
  ins += write_short(gameclient.session_id)
  # pak.WriteByte((byte)type);
  ins += write_byte(msg_type)
  # pak.Fill(0x0, 3);
  ins += fill_pak(0x00, 3)

  # string str;
  # if (loc == eChatLoc.CL_ChatWindow)
  # 	str = "@@";
  # else if (loc == eChatLoc.CL_PopupWindow)
  # 	str = "##";
  # else
  # 	str = "";
  st = ""
  ins += write_string(st + msg)

  pak = write_short(packet_length(ins))
  pak += write_byte(0xAF)
  pak += ins
  return pak

  # 		public override void SendMessage(string msg, eChatType type, eChatLoc loc)
  # 		{
  # 			if (m_gameClient.ClientState == GameClient.eClientState.CharScreen)
  # 				return;
  #
  # 			using (GSTCPPacketOut pak = new GSTCPPacketOut(GetPacketCode(eServerPackets.Message)))
  # 			{
  # 				pak.WriteShort(0xFFFF);
  # 				pak.WriteShort((ushort)m_gameClient.SessionID);
  # 				pak.WriteByte((byte)type);
  # 				pak.Fill(0x0, 3);
  #
  # 				string str;
  # 				if (loc == eChatLoc.CL_ChatWindow)
  # 					str = "@@";
  # 				else if (loc == eChatLoc.CL_PopupWindow)
  # 					str = "##";
  # 				else
  # 					str = "";
  #
  # 				pak.WriteString(str+msg);
  # 				SendTCP(pak);
  # 			}
  # 		}
