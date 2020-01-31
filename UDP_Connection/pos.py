# Import the things
from pathlib import Path
from netconnect import *
import threading
from subprocess import call
# Define the class for the srver
class Server:
    # Init the host and port
    def __init__(self,host,port):
        self.host = host
        self.port = port
    # define the funciton to run the server
    def run_server(self, host, port):
        # set connect to be the netconnect the right things
        connect = NetConnect(host, port)
        # connect to the server
        connect.server()
    # define the funciton to run the POS by calling that code
    def run_pos(self):
        call(["python","pos2.py"])
    # define the funciton to run the things using multi threading
    def run(self):
        t1 = threading.Thread(target=self.run_server, args=[self.host,self.port, ])
        t2 = threading.Thread(target=self.run_pos)
        t1.start()
        t2.start()
# Define the main loop set the host to be localhost and the port to be 5555
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5555
    server = Server(host,port)
    server.run()


