import argparse
import socket
from os.path import exists

def recibir_mensaje(socket):
    terminar = 2
    mensaje = ""
    while terminar > 0:
        recibido = socket.recv(1).decode('utf-8')
        mensaje += recibido
        if (recibido == " "): terminar -= 1
        else: terminar = 2

    return mensaje

def main(host, port, filein, fileout):
    REMOTE_ADDR = (host, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if(not exists(filein)):
        raise OSError

    file = open(filein, 'r')
    text = file.read()
    
    s.connect(REMOTE_ADDR)
    s.sendall(text.encode('utf-8'))

    #Guardamos en palsa el numero de palabras que contienen la A
    buffer = s.recv(2)
    palsa = int.from_bytes(buffer, 'big')

    #guardamos en mensaje la cadena con las palabras, separadas con espacios, y lo convertimos en lista
    mensaje = recibir_mensaje(s)
    lista = mensaje.split()

    file.close()

    if(not exists(fileout)):
        raise OSError
    
    file = open(fileout, 'w', newline='\n')
    for pal in lista:
        file.write(pal)
        file.write('\n')
    
    file.close()
    s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--filein', default='filein.txt', help="file to be read")
    parser.add_argument('--fileout', default='fileout.txt', help="file to be written")
    args = parser.parse_args()

    main(args.host, args.port, args.filein, args.fileout)
