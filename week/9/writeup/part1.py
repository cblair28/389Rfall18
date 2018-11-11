#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
#wordlist = open("../probable-v2-top1575.txt", 'r')
#hashes = open("../hashes", 'r')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for salt in salts:
    wordlist = open("../probable-v2-top1575.txt", 'r')
    for word in wordlist:
        w = word.rstrip()
        test = hashlib.sha512(salt + w).hexdigest()
        #print(test)
        i = 1
        hashes = open("../hashes", 'r')
        for h in hashes:
            h1 = h.rstrip()
            #print test
            #print h1
            if str(test) == str(h1):
                print(str(i) + " = " + str(salt) + str(word))
                break
            i += 1

