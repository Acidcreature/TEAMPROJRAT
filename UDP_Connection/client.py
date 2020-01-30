from netconnect import *
from gui2 import *
import threading
from pathlib import Path

class Client:
    def __init__(self):
        pass

    def client_gui(self):
        exec(Path(f'client/client.py').read_text())

    def client_listener(self):
        exec(Path(f'client/client_listener.py').read_text())

    def run(self):
        t1 = threading.Thread(target=self.client_gui)
        t2 = threading.Thread(target=self.client_listener)
        t1.start()
        t2.start()

if __name__ == '__main__':
    client = Client()
    client.run()
