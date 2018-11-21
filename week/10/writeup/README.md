Writeup 10 - Crypto II
=====

Name: Corbett Blair
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Corbett Blair

## Assignment 10 Writeup

### Part 1 (70 Pts)

Flag : CMSC389R-{i_still_put_the_M_between_the_DV}

My first order of business was to really understand how the length extension attacks worked. I realized the hard part was figuring out the padding used during the original secret+message hashing that the server does. This was made difficult by the secret being different lengths each time. My approach was this: Hash the message "hi", which is two bytes long. Since we know the secret is between 6 and 15 bytes, the secret + message would be between 8 and 17. Then, loop from 8 to 17, trying out the custom padding for each, and see if one is correct. I used the word "malicious" as my malicious message. So, I wanted the real hash of (secret + message + padding + malicious) to equal the fake hash of "malicious".

I was trying to avoid using sockets for this if I could, but seeing as the setup was continuously communicating and recieving data from a server, I eventually decided sockets would be the easiest way. After playing with the server and configuring my sockets correctly, I had to figure out how to determine the padding. I would start assuming the secret was 6 bytes, then add the correct padding as documented on the slides. Then I would try the same but increment the secret size. It seemed to be working correctly but took me an entire day to figure out I was adding the wrong number of null bytes to the end. Once I fixed that, I was able to retrieve the flag.


### Part 2 (30 Pts)

The commands you would use for this are:
gpg --gen-key
gpg --import pgpassignment.key
gpg -e -u "Corbett Blair" -r "UMD Cybersecurity Club <president@csec.umiacs.umd.edu>" message.private

This generates message.private.gpg, the encrypted message.

For the majority of this part of the assignment, the slides were an efficient guide. I first generated my own private key, then imported the public key that was given to me. I wasn't too sure what I should put as the recipient name until I opened the pgpassignment.key file and saw the username listed. After that, I put a message in message.private and encrypted it. I did this again using my own public key and was able to successfully decrypt, so I am hoping it works smoothly on your end.