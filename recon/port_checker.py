#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter the host to scan: ")
port = int(input("Enter the port to scan: "))

def portscanner(port):
    if s.connect_ex((host, port)):
        print("Port is closed")
    else:
        print("Port is open")

portscanner(port)