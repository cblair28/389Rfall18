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
(or just "; cat home/flag.txt")

My thought process:
For a good while, I didn't see the part where it said "It is vulnerable to command injection",and began trying to crack it like the heartbleed bug. I did research on it and ping commands, and begin trying to request bytes to read past the buffer and potentially return the flag. I begin playing with the -l and -f tags after pinging 142.93.117.193, and although the bytes returned would differ, none of them returned the flag. So, I read the README closer and discovered what I was actually supposed to do. 

I first had to do a little research with command injection. I suspected that it would run ping "______" on whatever input we typed in. So, I thought that by adding a semicolon, I could trick it into executing what came after as a command. I tried 142.93.117.193; ls, and saw the contents of the directory. I remembered in class we were told often things are stored in the home directory. After calling dir home, I saw the file flag.txt, and then it was just a matter of examining it. I found shortler after I didn't have to start with the IP address - starting with ; was sufficient.

What can Fred do to protect against this:
Command injection works because user input is treated as code. A solution around this is to sanitize input. In class we talked about whitelisting and blacklisting. In this case, the unescaped semicolon is what allowed me to trick the server into running malicious code. The first thing Fred can do is whitelist input by sanitizing special characters, replacing ";" with "\;" and so on. Other characters he might want to watch out for would include ".", "/", "'", and so on. This would have at least prevented my specific attack. Fred might also be able to use a prepared statement. I remember this is a way to protect against sql injection. It would treat the user input as a variable, not a direct string, and ensure that nothing in it could be mistaken for code to execute.

### Part 2 (55 pts)
For part 2 I knew I hads to write a program that repeats what I did for part one as many times as the user wants. Looking at the nature of the server, I realized that between every command, the socket connection would have to be reestablished, because it exits after one input. So, I decided to write a program with an infinite loop. At each iteration of the loop, it would get user input, and ideally call the function execute_cmd. In the execute_cmd function, the first thing I did was establish a socket connection. Then, I would recieve data, which would be the prompt screen, before inputting my command. I concatenated a ";" to the beginning of the command and a "\n" to the end to make sure it would be registered correctly. The program would then read the output and print it. So, for example, if the user input "ls", execuse_cmd would be called, the connection will be established, the prompt will be recived, "; ls \n" would be entered, and the response would be printed.

Note that on piazza it said allow 2 seconds between recieving and sending the command. For some reason, I had to wait 4 seconds, as well as 2 seconds before and after the first recieve call, otherwise it would occasionally recieve and print the "CORNERSTONE AIRLINES" screen. Which, although it still worked, I wanted to get rid of. So I apologize for the runtime.

Next, I had to deal with the fact that the connection was reset after every command. This would render all "cd" calls useless. The way I combatted this was whenever a "cd" call was made, I stored it in a variable. Then, on every subsequent call, I added the variable to the beginning of the command. So, if the user input "cd home", and then "ls", the command sent would look like: "; cd home; ls \n".

Next, I had to make sure this only happened after the user typed "shell". I did this by adding another infinite input loop outside of this one, and dropping into the loop detailed above on the "shell" command. "Help" and "quit" were easy to implement - for Help, I just saved the menu into a text file, then printed the contents. I also printed the contents if the command was unrecognized. Finally, I had to implement "pull".

I decided that the easiest way to do this was to create an "if" statement in the execute_cmd function, and "pull" would have its own set of instructions. The user would call "pull file1 file2". I would call execute_cmd, call "; cat file1\n", then save the output to a variable. I would then write that variable to file2.

After all that, I finally had a shell that worked according to the given specs.