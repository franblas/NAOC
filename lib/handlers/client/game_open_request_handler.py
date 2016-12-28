from ..packets.packet_in import read_byte
from ..server.game_open_pak import game_open_pak

def game_open_request_handler(packet,gameclient):
    cursor = 0
    flag, cursor = read_byte(packet, cursor)
    game_open_pak()
    # status_update_pak()
    # update_points_pak()
    # update_disabled_skills_pak()

# int flag = packet.ReadByte();
# client.UdpPingTime = DateTime.Now.Ticks;
# client.UdpConfirm = flag == 1;
# client.Out.SendGameOpenReply();
# client.Out.SendStatusUpdate(); // based on 1.74 logs
# client.Out.SendUpdatePoints(); // based on 1.74 logs
# if (client.Player != null)
# 	client.Player.UpdateDisabledSkills(); // based on 1.74 logs
