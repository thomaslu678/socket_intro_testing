#adf

import socket
import sys

def connect_to_google():
    ip = socket.gethostbyname('www.google.com')
    #terminal gets different last 2 decimals
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
    # default port for socket
    port = 80
    try:
        host_ip = socket.gethostbyname('www.google.com')
    except socket.gaierror:

        # this means could not resolve the host
        print("there was an error resolving the host")
        sys.exit()
    # connecting to the server
    s.connect((host_ip, port))
    print("the socket has successfully connected to google")

def create_server():
    global s
    # next create a socket object
    s = socket.socket()
    print("Socket successfully created")
    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 12345
    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))
    print("socket binded to %s" % (port))
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")
    # a forever loop until we interrupt it or
    # an error occurs
    while True:
        # Establish connection with client.
        c, addr = s.accept()
        print('Got connection from', addr)

        # send a thank you message to the client. encoding to send byte type.
        c.send('Thank you for connecting'.encode())

        # Close the connection with the client
        c.close()

        # Breaking once connection closed
        break

create_server()