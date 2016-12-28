import socket
import threading

from lib.game_client import GameClient

TCP_IP = "127.0.0.1"
TCP_PORT = 10300
SOCKET_BUFFER_SIZE = 16 * 1024
SESSION_ID = 1

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SOCKET_BUFFER_SIZE)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(100)

while True:
  connect, addr = sock.accept()
  gc = GameClient(SESSION_ID, connect, SOCKET_BUFFER_SIZE)
  t = threading.Thread(name='client_' + str(SESSION_ID), target=gc.start)
  t.start()
  SESSION_ID += 1
sock.close()
