Writeup 10 - Crypto II
=====

Name: Corbett Blair
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Corbett Blair

## Assignment 10 Writeup

### Part 1 (70 Pts)

The bolded letters in "Such a Quick Little" tipped me off that this is would be related to SQL. After perusing the site, the only place I could see that I could possibly inject is the URL. I tried to click around a bit, and it seemed that the different items we could purchase were kept in a database, and there was probably something else in the database we wanted to see. So, if I said get items where id=0 OR '1'='1', or something similar, I should be able to see everything in the database. I tried that, but nothing seemed to be working. However, after revisiting the slides, I saw that there might be a firewall that was sanitizing my input. I changed the OR to || and the '1' to 'hey' and it worked. The full URL I typed in was:

http://cornerstoneairlines.co:8080/item?id=1' || 'hey'='hey

CMSC389R-{y0U-are_the_5ql_n1nja}


### Part 2 (30 Pts)

Level 1: Answer = <script>alert("alert")</script>

This level was simple enough. Here, the browser sees the script tags and treats the text in between as code. All I had to do was make it an alert.



Level 2: Answer: <img src=”” onerror=’alert(“hey”)’/>

This level was very difficult because I was not very familiar with the img tag or Javascript. I initially tried to just use the same commands from level 1, but it didn’t work. After looking at all the hints, I decided to try to play with the “onerror” tag in an img format and give a nonexistent source. I tried to make the onerror tag the answer to level 1, but it didn’t work. I had to look up how else you could write javascript, and learned that you can also type alert().



Level 3: Change the url to: https://xss-game.appspot.com/level3/frame#1' onerror='alert("hey")'>


Starting this level out and looking at the code, I see the only place where input is read is through the image number in the URL.  If we could add a quotation mark of some sort to trick the code into thinking it is no longer reading input, maybe we can sneak an alert in there. I tried around with a few things and eventually learned that you can just use the same “onerror” command as in part 2. This works because the ‘ after the one cuts off the .jpg file, so the source is invalidated, and it errors.


Level 4: enter into timer box: 3'),alert('hello


It was easy to see in this level where I should focus because there is only one place that accepts user input. My original plan was to again use ‘ to trick the code into thinking my input was finished, and then injecting code in after. I was able to finish the time by typing 3’) and then injecting my alert code. It took me very long to figure out how to separate the ) and the “alert(‘hello” which ended without a quotation mark because the alert argument would be finished with a ‘ in the code. I tried a semicolon and the HTML encoding of a semicolon, which 


Level 5: URL = https://xss-game.appspot.com/level5/frame/signup?next=alert('hey')


After looking at the source code, it seemed like I could inject code into the “next” tag in the URL and have it execute. This was easy enough – I simply changed the next tag to “alert(‘hey’)” and it worked.


Level 6: https://xss-game.appspot.com/level6/frame#//google.com/jsapi?callback=alert


Level 6 was tricky until I read the final hint. I was confused about the external file line, and I spent a while pondering whether or not I had to make my own file somehow. However, they give you a file in the last hint that you can place in, if you replace the foo with alert. The code showed that whatever appeared after the # was appended to the file name. So, simply inserting the given text after the # worked.

