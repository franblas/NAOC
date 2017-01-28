
from handlers.client.client_handler import client_handler

class GameClient(object):

    request_counter = 0
    login_name = ''
    selected_character = dict()

    def __init__(self, session_id, clientsocket, SOCKET_BUFFER_SIZE):
        self.session_id = session_id
        self.clientsocket = clientsocket
        self.SOCKET_BUFFER_SIZE = SOCKET_BUFFER_SIZE

    def start(self):
        self.request_counter = 0
        while True:
            resp = (self.clientsocket.recv(self.SOCKET_BUFFER_SIZE)).strip()
            server_pak = client_handler(resp, self.request_counter, self)
            self.request_counter += 1
            self.send_pak(server_pak)
        self.clientsocket.close()

    def send_pak(self, server_pak):
        if server_pak:
            print server_pak.decode('hex')
            self.clientsocket.send(server_pak.decode('hex'))
        else:
            self.clientsocket.send('')
