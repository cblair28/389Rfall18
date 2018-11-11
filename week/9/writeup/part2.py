#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib
import time

host = "142.93.117.193"   # IP address or URL
port = 7331   # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data = s.recv(1024)
print(data)
x = data.split()
#print(x[12])
h = hashlib.new(x[12], string=x[15])
#print(h.hexdigest())
s.send(h.hexdigest())
s.send("\n")

while 1:
    data = s.recv(1024)
    print(data)
    x = data.split()
    if x[3] == "You":
        break
    #print(x[12])
    h = hashlib.new(x[4], string=x[7])
    #print(h.hexdigest())
    s.send(h.hexdigest())
    s.send("\n")


# close the connection
s.close()
