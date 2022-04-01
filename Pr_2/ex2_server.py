import argparse
from operator import truediv
import socket

def hayA(pal):
    for letter in pal:
        if(letter == 'a' or letter == 'A'):
            return True
    return False


def main(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen()
    s_for_client, addr_c = s.accept()

    cadin = ""
    buffer = s_for_client.recv(1024)
    cadin = cadin + buffer.decode('utf-8')
    
    #Contamos las palabras y eso
    cont = 0
    lista = cadin.split()   #Ahora lista tiene una lista con todas las palabras del string
    list_res = list()
    for palabra in lista:
        if(hayA(palabra)):
            cont = cont + 1
            list_res.append(palabra)
    
    msg1 = cont.to_bytes(2, 'big')
    s_for_client.send(msg1)

    for palabra in list_res:
        palabra = palabra + ' '
        s_for_client.send(palabra.encode('utf-8'))
    s_for_client.send(' '.encode('utf-8'))

    s_for_client.close()
    s.close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
