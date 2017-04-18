from gevent import monkey
monkey.patch_all()

import socket
import asyncore

from lib.game_client import GameClient

from lib.world.world_manager import WorldManager
from lib.world.world_update import WorldUpdate

TCP_IP = '127.0.0.1'
TCP_PORT = 10300
MAX_CONNECTIONS = 100

class Server(asyncore.dispatcher):
    def __init__(self, address):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(address)
        self.address = self.socket.getsockname()
        self.listen(MAX_CONNECTIONS)
        self.SESSION_IDS = [i for i in range(1, MAX_CONNECTIONS)]

    def handle_accept(self):
        client_info = self.accept()
        if client_info:
            wm = WorldManager.get_world_manager()
            gcs = wm.gameclients
            session_id = self.new_session_id(gcs)
            print 'session_id ' + str(session_id)
            gc = GameClient(session_id, client_info[0])
            gcs[str(session_id)] = gc

    def new_session_id(self, gcs):
        gcs_session_ids = [int(s) for s in gcs.keys()]
        available_session_ids = [x for x in self.SESSION_IDS if x not in gcs_session_ids]
        return available_session_ids[0]


def main():
    # World init and update loop
    wm, wup = WorldManager(), WorldUpdate()
    wup.update_NPCs()

    # Start server
    s = Server((TCP_IP, TCP_PORT))
    asyncore.loop()

    # Server down, stop all threads
    # wup.stop_world_updates()

if __name__ == '__main__':
    main()
