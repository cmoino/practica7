
# importamos json
import json
# importamos requests
import requests
# formato json para el header del request
url1 = "http://localhost:54736/api/bus/agregar"
headers = {
    'content-type': 'application/json'
}
# guardamos en una variable tipo json el pedido agregar
data = {
    "id": 5,
    "descripcion": "Pedido 10",
    "idrestaurante": 1,
    "idrepartidor": 1,
    "idcliente": 1,
    "estado": 1
}
# hacemos el request tipo post y lo guardamos en un response
def post_pedido(header, data, url):
    return requests.post(url, data=json.dumps(data),headers=header)

def test_post_pedido():
    assert post_pedido(headers,data,url1).status_code == 500

