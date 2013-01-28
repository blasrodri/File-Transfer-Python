import os
import socket
PORT = 8080
HOST = 'localhost'
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST,PORT))
socket.listen(1)
conn, addr = socket.accept()
print '\033[46m\033[34m\033[1mBienvenido al File Sender v.0.02 hecho en Python. Este programa permite enviar archivos a traves de tu maquina\033[0m'
ANSI_BACKGROUND = '\033[46m'
ANSI_RED = '\033[31m'
ANSI_BLUE = '\033[34m'
ESCAPEANSI = '\033[0m'
def seleccion_path():
	PATH = raw_input('\033[34m\033[1mSelect the Path (./ by default)').strip('n')
	if PATH == '':
		PATH = os.getcwd()	 
	print PATH, ESCAPEANSI
	acepta_path = raw_input('\033[34m\033[1mSi o No (S/N)').lower().strip(' ')
	if acepta_path == 's' or acepta_path == 'si':
		return PATH
	else:
		seleccion_path()
def filesDir(path):
	files = os.listdir(PATH)
	for fl in files:
		i = int(files.index(fl))+1
		print ANSI_RED + str(i)+ ')' + fl
	return files

PATH = seleccion_path()
print 'el PATH seleccionado es:', PATH + '\n'
filesDir(PATH)
fileSelected = int(raw_input(ANSI_BLUE + 'Select a file with the number').strip(' ').lower()) 
print PATH + filesDir(PATH)[fileSelected-1]

filepath = PATH + filesDir(PATH)[fileSelected-1]
#envia nombre del file
conn.send(filepath)
qLines = len(open(PATH + filesDir(PATH)[fileSelected-1], 'rb').readlines())
fileToSend = open(filepath, 'rb')
while True:
	data = fileToSend.readline()
	if data:
		conn.send(data)
	else:
		break
fileToSend.close()
conn.sendall('')
conn.close()
print '\033[43m File sent'
#Finaliza el programa y deja los codigos ANSI cerrados
print ESCAPEANSI
exit()
