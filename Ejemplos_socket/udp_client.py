import socket

REMOTE_PORT = 1024          #Es 1024 porque es el puerto al que nos conectamos (server)
REMOTE_HOST = 'localhost'
REMOTE_ADDR = (REMOTE_HOST, REMOTE_PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Sending the message to server in " + str(REMOTE_ADDR))
s.sendto("This is the way.".encode("utf-8"), REMOTE_ADDR)