import json
from operator import truediv
import pdb
from bottle import request, response, put, get, route, post, run, template

#Guardamos las listas del JSON en el ámbito global, para tenerlas siempre disponibles
salas = list()
reservas = list()
users = list()

#Reserva incremental
ultres = 0

#Definimos las clases a usar
class Sala:
    def __init__(self, idSala, capacidad, recursos):    #Recursos es una lista de strings
        self.idSala = idSala
        self.capacidad = capacidad
        self.recursos = recursos
    
    def __str__(self):
        return "roomId = {}, capacity = {}, resources = {}".format(self.idSala, self.capacidad, self.recursos)
    def __repr__(self):
        return "roomId = {}, capacity = {}, resources = {}".format(self.idSala, self.capacidad, self.recursos)

class Reserva:
    def __init__(self, idReserva, idSala, DNI, fecha, ini, fin):
        self.idReserva = idReserva
        self.idSala = idSala
        self.DNI = DNI
        self.fecha = fecha
        self.ini = ini
        self.fin = fin
    def __str__(self):
        return "bookingId = % s, roomId = %s ,DNI = % s, date = % s, startTime = % s, endTime = % s" % \
        (self.idReserva, self.idSala, self.DNI, self.fecha, self.ini, self.fin)
    def __repr__(self):
        return "bookingId = % s, roomId = %s ,DNI = % s, date = % s, startTime = % s, endTime = % s" % \
        (self.idReserva, self.idSala ,self.DNI, self.fecha, self.ini, self.fin)

class Usuario:
    def __init__(self, DNI, nick, passwd):
        self.DNI = DNI
        self.nick = nick
        self.passwd = passwd
    def __str__(self):
        return "DNI = % s, UserName = % s, password = % s" % (self.DNI, self.nick, self.passwd)
    def __repr__(self):
        return "DNI = % s, UserName = % s, password = % s" % (self.DNI, self.nick, self.passwd)

def jsonparser():
    file_name = "DB.json"
    with open(file_name) as f:
        data = json.load(f)
    
    lista_salas = data["Salas"]
    lista_reservas = data["Reservas"]
    lista_users = data["Usuarios"]

    for sala in lista_salas:
        objsala = Sala(sala["roomId"], sala["capacity"], sala["resources"])
        salas.append(objsala)

    for reserva in lista_reservas:
        objresv = Reserva(reserva["bookingId"], reserva["roomId"], reserva["DNI"], reserva["date"], reserva["startTime"], reserva["endTime"])
        reservas.append(objresv)

    for user in lista_users:
        objuser = Usuario(user["DNI"], user["userName"], user["password"])
        users.append(objuser)

@post('/addRoom')
def add_room():
    datosSala = request.json

    if not checkCredenciales(datosSala['user'], datosSala['passw']):
        return "Credenciales no válidas"
    else:
        id = datosSala['roomId']
        cap = datosSala['capacity']
        rss = datosSala['resources']

        sala = Sala(id, cap, rss)

        salas.append(sala)

@get('/showInformationRoom/<id>')
def show_room(id):
    datosUser = request.json

    if not checkCredenciales(datosUser['user'], datosUser['passw']):
        return "Credenciales no válidas"
    else:
        for sala in salas:
            if(sala.idSala == id):
                break

        auxdict = {
            "roomId": sala.idSala,
            "capacity": sala.capacidad,
            "resources": sala.recursos
        }
        return json.dumps(auxdict, indent=4)

@post('/addBooking')
def add_resrv():
    datosResrv = request.json
    global ultres

    if not checkCredenciales(datosResrv['user'], datosResrv['passw']):
        return "Credenciales no válidas"
    else:
        ids = datosResrv['roomId']
        fec = datosResrv['date']
        horaini = datosResrv['startTime']
        horafin = datosResrv['endTime']

        if not salaOcupada(ids, fec, horaini, horafin):
            for u in users:
                if u.nick == datosResrv['user'] and u.passwd == datosResrv['passw']:
                    break
            reserva = Reserva(ultres, ids, u.DNI, fec, horaini, horafin)
            reservas.append(reserva)
            ultres = ultres + 1
        else:
            ocupDict = {
                "La sala que desea reservar está ocupada":[

                ]
            }
            for s in salas:
                if not salaOcupada(s.idSala, fec, horaini, horafin):
                    ocupDict["La sala que desea reservar está ocupada"].append(s.__str__())
            
            outjson = json.dumps(ocupDict)
            return outjson

@get('/showBookings/<dni>')
def mostrar_resvs(dni):
    datosUser = request.json

    if not checkCredenciales(datosUser['user'], datosUser['passw']):
        return "Credenciales no válidas"

    resdict = {
        'reservas' : []
    }
    for r in reservas:
        if r.DNI == dni:
            rdict = {
                "bookingId" : r.idReserva,
                "roomId"    : r.idSala,
                "DNI"       : r.DNI,
                "date"     : r.fecha,
                "startTime"   : r.ini,
                "endTime"   : r.fin
            }
            resdict["reservas"].append(rdict)
    
    resjson = json.dumps(resdict, indent=4)
    return resjson

@put('/deleteBooking/<id>')
def borrar_resv(id):
    datosUser = request.json

    if not checkCredenciales(datosUser['user'], datosUser['passw']):
        return "Credenciales no válidas"
    
    for r in reservas:
        if str(r.idReserva) == id:
            reservas.remove(r)
            return json.dumps("Reserva eliminada")
    
    return json.dumps("No existe el identificador de la reserva")

@post('/exit')
def salir():
    file_name = "DB.json"
    with open(file_name, "r") as f:
        data = json.loads(f.read())

    for s in salas:
        sala = {
            "roomId": s.idSala,
            "capacity": s.capacidad,
            "resources": s.recursos
        }
        data['Salas'].append(sala)

    for r in reservas:
        rsv = {
            "bookingId": r.idReserva,
            "roomId": r.idSala,
            "DNI" : r.DNI,
            "date": r.fecha,
            "startTime": r.ini,
            "endTime": r.fin
        }
        data['Reservas'].append(rsv)
    
    with open(file_name, "w") as f:
        json.dump(data, f)
    
    exit(1)

            

#FUNCIONES AUXILIARES----------------------------------------------------------------------------------------------
def salaOcupada(ids, fec, horaini, horafin):
    for resv in reservas:
        if resv.idSala == ids and resv.fecha == fec and horaini < resv.fin and horafin > resv.ini:
            return True
    return False

def checkCredenciales(user, passw):
    for u in users:
        if u.nick == user and u.passwd == passw:
            return True
    return False

if __name__ == '__main__':
    jsonparser()
    run(host='localhost', port=8000, debug=True)