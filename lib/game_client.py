from handlers.client.client_handler import client_handler
from world.world_update import WorldUpdate

class GameClient(object):

    request_counter = 0
    login_name = ''
    selected_character = dict()
    player = None
    world_update = None

    def __init__(self, session_id, clientsocket, SOCKET_BUFFER_SIZE):
        self.session_id = session_id
        self.clientsocket = clientsocket
        self.SOCKET_BUFFER_SIZE = SOCKET_BUFFER_SIZE
        self.world_update = WorldUpdate(self)

    def start(self):
        self.request_counter = 0
        self.world_update.update_player_NPCs()
        try:
            while True:
                resp = (self.clientsocket.recv(self.SOCKET_BUFFER_SIZE)).strip()
                server_pak = client_handler(resp, self.request_counter, self)
                self.request_counter += 1
                self.send_pak(server_pak)
        except Exception as e:
            print '[ERROR] GameClient ' + str(self.session_id) + ' exited. Err: ' + str(e)
            self.world_update.stop_world_updates()
            self.clientsocket.close()

    def send_pak(self, server_pak):
        if server_pak:
            print '----------------------------------'
            print server_pak
            print '----------------------------------'
            self.clientsocket.send(server_pak.decode('hex'))
        else:
            self.clientsocket.send('')
