#Modules imported for network framework
import socket
from pathlib import Path
import sys
import subprocess

#NetConnect is the name of the network framework
class NetConnect:
    def __init__(self, hostname, port):
        self.hostname = hostname            #hostname accepts ip addresses
        self.port = port                    #Default port for the server is 5555 and client listener is 6667

    #May be used to change the hostname
    def set_hostname(self, hostname):
        self.hostname = hostname

    #Utilized to set message sent
    def set_message(self, message):
        self.message = bytes(message, encoding="utf-8")

    #Retrieve the hostname
    def get_hostname(self):
        return self.hostname

    #Retrieve the port
    def get_port(self):
        return self.port

    #Retrieve data within message
    def get_message(self):
        if self.message:
            return self.message
        else:
            return

    #Send message to client/server
    def send_message(self,sock,message,ip,port):
        sock.sendto(message,(ip,port))

    #Receive message from client/server
    def rec_message(self,sock):
        data, addr = sock.recvfrom(4096)
        return data, addr

    #Genereates the message that will be used in transmition
    def message_generator(self,message):
        orig_stdout = sys.stdout            #save the status of original standard out (terminal by default)
        file = open('text.txt','w')         #File used for storing data
        sys.stdout = file                   #Standard out will change from terminal to the file
        if '.py' in message:                #If statement to find if python file is called in message
            exec(Path(f'toolkit/{message}').read_text())    #Execute python file if the 'if' statement is true
        elif '.exe' in message:             #If statement to find if exe file is called in message
            test = subprocess.check_output([f'toolkit/' + message]).decode('ascii')    #Execute exe file on server
            print(test)                     #print results to the file (standard out is still calling on the file)
        else:
            print(message)                  #Display message if exe or python file is not called
        file.close()                        #Close the file used for storage
        sys.stdout = orig_stdout            #Change the standard out back to default value (terminal)
        file = open("text.txt")
        read = file.read()                  #Read the contents of the file
        return read

    #Function for client to send message to server
    def client(self,message = "Connection Established"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     #DGRAM is UDP (SOCK_STREAM is TCP)
        name = self.hostname
        port = int(self.port)
        self.send_message(sock,message.encode(),name,port)          #Send message to specified host


    #Function for server to receive messages from client and to forward results to client listener
    def server(self):
        name = self.hostname
        port = int(self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Again, utilizing UDP
        sock.bind((name,port))                                  #This is required to receive UDP messages from the client
        while True:
            data, addr = sock.recvfrom(4096)                    #4096 is the buffer size
            while data != None:
                print(data.decode())                            #Display the message received from client (mostly for trouble shooting)
                message = data.decode()
                message = self.message_generator(message)
                self.send_message(sock, message.encode(), addr[0], 6667)    #Send results to client listener
                data = None                                                 #End the while loop

    #Function for client to receive messages from server
    def client_server(self):
        name = self.hostname
        port = int(self.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((name,port))
        while True:
            data, addr = sock.recvfrom(4096)
            while data != None:
                print(data.decode())
                self.message_generator(data.decode())
                data = None


