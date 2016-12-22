import socket
import arrow

from handlers.client.client_handler import client_handler

TCP_IP = "127.0.0.1"
TCP_PORT = 10300
SOCKET_BUFFER_SIZE = 2048

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
sock.bind((TCP_IP, TCP_PORT))
sock.listen(100)

REQUEST_COUNTER = 0
connect, address = sock.accept()
while True:
  resp = (connect.recv(SOCKET_BUFFER_SIZE)).strip()
  # with open('plip/plip_' + str(REQUEST_COUNTER), 'wb') as p:
  #   p.write(resp)
  #print "resp: ",resp
  server_pak = client_handler(resp, REQUEST_COUNTER)
  REQUEST_COUNTER += 1
  if server_pak:
    connect.send(server_pak.decode('hex'))
  else:
    connect.send('')

  print "\ndone",address
connect.close()
