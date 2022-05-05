import json
from urllib import response
import requests

headers = {'Content-Type': 'application/json'}  #Para indicarle al data que es un json

user = input('Introduce tu nick: ')
passw = input('Introduce tu contraseña: ')

saladict = {
    "idSala": 21,
    "capacidad": 50,
    "recursos": ["proyector", "rotuladores", "altavoces"],
    "user": user,
    "passw": passw
}

salajson = json.dumps(saladict, indent = 4)
if requests.post(url='http://localhost:8000/addRoom', data=salajson, headers=headers).text == 'Credenciales no válidas':
    print('Credenciales no válidas')
    exit()

#userdict = {
#    "user": user,
#    "passw": passw
#}

#userjson = json.dumps(userdict, indent=4)
#resp = requests.get(url='http://localhost:8000/showInformationRoom/21', data=userjson, headers=headers).text

#if resp == 'Credencialies no válidas':
#    print(resp)
#    exit()

#resp_str = json.loads(resp)
#print(resp_str)

resdict = {
    "user": user,
    "passw": passw,
    "idSala": 21,
    "fecha": '6/5/2022',
    "HoraInicio": "16:00",
    "HoraFin": "18:30"
}

resjson = json.dumps(resdict, indent=4)
resp = requests.post(url='http://localhost:8000/addBooking', data=resjson, headers=headers).text

if len(resp) > 0:
    if resp == 'Credenciales no válidas':
        print(resp)
        exit()

    resp_str = json.loads(resp)
    print(resp_str)

resdict = {
    "user": user,
    "passw": passw,
    "idSala": 21,
    "fecha": '6/5/2022',
    "HoraInicio": "16:00",
    "HoraFin": "18:30"
}

resjson = json.dumps(resdict, indent=4)
resp = requests.post(url='http://localhost:8000/addBooking', data=resjson, headers=headers).text

if len(resp) > 0:
    if resp == 'Credenciales no válidas':
        print(resp)
        exit()

    resp_str = json.loads(resp)
    print(resp_str)


