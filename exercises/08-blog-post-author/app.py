import requests

# Your code here
respuesta=requests.get('https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php')

if respuesta.status_code ==200:
    body= respuesta.json()

    nombre= body['posts'][0]['author']['name']
    print(nombre)
