#!/usr/bin/env python

import socket


TCP_IP = '192.168.1.136'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = b"Hello, World!"
M= []
M.append(0)
M.append(1)
bytes(M)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print (MESSAGE)
s.send(bytes(M))
data = s.recv(BUFFER_SIZE)
s.close()

print ("received data:", data)