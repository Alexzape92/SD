import socket

PORT = 1024
HOST = "localhost"

s_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_listener.bind((HOST, PORT))

print("Waiting for connecions...")
s_listener.listen()  #Bloqueante

print("Accepting connection...")
s_for_client, addr = s_listener.accept()    #Devuelve el socket exclusivo para atender a ese cliente, y
                                            #La direccion del cliente

print("Waiting for messages...")
buffer = s_for_client.recv(1024)
print("Received message: '" + buffer.decode("utf-8") + "'")
print("from the address: " + str(addr))

s_for_client.close()
s_listener.close()

