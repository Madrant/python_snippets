#!/usr/bin/python3
#
# UDP recv example
#
# use 'nc -u 127.0.0.1 31337' to send data

import socket

ip = "0.0.0.0"
port = 31337

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Listen on %s: %u" % (ip, port))
sock.bind((ip, port))

while True:
    data, addr = sock.recvfrom(64)
    print("Received: %s" % data)
