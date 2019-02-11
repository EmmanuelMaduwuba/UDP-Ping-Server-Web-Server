from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
#getting user input 
host = input('Input host:')
port = input('Input port:')
filename = input('Input filename:')
#TCP handshake
clientSocket.connect((host,int(port)))
message = 'GET /' + filename + " HTTP/1.1\nHost: " + host +":" + port
clientSocket.send(message.encode()) 
#listening for response
while True:
    response = clientSocket.recv(1024)
    if len(response) == 0:
        break
        end = ''
    print(response.decode(), end )
#closing socket connection
clientSocket.close()