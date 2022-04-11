import argparse
import socket

def resulTurno(coords, tablero):
    i = 0
    if len(coords) == 3:
        i = 9 * 21
    else:
        i = (ord(coords[1]) - 49) * 21
    
    col = ord(coords[0]) - 65
    i = i + col*2
    res = (tablero[i] == '1')
    newtablero = tablero[:i] + '0' + tablero[i+1:]    #Si era agua, lo dejamos igual, si era un navío, marcamos que ahora es agua (Ya le hemos dado)

    return res, newtablero  #Devuelve TRUE si ha acertado, FALSE si no

def Victoria(tablero):
    return ("1" not in tablero)

def main(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    buffer, addr1 = s.recvfrom(512)   #Obtenemos el nombre del jugador 1
    Nombre1 = buffer.decode('utf-8')

    buffer, addr1 = s.recvfrom(512)   #Obtenemos la matriz del jugador 1
    Tab1 = buffer.decode('utf-8')

    buffer, addr2 = s.recvfrom(512)   #Obtenemos el nombre del jugador 2
    Nombre2 = buffer.decode('utf-8')

    buffer, addr2 = s.recvfrom(512)   #Obtenemos la matriz del jugador 2
    Tab2 = buffer.decode('utf-8')

    terminado = False
    turno = 1
    jug = 1
    while(not terminado):
        if(jug == 1):
            s.sendto(('Turn ' + str(turno)).encode('utf-8'), addr1)
            buffer, addr1 = s.recvfrom(512)
            coords = buffer.decode('utf-8') 
            
            result, Tab2 = resulTurno(coords, Tab2)
            if not result:
                s.sendto('Fail'.encode('utf-8'), addr1)
                jug = 2
            else:
                if not Victoria(Tab2):
                    s.sendto('Hit'.encode('utf-8'), addr1)
                else:
                    s.sendto('You win'.encode('utf-8'), addr1)
                    s.sendto('You lost'.encode('utf-8'), addr2)
                    terminado = True
        else:
            s.sendto(('Turn ' + str(turno)).encode('utf-8'), addr2)
            buffer, addr2 = s.recvfrom(512)
            coords = buffer.decode('utf-8') 

            result, Tab1 = resulTurno(coords, Tab1)
            if not result:
                s.sendto('Fail'.encode('utf-8'), addr2)
                jug = 1
            else:
                if not Victoria(Tab1):
                    s.sendto('Hit'.encode('utf-8'), addr2)
                else:
                    s.sendto('You win'.encode('utf-8'), addr2)
                    s.sendto('You lost'.encode('utf-8'), addr1)
                    terminado = True
        turno = turno+1

    s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="listening port")
    parser.add_argument('--host', default='localhost', help="hostname")
    args = parser.parse_args()

    main(args.host, args.port)
