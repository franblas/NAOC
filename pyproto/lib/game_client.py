import asyncore

from handlers.client.client_handler import client_handler
from world.world_manager import WorldManager

SOCKET_BUFFER_SIZE = 16 * 1024

class GameClient(asyncore.dispatcher):

    request_counter = 0
    login_name = ''
    selected_character = dict()
    player = None

    def __init__(self, session_id, clientsocket):
        asyncore.dispatcher.__init__(self, clientsocket)
        self.data_to_write = list()
        self.session_id = session_id

    def writable(self):
        return bool(self.data_to_write)

    def handle_write(self):
        data = self.data_to_write.pop()
        sent = self.send(data[:SOCKET_BUFFER_SIZE])
        if sent < len(data):
            remaining = data[sent:]
            self.data.to_write.append(remaining)

    def handle_read(self):
        data = self.recv(SOCKET_BUFFER_SIZE)
        resp = data.rstrip()
        server_pak = client_handler(resp, self.request_counter, self) or ''
        self.request_counter += 1
        self.data_to_write.insert(0, server_pak.decode('hex'))

    def send_pak(self, server_pak):
        dec = server_pak or ''
        self.data_to_write.insert(0, dec.decode('hex'))

    def handle_close(self):
        wm = WorldManager.get_world_manager()
        gcs = wm.gameclients
        if gcs.get(str(self.session_id)): del gcs[str(self.session_id)]
        self.close()
