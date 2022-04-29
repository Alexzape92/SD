import json
from urllib import response
import requests

headers = {'Content-Type': 'application/json'}  #Para indicarle al data que es un json

saladict = {
    "idSala": 21,
    "capacidad": 50,
    "recursos": ["proyector", "rotuladores", "altavoces"]
}

salajson = json.dumps(saladict, indent = 4)
requests.post(url='http://localhost:8000/addRoom', data=salajson, headers=headers)

resp = requests.get('http://localhost:8000/showInformationRoom/21')
resp_json = json.loads(resp.text)

reservadict = {
    "idReserva": 1,
    "idSala": 21,
    "DNI": '32092444S',
    "fecha": '01/01/2023',
    "HoraInicio": '12:00',
    "HoraFin": '00:00'
}

reservajson = json.dumps(reservadict, indent=4)
requests.post(url='http://localhost:8000/addBooking', data=reservajson, headers=headers)
