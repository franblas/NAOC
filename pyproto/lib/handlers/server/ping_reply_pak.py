from ..packets.packet_out import *

# timestamp = arrow.now().timestamp
# sequence is the number of requests already sent to the client
def ping_reply_pak(timestamp, sequence):
  ins = write_int(timestamp)
  ins += fill_pak(0x00, 4)
  ins += write_short(sequence + 1)
  ins += fill_pak(0x00, 6)

  pak = write_short(packet_length(ins))
  pak += write_byte(0x29)
  pak += ins
  return pak
