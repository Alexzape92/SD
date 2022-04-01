import argparse
import socket
from os.path import exists

def main(host, port, filein, fileout):
    REMOTE_ADDR = (host, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if(not exists(filein)):
        raise OSError
    file = open(filein, 'r')
    text = file.read()
    
    s.connect(REMOTE_ADDR)
    s.sendall(text.encode('utf-8'))

    buffer = s.recv(1024)
    palsa = int.from_bytes(buffer, 'big')
    print(palsa)

    buffer = s.recv(1024)
    pala = buffer.decode('utf-8')
    print(pala)
    
    lista = pala.split()
    print(lista)

    s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--filein', default='filein.txt', help="file to be read")
    parser.add_argument('--fileout', default='fileout.txt', help="file to be written")
    args = parser.parse_args()

    main(args.host, args.port, args.filein, args.fileout)
