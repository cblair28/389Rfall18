Writeup 9 - Crypto I
=====

Name: Corbett Blair
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Corbett Blair

## Assignment 9 Writeup

### Part 1 (60 Pts)
Part 1 started off simply enough. I started by opening the password and hash files. I knew I had to do a nested for loop and try every combination of salt + password. Building off the stub I was given, I iterated first through the salts and then through the list of passwords. Getting hashlib to work was simple enough as the docs were very intuitive. I started out with some print statements within my loops to make sure everything was working correctly and hit my first road block. I was only iterating through the password list for my "a" salt, but apparently the password file iteration does not start from the top for subsequent loops. To solve this I reopened both the password file and the hash file at the beginning of each loop. I set a single print statement inside my innermost loop where I check the salt + password hash against the given hashes, where it would print out the salt and password if the hashes matched. However, nothing would match. I would be stuck at this roadblock for a couple hours and actually complete part 2 before having an epiphany - the hexdigest function returns a hex number and the read function probably reads the file as a string. After printing out some of the data, I noticed another problem - each hash has a newline character appended to it! I changed both hashes to strings using the str() method, then stripped them using .rstrip(), and voila, I found out the salts and passwords. They are:

Hash 1: Salt = k Password = neptune
Hash 2: Salt = p Password = pizza
Hash 3: Salt = u Password = loveyou
Hash 4: Salt = m Password = jordan



### Part 2 (40 Pts)

I started part 2 by manually connecting to the server and seeing what I would have to do. Using another program to compute the hashes I was asked, I answered a few of the questions by hand and got a handle on the prompts. After week 4's assignment, I was comfortable connecting to a port via a socket in python, so the setup of the program wasn't too hard. I recieved the data and split it into an array using the split() function. I noticed the two things I needed to parse from the data were the type of hash and the value to be hashed. These were in the same place each time, so I could easily isolate them by accessing part of my array. I tried using the hash.new function and substituting in the values that I read for the data, and to my surprise there were no errors. However, I still wasn't getting the "correct!" prompt. After some time thinking, just like part 1, it was the newlines that got me. I forgot to send a newline after sending the hash. After I did that, my program began to work. Because the very first data recieved has the "Welcome" header, the array indices I needed to access were different than the rest of the data. So, I had an initial round that dealt with the header, and then dropped into an infinite loop for the subsequent prompts and broke when I recieved the "You win!" message. 

FLAG: CMSC389R-{H4sh-5l!ngInG-h@sH3r}
