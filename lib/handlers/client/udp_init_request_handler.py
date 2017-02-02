from ..packets.packet_in import read_string, read_short
from ..server.udp_init_reply_pak import udp_init_reply_pak

def udp_init_request_handler(packet,gameclient):
    cursor = 0
    # string localIP = packet.ReadString(22);
    local_ip, cursor = read_string(packet, 22, cursor)
    # ushort localPort = packet.ReadShort();
    local_port, cursor = read_short(packet, cursor)
    # client.LocalIP = localIP;
    # client.Out.SendUDPInitReply();
    gameclient.send_pak(udp_init_reply_pak(gameclient))
