from netconnect import *

if __name__ == '__main__':
    host = '0.0.0.0'
    port = 6667
    connect = NetConnect(host, port)
    connect.client_server()