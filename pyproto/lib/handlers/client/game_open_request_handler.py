from ..packets.packet_in import read_byte
from ..server.game_open_pak import game_open_pak
from ..server.status_update_pak import status_update_pak
from ..server.update_points_pak import update_points_pak
from ..server.update_disabled_skills_pak import update_disabled_skills_pak

def game_open_request_handler(packet,gameclient):
    cursor = 0
    flag, cursor = read_byte(packet, cursor)
    gameclient.send_pak(game_open_pak())
    gameclient.send_pak(status_update_pak(0, gameclient))
    gameclient.send_pak(update_points_pak(gameclient))
    # gameclient.send_pak(update_disabled_skills_pak(gameclient))

# int flag = packet.ReadByte();
# client.UdpPingTime = DateTime.Now.Ticks;
# client.UdpConfirm = flag == 1;
# client.Out.SendGameOpenReply();
# client.Out.SendStatusUpdate(); # based on 1.74 logs
# client.Out.SendUpdatePoints(); # based on 1.74 logs
# if (client.Player != null)
# 	client.Player.UpdateDisabledSkills(); # based on 1.74 logs
