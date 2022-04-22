import json

from bottle import route, run, template

#Guardamos las listas del JSON en el ámbito global, para tenerlas siempre disponibles
salas = list()
reservas = list()
users = list()

#Definimos las clases a usar
class Sala:
    def __init__(self, idSala, capacidad, recursos):    #Recursos es una lista de strings
        self.idSala = idSala
        self.capacidad = capacidad
        self.recursos = recursos
    
    def __str__(self):
        return "idSala = {}, Capacidad = {}, recursos = {}".format(self.idSala, self.capacidad, self.recursos)
    def __repr__(self):
        return "idSala = {}, Capacidad = {}, recursos = {}".format(self.idSala, self.capacidad, self.recursos)

class Reserva:
    def __init__(self, idReserva, DNI, fecha, ini, fin):
        self.idReserva = idReserva
        self.DNI = DNI
        self.fecha = fecha
        self.ini = ini
        self.fin = fin
    def __str__(self):
        return "idReserva = % s, DNI = % s, fecha = % s, HoraInicio = % s, HoraFin = % s" % \
        (self.idReserva, self.DNI, self.fecha, self.ini, self.fin)
    def __repr__(self):
        return "idReserva = % s, DNI = % s, fecha = % s, HoraInicio = % s, HoraFin = % s" % \
        (self.idReserva, self.DNI, self.fecha, self.ini, self.fin)

class Usuario:
    def __init__(self, DNI, nick, passwd):
        self.DNI = DNI
        self.nick = nick
        self.passwd = passwd
    def __str__(self):
        return "DNI = % s, Username = % s, Password = % s" % (self.DNI, self.nick, self.passwd)
    def __repr__(self):
        return "DNI = % s, Username = % s, Password = % s" % (self.DNI, self.nick, self.passwd)

def jsonparser():
    file_name = "DB.json"
    with open(file_name) as f:
        data = json.load(f)
    
    lista_salas = data["Salas"]
    lista_reservas = data["Reservas"]
    lista_users = data["Usuarios"]

    for sala in lista_salas:
        objsala = Sala(sala["idSala"], sala["capacidad"], sala["recursos"])
        salas.append(objsala)

    for reserva in lista_reservas:
        objresv = Reserva(reserva["idResv"], reserva["DNI"], reserva["fecha"], reserva["ini"], reserva["fin"])
        reservas.append(objresv)

    for user in lista_users:
        objuser = Usuario(user["DNI"], user["Nick"], user["passwd"])
        users.append(objuser)

def main():
    jsonparser()
    



#Para la funcion main
if __name__ == '__main__':
    main()
