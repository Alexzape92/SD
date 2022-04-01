import argparse
import math
import socket
from xml.dom.minidom import CharacterData


def main(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    
    buffer, addr = s.recvfrom(1024)
    buffer = buffer.decode('utf-8')
    while buffer != 'exit':
        x, y = sacarTupla(buffer)
        if x < 0 or x > 1 or y < 0 or y > 1:
            s.sendto('error'.encode('utf-8'), addr)
        if y < f(x):
            s.sendto('below'.encode('utf-8'), addr)
        if y >= f(x):
            s.sendto('above'.encode('utf-8'), addr)
        buffer, addr = s.recvfrom(1024)
        buffer = buffer.decode('utf-8')
    
    s.close()


def sacarTupla(cad):
    i = 1
    substrx = ''
    while cad[i] != ',':
        substrx = substrx + str(cad[i])
        i = i + 1
    x = float(substrx)

    i = i + 1
    substry = ''
    while cad[i] != ')':
        substry = substry + str(cad[i])
        i = i + 1
    y = float(substry)

    return (x, y)

def f(x):
    return math.sqrt(1 - math.pow(x, 2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
