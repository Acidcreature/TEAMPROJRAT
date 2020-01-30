from netconnect import *
if __name__ == '__main__':
    host = 'localhost'
    port = 5555
    connect = NetConnect(host, port)
    connect.server()