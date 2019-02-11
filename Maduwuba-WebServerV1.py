from socket import *
import sys 
import threading
from multiprocessing import connection
#Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('192.168.2.78', 11000))
serverSocket.listen(7)
# this array will hold threads
threads = []  
print ('Ready to receive...')  
#function for threading
def TCPThread(connectionSocket,addr):
    try:                                                 
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])                                                  
        outputdata = f.read() 
        #Send one HTTP header line into socket                                                      
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode('utf-8')) 
        connectionSocket.send("Content-Type: text/html \r\n\r\n".encode('utf-8'))   
        connectionSocket.send(outputdata.encode('utf-8'))
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 Not Found'.encode('utf-8'))
        #Close client socket
        connectionSocket.close()
    return 
try:
    while True:
        connectionSocket, addr = serverSocket.accept()    
        #creating the thread                      
        thread_ = threading.Thread(target=TCPThread, args=(connectionSocket,addr))
        #adding a thread to array
        threads.append(thread_)
        #start
        thread_.start()                                                                                                      
        print(str(len(threads)) + " Thread(s)")
finally:
    serverSocket.close()
    sys.exit()#Terminate the program after sending the corresponding data
