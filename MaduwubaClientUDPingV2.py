from socket import *
import time
serverName = '192.168.2.78'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(10.0);   #setting timeout of socket
count = 0
message = 0

while(count < 10):
    count += 1
    message = str((time.time() ) / 1000)
    message = message.encode('utf-8')
    clientSocket.sendto(message,(serverName, serverPort))   #sending of the message
    time.sleep(5)
