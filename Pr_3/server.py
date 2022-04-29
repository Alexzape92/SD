import json
from operator import truediv
import pdb
from bottle import request, response, put, get, route, post, run, template

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
        return "idSala = {}, capacidad = {}, recursos = {}".format(self.idSala, self.capacidad, self.recursos)
    def __repr__(self):
        return "idSala = {}, capacidad = {}, recursos = {}".format(self.idSala, self.capacidad, self.recursos)

class Reserva:
    def __init__(self, idReserva, idSala, DNI, fecha, ini, fin):
        self.idReserva = idReserva
        self.idSala = idSala
        self.DNI = DNI
        self.fecha = fecha
        self.ini = ini
        self.fin = fin
    def __str__(self):
        return "idReserva = % s, idSala = %s ,DNI = % s, fecha = % s, HoraInicio = % s, HoraFin = % s" % \
        (self.idReserva, self.idSala, self.DNI, self.fecha, self.ini, self.fin)
    def __repr__(self):
        return "idReserva = % s, idSala = %s ,DNI = % s, fecha = % s, HoraInicio = % s, HoraFin = % s" % \
        (self.idReserva, self.idSala ,self.DNI, self.fecha, self.ini, self.fin)

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
        objresv = Reserva(reserva["idResv"], reserva["idSala"], reserva["DNI"], reserva["fecha"], reserva["ini"], reserva["fin"])
        reservas.append(objresv)

    for user in lista_users:
        objuser = Usuario(user["DNI"], user["Nick"], user["passwd"])
        users.append(objuser)

@post('/addRoom')
def add_room():
    datosSala = request.json

    id = datosSala['idSala']
    cap = datosSala['capacidad']
    rss = datosSala['recursos']

    sala = Sala(id, cap, rss)

    salas.append(sala)

@get('/showInformationRoom/<id>')
def show_room(id):
    for sala in salas:
        if(sala.idSala == id):
            break

    auxdict = {
        "idSala": sala.idSala,
        "capacidad": sala.capacidad,
        "recursos": sala.recursos
    }
    return json.dumps(auxdict, indent=4)

@post('/addBooking')
def add_resrv():
    datosResrv = request.json

    idr = datosResrv['idReserva']
    ids = datosResrv['idSala']
    dni = datosResrv['DNI']
    fec = datosResrv['fecha']
    horaini = datosResrv['HoraInicio']
    horafin = datosResrv['HoraFin']

    if not salaOcupada(ids):
        reserva = Reserva(idr, ids, dni, fec, horaini, horafin)
        reservas.append(reserva)
    else:
        


def salaOcupada(ids):
    for resv in reservas:
        if(resv.idSala == ids):
            return True
    return False

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True)