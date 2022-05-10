import json
from urllib import response
import requests

headers = {'Content-Type': 'application/json'}  #Para indicarle al data que es un json

def main():
    while True:
        user = input("Introduce tu nombre de usuario: ")
        passw = input("Introduce tu contraseña: ")


        print("\t1. Añadir sala")
        print("\t2. Mostrar información de la sala")
        print("\t3. Añadir reserva")
        print("\t4. Listar reservas")
        print("\t5. Eliminar reserva")
        print("\t6. Exit")
        print("")

        opcion = input("Selecciona la opción: ")

        if opcion == '1':
            print("AÑADIR SALA----------------------------------------------------")
            id = input("Introduce el id de la sala: ")
            cap = input("Introduce la capacidad de la sala: ")
            rss = list()

            aux = input("Introduce un recurso de [proyector, pizarra, rotuladores, altavoces, micrófono, puntero láser] ('fin' para terminar): ")
            if aux != 'fin': rss.append(aux)
            while aux != 'fin':
                aux = input("Introduce un recurso de [proyector, pizarra, rotuladores, altavoces, micrófono, puntero láser] ('fin' para terminar): ")
                if aux != 'fin': rss.append(aux)
            
            saladict = {
                "roomId": id,
                "capacity": cap,
                "resources": rss,
                "user": user,
                "passw": passw
            }

            anadir_sala(json.dumps(saladict, indent=4))
        
        if opcion == '2':
            print("MOSTRAR SALA--------------------------------------------------------")
            id = input("Introduce el id de la sala: ")

            userjson = json.dumps({"user":user, "passw":passw}, indent=4)
            ver_sala(userjson, id)
            
        if opcion == '3':
            print("AÑADIR RESERVA--------------------------------------------------------")
            ids = input("Introduce el id de la sala a reservar: ")
            fec = input("Introduce la fecha de la reserva")
            ini = input("Introduce la hora de entrada")
            fin = input("Introduce la hora de salida")

            resvdict = {
                "roomId": ids,
                "date": fec,
                "startTime": ini,
                "endTime":fin,
                "user": user,
                "passw": passw
            }

            resvjson = json.dumps(resvdict, indent=4)
            anadir_rsv(resvjson)
        
        if opcion == '4':
            print("LISTAR RESERVAS-------------------------------------------------")
            userjson = json.dumps({"user":user, "passw":passw}, indent=4)
            dni = input("Introduce tu dni: ")   #Debemos preguntarle, la única alternativa sería añadir un endpoint que nos devuelva el dni dado el usuario y contraseña

            ver_reservas(userjson, dni)
        
        if opcion == '5':
            print("ELIMINAR RESERVA----------------------------------------------------------")
            userjson = json.dumps({"user":user, "passw":passw}, indent=4)
            id = input("Introduce el id de la reserva a eliminar: ")

            borrar_reserva(userjson, id)

        if opcion == '6':
            print("Hasta la próxima!")
            requests.post(url='http://localhost:8000/exit')
            exit()

def anadir_sala(salajson):
    if requests.post(url='http://localhost:8000/addRoom', data=salajson, headers=headers).text == 'Credenciales no válidas':
        print('Credenciales no válidas')
        exit()

def ver_sala(userjson, id):
    resp = requests.get(url='http://localhost:8000/showInformationRoom/{}'.format(id), data=userjson, headers=headers).text

    if resp == 'Credencialies no válidas':
        print(resp)
        exit()

    resp_str = json.loads(resp)
    print(resp_str)

def anadir_rsv(resjson):
    resp = requests.post(url='http://localhost:8000/addBooking', data=resjson, headers=headers).text

    if len(resp) > 0:
        if resp == 'Credenciales no válidas':
            print(resp)
            exit()

        resp_str = json.loads(resp)
        print(resp_str)

def ver_reservas(userjson, dni):
    resp = requests.get(url='http://localhost:8000/showBookings/{}'.format(dni), data=userjson, headers=headers).text

    if resp == 'Credenciales no válidas':
        print(resp)
        exit()

    resp_str = json.loads(resp)
    print(resp_str)

def borrar_reserva(userjson, id):
    resp = requests.put(url='http://localhost:8000/deleteBooking/{}'.format(id), data=userjson, headers=headers).text

    if resp == 'Credenciales no válidas':
        print(resp)
        exit()

    resp_str = json.loads(resp)
    print(resp_str)

if __name__ == '__main__':
    main()
