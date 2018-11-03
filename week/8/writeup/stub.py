#!/usr/bin/env python2

import sys
import struct
import pylint
import binascii

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!
# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

timestamp, = struct.unpack("<L", data[8:12])

author, = struct.unpack("<8s", data[12:20])

sectioncount, = struct.unpack("<L", data[20:24])

index = 24

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))


if int(sectioncount) <= 0:
    bork("Bad section count! Less than or equal to zero!")


print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: %d" % int(timestamp))
print("AUTHOR: %s" % str(author))
print("SECTIONCOUNT: %d" % int(sectioncount))


print("-------  BODY  -------")

for i in range(0, sectioncount + 1):
    stype, slen = struct.unpack("<LL", data[index: index + 8])
    #stype, = struct.unpack("<L", data[index: index + 4])
    index += 8
    print i
    print slen
    print("SECTIONTYPE: %d" % int(stype))

    if slen != 0:
        if stype == 0x1:
           # png, = struct.unpack("<" + str(slen) + "s", data[index: index + slen])
           # magic = 0x89504e470d0a1a0a
           # iend = 0x73697868
            #f = open("ping.png", "wb")
           # f.write(magic)
           # f.write(png)
           # f.write(iend)
           # f.close
            index = index + slen
        
        elif stype == 0x2:
            wordnum = slen/8
            words = [0] * wordnum
            for j in range(0, wordnum):
                words[j], = (struct.unpack("<d", data[index: index + 8]))
                index += 8
            print words

        elif stype == 0x3:
            print "utf"


        elif stype == 0x4:
            print "dubs"

        elif stype == 0x5:
            print slen
            wordnum = slen/4
            print wordnum
            print index
            words = [0] * wordnum
            for j in range(0, wordnum):
                words[j], = struct.unpack("<L", data[index: index + 4])
                index = index + 4
            print words

        elif stype == 0x6:
            lon, lat = struct.unpack("<dd", data[index: index + 16])
            print("LONGITUTE: %d" % lon)
            print("LATITUDE: %d" % lat)
            index = index + 16

        elif stype == 0x7:
            ref, = struct.unpack("<L", data[index: index + 4])
            print("REF: %d" % ref)
            index = index + 4

        elif stype == 0x9:
            asciitxt = struct.unpack("<" + str(slen) + "s", data[index:index + slen])
            index = index + slen
            print("ASCII: %s" % str(asciitxt))

        else:
            bork("Incorrect section %s" % str(stype))