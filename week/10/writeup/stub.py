#!/usr/bin/env python2
# from the git repo
import md5py
import socket
import hashlib
import time

host = "142.93.118.186"   # IP address or URL
port = 1234   # port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data = s.recv(1024)
print(data)

#####################################
### STEP 1: Calculate forged hash ###
#####################################

s.send("1\n")
data = s.recv(1024)
print(data)

message = 'hi'    # original message here
s.send(message + "\n")
data = s.recv(1024).split()
print(data)

legit = data[7] # a legit hash of secret + message goes here, obtained from signing a message
print(legit)
# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(legit.decode('hex'))

malicious = 'malicious'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()
print(fake_hash)


#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits
length = 8

for i in range(8,18):
    pad = "\x80"
    for j in range(0,(55 - i)):
        pad = pad + '\x00'
    f = ""
    
    if (i == 8):
        f = "\x40"
    if (i == 9):
        f = "\x48"
    if (i == 10):
        f = "\x50"
    if (i == 11):
        f = "\x58"
    if (i == 12):
        f = "\x60"
    if (i == 13):
        f = "\x68"
    if (i == 14):
        f = "\x70"
    if (i == 15):
        f = "\x78"
    if (i == 16):
        f = "\x80"
    if (i == 17):
        f = "\x88"
    
    pad = pad + f
    pad = pad + "\x00\x00\x00\x00\x00\x00\x00"
    s.send("2\n")
    s.recv(1024)
    s.send(fake_hash + "\n")
    s.send(message + pad + malicious + "\n")
    data = s.recv(1024)
    print(data)


padding = ''

# payload is the message that corresponds to the hash in `fake_hash`
# server will calculate md5(secret + payload)
#                     = md5(secret + message + padding + malicious)
#                     = fake_hash
payload = message + padding + malicious

# send `fake_hash` and `payload` to server (manually or with sockets)
# REMEMBER: every time you sign new data, you will regenerate a new secret!
