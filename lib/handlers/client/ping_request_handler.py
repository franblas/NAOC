from ..packets.packet_in import skip, read_int
from ..server.ping_reply_pak import ping_reply_pak
import arrow

def ping_request_handler(packet,gameclient):
    request_counter = gameclient.request_counter
    cursor = 0
    cursor = skip(cursor, 4)
    timestamp, cursor = read_int(packet, cursor)
    return ping_reply_pak(arrow.now().timestamp, request_counter)
