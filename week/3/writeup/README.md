Writeup 3 - OSINT II, OpSec and RE
======

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Corbett Blair

## Assignment 3 Writeup

### Part 1 (100 pts)

Vulnerability 1: Open ports
Why it's a problem: Fred's open port is the reason the 389R attackers were able to hack into his website. By using nscan on the IP address of his website, attackers were able to see all the available open ports, try to connect to them, and eventually encounter a username/password prompt. This was their sign to attack. 
How to fix: After doing some research, it seemed like a firewall would be a good counter to open ports. Because firewalls can monitor/control incoming and outgoing information, Fred should be able to use one to block outside users from trying to enter his ports. There is also the simple solution of being aware of which ports are open, and close them when the are not needed. Either of these would have probably stopped the hackers.

Vulnerability 2: No nscan awareness
Why it's a problem: In class, it was stated that nscanning is noisy, and whoever you are scanning will be able to tell somebody is poking around. It did not appear Fred knew this. This is important because it was how the attackers found the open port in the first place - if Fred had more awareness that somebody is potentially looking for vulnerabilities in his site, he could take better precautions, double check for possible points of weakness, and discover that he is under attack before it's too late.
How to fix: I did some researching for Fred, and it appears the easiest way to keep an eye on your ports being scanned is to download software to do it for you. One that I found for him was called the ExtraHop Scan Detection Bundle, which even notifies you when somebody is doing a very slow scan to try to avoid detection. 

Vulnerability 3: Predictable password/Oversharing on social media
Why it's a problem: These kind of go hand in hand. Fred's instagram was crucial to the cracking of his password and the finding of the flag. It's incredibly careless to not only have a password as weak as "pokemon" but also plaster your social media with pictures of your password. In addition, he had a picture of his boarding pass, which I was able to use to locate a folder with valuable information in it.
How to fix: This is mostly an awareness thing for Fred. He needs to be more mindful of what he posts on social media. There are plenty of ways to choose better passwords. He could use a password generator such as www.lastpass.com/passwordgenerator, and then use a password manager such as KeePass to keep his password(s) safe. In addition to that, he just needs to double check every time he posts something to social media, and ask himself: Will any of this put me at risk?