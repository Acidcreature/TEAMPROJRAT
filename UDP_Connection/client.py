#netconnect and client_gui are in-house built modules for this program to run
from netconnect import *
from client_gui import *

#These modules are required for the functionality of this program
import threading
from pathlib import Path


#Start of the Client class
class Client:
    def __init__(self):
        pass

    #This will run the gui interface that is designed
    #to send udp packets to the server
    def client_gui(self):
        exec(Path(f'client/client.py').read_text())

    #This will start the client listener for the server to communicate with
    def client_listener(self):
        exec(Path(f'client/client_listener.py').read_text())

    #Multithreading to run both python files simultaneously
    def run(self):
        t1 = threading.Thread(target=self.client_gui)
        t2 = threading.Thread(target=self.client_listener)
        t1.start()
        t2.start()

#Start the program
if __name__ == '__main__':
    client = Client()
    client.run()
