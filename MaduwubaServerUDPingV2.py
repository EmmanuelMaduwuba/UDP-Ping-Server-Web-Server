# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
import random
import time
from socket import  *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('192.168.2.78', 12000))

count = 1 
while True:
    # Receive the client packet along with the address it is coming from
    try:
        message, address = serverSocket.recvfrom(1024)
        timeleft = message.decode('utf-8')
        timeleft = float(timeleft)
        # Calculating time difference
        timeDiff = (time.time() / 1000) - timeleft;
        print("Time Difference of packet number " + str(count)+ " : " + str(timeDiff) + " ms")
        count += 1
    except timeout:
        print("Client's host is down")