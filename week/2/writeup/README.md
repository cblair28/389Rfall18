Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Corbett Blair
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Corbett Blair

## Assignment 2 writeup

### Part 1 (45 pts)

1.  Fred Krueger

2.  Twitter: @Kruegster1990
    Reddit: u/Kruegster1990
    (Found these two by simply googling)
    Website: www.cornerstoneairlines.co (In twitter bio)
    Email: kruegster@tutanota.com (About page of conerstoneairlines)
    Instagram: kruegster1990 (I searched kruegster1990 on checkusernames.com and saw that
    there was an instagram account associated with it)
    On his instagram account, there was a photo of a boarding pass for a flight
    from BWI to SFO on 9/12/2018. From his instagram and twitter (where he posted a pokemon go article), Fred is a confirmed pokemon fan. Also one time Josh said "fuck off" to him on a picture of ivysaur

3.  IP: 142.93.118.186. I searched Domain Dossier on cornerstoneairlines.co and found this address. A little further down the page, it says that it belongs to Digital Oceans cloud service.

4. Cornerstoneairlines.co/robots.txt points to the url cornerstoneairlines.co/secret, where
I found a flag by examining the source, which I documented below.

5. I found the IP address 142.93.117.193, which corresponds to the admin page of cornerstoneairlines.co. This is what I used to log into the admin port.

6. By running a domain dossier on cornerstoneairlines.co I found that the webserver, Digital Oceans, is located at 101 Ave of the Americas, NY, NY.

7. By clicking the "service scan" button on domain dossier and scrolling down to the infobox, I determined that the server is running on Ubuntu.

8. *(BONUS)*
Flag 1: CMSC389R-{fly_th3_sk1es_w1th_u5} (Found "/secret" listed
on robots.txt. Went to cornerstoneairlines.co/secret and examined the source)
Flag 2: CMSC389R-{h1dden_fl4g_in_s0urce} (Examined source of cornerstoneairlines.co)
Flag 3: CMSC389R-{dns-txt-rec0rd-ftw} (Examined the DNS txt records of cornerstoneairlines.co on Domain Dossier)
Flag 4: CMSC389R-{c0rn3rstone-air-27670} (Accessed the admin port by guessing username/password combo via OSINT clues, as described below in part 2. Then, I used the boarding pass that I found on Fred's instagram to locate the text file that corresponded with the number on the pass.)


### Part 2 (55 pts)

First, I had to nmap the URL/IP to find open ports. I tried for a while looking into the
cornerstoneairlines.co url, but to no avail. I then tried the IP address found on the admin page, and ran an nmap on that. At first no notable ports showed up, so I added the -p- flag to scan all possible ports, and found port 1337, which when I try to nc into, I get a username and password prompt.

I tried to use the python brute force script but I couldn't quite get it to work. It would try username/password combinations but the pipe would eventually breakafter 600-800 tries. I've submitted my commented code so you can see my logic. Maybe I wasn't getting the syntax quite right. Eventually, I tried to crack it by hand. I guessed that "kruegster" would be the username because that's Fred's work email username listed on cornerstoneairlines.co. I suspected the password had something to do with Pokemon, because he shared a pokemon go link on twitter and also his instagram was filled with pokemon pictures. I searched the rockyou.txt file for any passwords including "pokemon" and found a 2 or 3 in the first few thousand entries. I tried those, and it was "pokemon" that was the password. After gaining access I navigated to the flight_record directory and opened up the text file that corresponded with the number on the boarding pass posted to Fred's instagram. Inside, I found the flag, which is CMSC389R-{c0rn3rstone-air-27670}.
