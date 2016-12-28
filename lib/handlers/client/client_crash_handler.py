from ..packets.packet_in import read_string, read_int

def client_crash_handler(packet,gameclient):
  cursor = 0
  dll_name, cursor = read_string(packet, 16, cursor)
  print "Client crash! :("
  print dll_name
  cursor = 0x50
  up_time, cursor = read_int(packet, cursor)
  print "UP TIME"
  print up_time
