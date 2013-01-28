import os
import socket
PORT = 8080
HOST = 'localhost'
ANSI_BACKGROUND = '\033[44m'
ANSI_RED = '\033[31m'
ANSI_BLUE = '\033[34m'
ESCAPEANSI = '\033[0m'
print ANSI_BLUE + 'Welcome to the Data Transfer application'
nombrearchivo = raw_input('define a name with its extension').strip(' ')
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
filename = socket.recv(1024)
#fname = open('./asd.pdf', 'wb')
fname = open('./'+nombrearchivo, 'wb')

while True:
	strng = socket.recv(1024)
	if strng:
		fname.write(strng)
	else:
		fname.close()
		break
socket.close()
print ESCAPEANSI
print ANSI_BACKGROUND + ANSI_RED + 'Data received correctly'	
print ESCAPANSI
exit()
