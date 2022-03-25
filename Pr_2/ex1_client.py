import argparse
import socket
import random



def main(host, port, n):
    REMOTE_ADDR = (host, port)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    counts_b = 0
    for i in range(0, n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        cad = '(0' + str(x) + ',' + str(y) + ')'
        print('He llegado al sendto')
        s.sendto(cad.encode("utf-8"), REMOTE_ADDR)

        buffer, addr = s.recvfrom(1024)
        buffer = buffer.decode('utf-8')

        if(buffer == 'below'):
            counts_b = counts_b + 1
    
    pi = 4 * counts_b / n
    print(pi)

    s.close()
     


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=1024, help="remote port")
    parser.add_argument('--host', default='localhost', help="remote hostname")
    parser.add_argument('--number', default=100000, help="number of random points to be generated")
    args = parser.parse_args()

    main(args.host, args.port, args.number)
