#Modules imported for network framework
from netconnect import *
import threading
from subprocess import call

# Define the class for the server
class Server:
    # Init the host and port
    def __init__(self,host,port):
        self.host = host
        self.port = port

    # define the function to run the server
    def run_server(self, host, port):
        # Utilize NetConnect class from netconnect.py (network framework built from scratch)
        connect = NetConnect(host, port)
        # Start the server module from netconnect.py (starts listener)
        connect.server()

    # Initiates GUI for POS
    def run_pos(self):
        call(["pythonw","pos_gui.py"])

    # Multi-threading to allow GUI and listener to function simultaneously
    def run(self):
        t1 = threading.Thread(target=self.run_server, args=[self.host,self.port, ]) #Begin GUi
        t2 = threading.Thread(target=self.run_pos)                                  #Begin listener
        t1.start()
        t2.start()

# Define the main loop set the host to be localhost and the port to be 5555
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5555
    server = Server(host,port)
    server.run()


