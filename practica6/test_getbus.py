# importamos json
import json
# importamos requests
import requests
# importamos fecha y hora
from datetime import datetime
# solicitud de un pedido
# url de la solicitud
url1 = "http://localhost:54736/api/bus/"
# hacemos una funcion de respuesta que retornará el metodo get del request

def respuesta(url):
    return requests.get(url1)

# hacemos una funcion que corroborará el estado de la respuesta

def test_respuesta():
    assert respuesta(url1).status_code == 200
    