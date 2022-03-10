import socket

REMOTE_PORT = 1024
REMOTE_HOST = 'localhost'
REMOTE_ADDR = (REMOTE_HOST, REMOTE_PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connecting to..." + str(REMOTE_ADDR))
s.connect(REMOTE_ADDR)

print("Sending a message...")
s.sendall("This is the way.".encode("utf-8")) #El sendall hace automáticamente el bucle por si el mensaje
                                              #Fuera muy grande

s.close()