from ..packets.packet_in import skip, read_int
from ..server.ping_reply_pak import ping_reply_pak
import arrow

def ping_request_handler(packet):
    with open('request_counter', 'r') as f:
        request_counter = int(f.read())
    cursor = 0
    cursor = skip(cursor, 4)
    timestamp, cursor = read_int(packet, cursor)
    return ping_reply_pak(arrow.now().timestamp, request_counter)
