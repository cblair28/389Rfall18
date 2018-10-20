Writeup 7 - Forensics I
======

Name: Corbett Blair
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 7 writeup

### Part 1 (40 pts)

1. image/JPEG file

2. Chicago, Illinois - The John Hancock Center

3. 11:33:24 on 8/22/2018

4. iPhone 8 back camera 3.99mm f/1.8

5. 539.5 m Above Sea Level

6. CMSC389R-{look_I_f0und_a_str1ng}

### Part 2 (55 pts)

flag: CMSC389R-{dropping_files_is_fun}

To get this flag, first I took a look at the binary file. I tried binwalk and exiftool on it, to no luck. Eventaully I downloaded cutter, as seen in class, and took a look at the file in there. I saw the location /tmp/.stego, so I decided to check in there. I was unable to find anything, so I went back, and learned in office hours you could compile the file by chmod command and changing permissions. After I did and ran that, "Where is your flag?" popped out, and I knew I was on the right track. .stego was now in my directory, but I had to figure out what to do with it. After a good while of calling strings and binwalk and file and exiftool, I realized (with help from piazza) it was almost a jpeg file, but there was something wrong with the magic bytes. I searched the internet and found the problem: There was an extra byte at the beginning. After removing that, I was able to open the file, and it was a picture of a stegosaurus. Now, I thought I could finally use steghide on it, but there was another extra byte at the end. After removing that I could use steghide. After trying stegosaurus as the password, I was able to find the flag.
