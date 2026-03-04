#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(socket.gethostname())
port = 444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print(f"Connection from {address} has been established.")
    message = "Hello! Welcome to the server!"
    clientsocket.send(message.encode('ascii'))
    clientsocket.close()
