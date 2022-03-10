import socket

#Solo podemos coger puertos mayores a 1024
PORT = 1024
HOST = "localhost"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

buffer, addr = s.recvfrom(1024)     #addr será una tupla (ip, puerto).
                                    #El receive será bloqueante, se quedará parado hasta que reciva un mensaje
                                    #Cada receive recibe un mensaje, si mandamos mas de 1, tenemos que hacer más
print("Received message: '" + buffer.decode("utf-8") + "'")
print("From address: '" + str(addr) + "'")

s.close()