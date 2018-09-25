Writeup 3 - Pentesting I
======

Name: Corbett Blair
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Corbett Blair

## Assignment 4 Writeup

### Part 1 (45 pts)
The flag I found was CMSC389R-{p1ng_as_a_$erv1c3}.

The input I used to obtain the flag was:
nc cornerstoneairlines.co 45
142.93.117.193; cat home/flag.txt

My thought process:
For a good while, I didn't see the part where it said "It is vulnerable to command injection",and began trying to crack it like the heartbleed bug. I did research on it and ping commands, and begin trying to request bytes to read past the buffer and potentially return the flag. I begin playing with the -l and -f tags after pinging 142.93.117.193, and although the bytes returned would differ, none of them returned the flag. So, I read the README closer and discovered what I was actually supposed to do. 

I first had to do a little research with command injection. I suspected that it would run ping "______" on whatever input we typed in. So, I thought that by adding a semicolon, I could trick it into executing what came after as a command. I tried 142.93.117.193; ls, and saw the contents of the directory. I remembered in class we were told often things are stored in the home directory. After calling dir home, I saw the file flag.txt, and then it was just a matter of examining it.

What can Fred do to protect against this:
Command injection works because user input is treated as code. A solution around this is to sanitize input. In class we talked about whitelisting and blacklisting. In this case, the unescaped semicolon is what allowed me to trick the server into running malicious code. The first thing Fred can do is whitelist input by sanitizing special characters, replacing ";" with "\;" and so on. Other characters he might want to watch out for would include ".", "/", "'", and so on. This would have at least prevented my specific attack. Fred might also be able to use a prepared statement. I remember this is a way to protect against sql injection. It would treat the user input as a variable, not a direct string, and ensure that nothing in it could be mistaken for code to execute.

### Part 2 (55 pts)
*Put your writeup >= 200 words here in response to part 2 prompt. Your code for part 2 should be copied into a file in the /writeup directory and pushed there as well*
