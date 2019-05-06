from socket import *
import time
serverName = '192.168.2.78' #you can put your Machine's  IP address here 
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) 
clientSocket.settimeout(2.0);   #setting timeout of socket
message = input('Input lowercase sentence:')   #getting user input for the message
message = message.encode('utf-8')
#making a counting variable ,min and max variable
count = 0; min = 0; max = 0; startTime = 0; 
#sending 10 ping messages
while (count < 10):
 	clientSocket.sendto(message,(serverName, serverPort))   #sending of the message
 	count = count + 1
 	startTime = time.time()
 	try:
 		modifiedMessage,serverAddress = clientSocket.recvfrom(2048) #listening for the message
 	except timeout:
 		print("Request timed out")
 	elapsedTime = time.time() - startTime
 	elapsedTime = elapsedTime / 1000
 	if(elapsedTime < clientSocket.gettimeout()):
  		print( str(modifiedMessage)+ str(count) + " Round Trip Time: " + str(elapsedTime) + " ms")
		
clientSocket.close()
