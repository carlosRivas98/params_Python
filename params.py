# Envía información al servidor a través de la URL
import requests
# El query es todo lo que se encuentra después del signo ?
# URL = "https://httpbin.org/get?name=Carlos &password=1234&email=prueba@gmail.com"
URL = "https://httpbin.org/get"

params = {
    'name': 'Carlos Daniel',
    'password': 123,
    'email': 'pueba@gmail.com '
}

response = requests.get(URL, params=params)

if response.status_code == 200:
     payload = response.json()
     params = payload['args']
     print(params['name'])
     print(params['password'])
     print(params['email'])

print(response.url)