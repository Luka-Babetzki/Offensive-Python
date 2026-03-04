#!/usr/bin/python3

import socket

def banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((ip, int(port)))
        print(s.recv(1024).decode('ascii'))
    except socket.timeout:
        print(f"No banner received from {ip}:{port} — timed out.")
    except ConnectionRefusedError:
        print(f"Connection refused on {ip}:{port}.")

def main():
    ip = input("Enter the IP address: ")
    port = int(input("Enter the port: "))
    banner(ip, port)

main()
